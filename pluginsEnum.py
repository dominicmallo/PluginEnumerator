import os, getpass, requests, re, json, time


userName = getpass.getuser()



chromePluginsPath = "C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions".format(userName)
chromePlugins = next(os.walk(chromePluginsPath))[1]

try:
    chromePlugins.remove('Temp')
except:
    print("no tmp folder")

allOutput = ["----------------------"]




for chromePlugin in chromePlugins:
    
    chromePluginPath = "C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Extensions\\{}".format(userName,chromePlugin)
    chromePluginVersion = next(os.walk(chromePluginPath))[1]

    
    chromePlugin = str(chromePlugin)
    chromePluginURL = "https://chrome.google.com/webstore/detail/{}".format(chromePlugin)
    chromePluginPage = requests.get(chromePluginURL)
    chromePluginName = re.search('<title>(.*)</title>', str(chromePluginPage.content))
    chromePluginName = chromePluginName.group(1)
    
    output = (chromePluginName + " - " + chromePluginURL + " - " + str(chromePluginVersion[0]))
    allOutput.append(output)
    print(output)


    chromePluginManifest = open(str(chromePluginPath + "\\" + chromePluginVersion[0] + "\\" + "manifest.json"), "r").read()

    chromePluginManifestContents = json.loads(chromePluginManifest)

    if "permissions" in chromePluginManifestContents.keys():
        output2 = ("has access:" + str(chromePluginManifestContents["permissions"]))
        allOutput.append(output2)
        print(output2)

        

    output3 = "----------------------"
    allOutput.append(output3)
    print(output3)


    #clear vars
    chromePluginManifestContents = ""
    chromePluginPath = ""
    chromePluginVersion = ""
    chromePluginManifest = ""
    chromePluginName = ""
    chromePluginURL = ""



f = open(userName + "-"  + str(round(time.time())) + ".txt", "a")
for output in allOutput:
    f.write(output + "\n")
f.close()
    
