import urllib.request, requests, os

#URL of website to pull images from
URL = "https://designyoutrust.com/2019/08/artist-creates-modern-landscapes-in-his-unique-abstract-style/"

#location to save images to (can be left blank if using default path)
PATH = "D:/Pictures/PulledFromInternet/"

#Use default path for pictures library?
DefaultPicturesPath = True

#set to JPEG by default 
EXTENSTION = ".jpg"

#Name of Folder To Save into and prefix for filenames
name = "Jason Anderson Abstract Landscapes "


#Image counter - do not change
n = 0
def getExtention(FileURL):
    global EXTENSTION
    Extensions = [".jpg", ".jpeg" , ".bmp", ".gif", ".png", ".vec"]
    for ex in Extensions:
        if ex in FileURL:
            EXTENSTION = ex
    return
def DownloadIMG(FileURL):
    global n
    print("File URL: ", FileURL)
    getExtention(FileURL)
    print("downloading image from URL...")
    urllib.request.urlretrieve(FileURL, PATH +  name + str(n) + EXTENSTION)
    print("Saved into location: ", PATH + name + str(n) + EXTENSTION)
    n += 1
    return


def FindImages():
    currentLine = ""
    foundSource = False
    IMGTag = False
    FileURL = ""
    r = requests.get(URL)
    for i in range(len(r.text)):
        character = r.text[i]
        FileURL = ""
        foundSource = False
        if currentLine == "<img":
            IMGTag = True
            print("Found img tag")
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
    if not IMGTag:
        print("No img tags found")
    return
def init():
    global PATH
    if DefaultPicturesPath:
        import ctypes.wintypes
        SHGFP_TYPE_CURRENT = 0   # Want current, not default value
        ID = 39 # ID for Picture Folder Location
        buf = ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(0, ID, 0, SHGFP_TYPE_CURRENT, buf)
        PATH = buf.value + "/"
        
    PATH += (name + "/")
    # Create target Directory if don't exist
    if not os.path.exists(PATH):
        os.mkdir(PATH)
        print("Directory " , PATH ,  " Created ")
    else:    
        print("Directory " , PATH ,  " already exists")
    return
init()
try:
    FindImages()
except (KeyboardInterrupt, SystemExit):
    print("--------------")
    print("Program halted")
    print("--------------")
