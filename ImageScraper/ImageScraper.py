import urllib.request, requests
URL = "https://designyoutrust.com/2019/01/artist-creates-illustrations-that-turn-loneliness-into-magic/"
PATH = "D:/Pictures/PulledFromInternet/"
EXTENSTION = ".jpg"


n = 0
name = " Jenny Wu "

def DownloadIMG(FileURL):
    global n
    print("File URL: ", FileURL)
    print("downloading image from URL...")
    urllib.request.urlretrieve(FileURL, PATH + name + str(n) + EXTENSTION)
    print("Saved into location: ", PATH + name + str(n) + EXTENSTION)
    n += 1



def FindImages():
    currentLine = ""
    foundSource = False
    FileURL = ""

    r = requests.get(URL)
    for i in range(len(r.text)):
        character = r.text[i]
        FileURL = ""
        foundSource = False
        if currentLine == "<img":
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
                        DownloadIMG(FileURL)
                        currentLine = ""
                        break
                if currentLine == "src=\"":
                    foundSource = True
                    
        if character == '<':
            currentLine = ""
        currentLine += character


FindImages()
