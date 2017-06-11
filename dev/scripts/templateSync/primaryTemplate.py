# primaryTemplate.py
#
# A file dedicated to retemplating pages following the primary style on the site.
# No other styles are currently underway, but having independent files for each will make it more repurposeable in the future.

def findContentRange(arr):
    start = -1
    finish = -1
    for i, line in enumerate(arr):
        if "<!-- begin content anchor !-->" in line:
            start = i
        elif "<!-- end content anchor !-->" in line:
            finish = i
    return [start, finish]

def toString(arr):
    string = ""
    for x in arr:
        string += x + "\n"
    return string

def assignSelectedHeader(page, index):
    arr = page.split("navunselected")
    tmp = ""
    for i, text in enumerate(arr):
        tmp += text
        if i == index:
            tmp += "navselected"
        elif i < (len(arr)-1):
            tmp += "navunselected"

    return tmp
print "primaryTemplate.py"
print "Beginning implementation of templateMain.html"

print "Reading template file . . ."
path = "../templates/templateMain.html"
templateFile = open(path, "r")
templateFull = templateFile.read().split("\n")
templateFile.close()
print "Done!"

templateContentRange = findContentRange(templateFull)

print "Template consists of all lines before line " + str(templateContentRange[0] + 1) + " and all lines after " + str(templateContentRange[1] + 1)

print "Reading config file . . ."
config = open("templateSync/primary.cfg", "r")
configFull = config.read().split("\n")
config.close()
print "Done!"

root = "../../"
for line in configFull:
    entry = line.split(":")
    path = entry[0]
    navIndex = int(entry[1])

    print "Templating file " + path + " with header index " + str(navIndex)
    print "Opening file . . ."
    contentRead = open(root + path, "r")
    contentArr = contentRead.read().split("\n")
    contentRead.close()
    print "Done!"
    
    contentRange = findContentRange(contentArr)
    if -1 in contentRange:
        print "Error: Missing a content anchor."
        continue
    else:
        print "Content consists of lines between " + str(contentRange[0]+1) + " and " + str(contentRange[1]+1)
        
    print "Writing merged file . . ."
    fullArr = templateFull[0:templateContentRange[0]]
    fullArr.extend(contentArr[contentRange[0]:contentRange[1]])
    fullArr.extend(templateFull[templateContentRange[1]:len(templateFull)-1])
    
    mergedStr = toString(fullArr)

    print "Assigning 'selected' navbar element"
    mergedStr = assignSelectedHeader(mergedStr, navIndex)
    
    contentWrite = open(root + path, "w")
    contentWrite.write(mergedStr)
    contentWrite.close()
    print "Done!"
    
print "Finished template implementation for templateMain.html"
