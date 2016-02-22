import pycurl
import certifi
import json
import pickle
from text_edit import *
from StringIO import StringIO

def save_data(data, file):
    with open(file, "wb") as f:
        pickle.dump(data, f)

def load_data(p_tree):
    try:
        with open(p_tree) as f:
            x, y = pickle.load(f)
    except:
        x, y = [], []
    return x, y

def print_dict(dictionary, ident = '', braces=1):
    """ Recursively prints nested dictionaries."""

    for key, value in dictionary.iteritems():
        if isinstance(value, dict):
            print '%s%s%s%s' %(ident,braces*'[',key,braces*']')
            print_dict(value, ident+'  ', braces+1)
        elif isinstance(value, list):
            for i in value:
                if isinstance(i, dict):
                    print '%s%s%s%s' %(ident,braces*'[',key,braces*']')
                    print_dict(i, ident+'  ', braces+1)
        else:
            print ident+'%s = %s' %(key, value)

username = ''
password = ''
input_text = ''

chapters, index = sep_chap(input_text)

chapters = chapters[0:index+1]
print len(chapters)
data = ''
i = 1
splits = []
trees = []
while i<=index:

    #Group Chapters together to make sure they are 3500words+ entries to send to BlueMix
    while len(data.split())<3500 and i<= index:
        data += chapters[i]
        i += 1

    if (i==index) and (len(chapters[i].split())<3500):
        data += chapters[i]
        i+1

    print "split at: "
    print i

    splits.append(i) #So we know which chapters were grouped together for the next stage

    #PyCurl Calls
    c = pycurl.Curl()
    buffer = StringIO()
    c.setopt(c.URL,'https://gateway.watsonplatform.net/personality-insights/api')
    c.setopt(pycurl.USERPWD, '%s:%s' % (username, password))
    c.setopt(pycurl.CAINFO, certifi.where())
    #result = c.perform()

    c.setopt(pycurl.POST, 1)
    c.setopt(c.URL,'https://gateway.watsonplatform.net/personality-insights/api/v2/profile')
    c.setopt(pycurl.HTTPHEADER, ['Content-Type: text/plain'])
    c.setopt(pycurl.USERPWD, '%s:%s' % (username, password))
    c.setopt(pycurl.POSTFIELDS, data)
    c.setopt(pycurl.CAINFO, certifi.where())
    c.setopt(pycurl.WRITEFUNCTION, buffer.write)
    c.perform()
    c.close()

    body = buffer.getvalue()
    # Body is a string in some encoding.
    # In Python 2, we can print it without knowing what the encoding is.


    parsed = json.loads(body)
    trees.append(parsed) #Appends the retrieved personality tree

    data = ''

save_data([trees, splits], "bin2.dat") #Saves the list of personality trees
