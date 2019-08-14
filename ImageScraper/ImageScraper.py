import urllib.request, requests
URL = "https://designyoutrust.com/2019/01/artist-creates-illustrations-that-turn-loneliness-into-magic/"
PATH = "D:/Pictures/PulledFromInternet/"
EXTENSTION = ".jpg"
name = " Jenny Wu "
n = 0

def DownloadIMG():
    global n
    print("File URL: ", FileURL)
    print("downloading image from URL...")
    urllib.request.urlretrieve(FileURL, PATH + name + str(n) + EXTENSTION)
    print("Saved into location: ", PATH + name + str(n) + EXTENSTION)
    n += 1




r = requests.get(URL)
currentLine = ""
imgTag = False
foundSource = False
FileURL = ""
for i in range(len(r.text)):
    character = r.text[i]
    FileURL = ""
    foundSource = False
    if currentLine == "<img":
        imgTag = True
        currentLine = ""
        while character != ">":
            character = r.text[i]
            i += 1
            character = r.text[i]
            currentLine += character
            if character == " ":
                currentLine = ""
            if foundSource:
                if character != " ":
                    FileURL += character
                else:
                    DownloadIMG()
                    currentLine = ""
                    break
            if currentLine == "src=\"":
                foundSource = True
                
    if character == '<':
        currentLine = ""
    currentLine += character




#page_source = response.read()
#urllib.request.urlretrieve(URL, PATH + name)
