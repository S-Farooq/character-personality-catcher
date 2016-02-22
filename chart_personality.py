import matplotlib.pyplot as plt
import numpy as np
from retrieve_personality import *


trees, splits = load_data('bin.dat')
trees = trees[:]

#Data structures to hold personality tree
percentages = {}
primary_p = {}
primary_p['personality'] = []
primary_p['percentage'] = []

#percentages_big = {}
index =0
for parsed in trees:
    print '%s out of %s:' %(index+1, len(trees))
    index += 1
    #print "Word Count: "
    #print parsed['word_count']
    for basics in parsed['tree']['children']:
        if basics['id'] == 'personality':
            for primary in basics['children']:
                primary_p['personality'].append(primary['id'])
                primary_p['percentage'].append(float(primary['percentage']))


                for secondary in primary['children']:
                    if (secondary['id'] not in percentages.keys()):
                        percentages[secondary['id']] = {}
                        percentages[secondary['id']][secondary['id']+'_BIG'] = []
                        percentages[secondary['id']][secondary['id']+'_BIG'].append(float(secondary['percentage']))
                    else:
                        percentages[secondary['id']][secondary['id']+'_BIG'].append(float(secondary['percentage']))

                    for traits in secondary['children']:
                        if (traits['id'] not in percentages[secondary['id']].keys()):
                            percentages[secondary['id']][traits['id']]= []
                            percentages[secondary['id']][traits['id']].append(float(traits['percentage']))
                        else:
                            percentages[secondary['id']][traits['id']].append(float(traits['percentage']))

                        for key, value in traits.iteritems():
                            if key == 'id':
                                print key, value
                            elif key == 'percentage':
                                print key, value
                    print "-----\n"


#Groups of chapters
x_a = range(0,15,1)
x_names = ['1-2','3','4-5','6-7', '8-9', '10-11', '12-13', '14-15', '16-17', '18-19', '20-21', '22-23', '24', '25', '26']

#Plot on a single plot the Big Five
plt.xticks(x_a,x_names)
plt.plot(primary_p['percentage'])
plt.title('Primary Personality')
plt.xlabel('Chapters', size=22)
plt.ylabel('Percentages (%)', size=22)
index = 0
for label in primary_p['personality']:
    label_e = label[0:1]
    plt.annotate(label_e, xy = (index,primary_p['percentage'][index]),xytext=(index-0.05, 0.95))
    index += 1
plt.show()

#Separate plot for each big five personality, including the minor traits
for keys, values in percentages.iteritems():
    fig = plt.figure()
    plt.xticks(rotation=70)
    ax = fig.add_subplot(111)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0+0.05, box.width * 0.8, box.height*0.95])
    ax.set_xticks(x_a)
    ax.set_xticklabels(x_names)
    percent = percentages[keys][keys+'_BIG']
    percent = [x * 100 for x in percent]
    print np.shape(percent)
    ax.plot(x_a, percent, label=keys, linestyle='--')
    plt.title(keys)
    #plt.tight_layout()
    for traits, perc in percentages[keys].iteritems():
        if traits != (keys+'_BIG'):
            perc = [x * 100 for x in perc]
            ax.plot(x_a,perc, label=traits)
            ax.axis([0,14,0,100])
            ax.set_xlabel('Chapters', size=22)
            ax.set_ylabel('Percentages (%)', size=22)
            ax.legend(loc='center right', bbox_to_anchor=(1.4, 0.5))
            ax.grid('on')
    plt.show()
