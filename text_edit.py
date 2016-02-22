import re

def sep_chap(input):
    chapters = ['']*100
    index = 0
    with open(input) as fp:
        for line in fp:
            if (re.match("\-+\sPage\s(\d+)\-+", line)):
                continue
            elif (re.match("^\s*\d+\s+$", line)):
                index += 1
            elif not (re.match("^\s+$", line)):
                chapters[index] += line

    return chapters, index
