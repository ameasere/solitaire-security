##################################NOTE########################################
#In each control panel section, you may notice the programs seem in backwards
#order. This is deliberate to avoid any NameError not defined problems or just
#general logic errors. It makes sense to do them backwards as then the final
#module that runs everything has all of the methods and data it needs to run.
##############################################################################
#####REQUIRED MODULES#####
import requests
import os
import base64
import pyminizip
from tkinter import *
import warnings
import webbrowser
import zipfile
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import ntpath
from Cryptodome.Cipher import AES
from ruamelmod import delete_from_zip_file
import urllib
from PIL import Image, ImageTk
from itertools import count
import random
import platform,socket,re,uuid,psutil,logging
##########################
#####SUPPRESS WARNINGS####
warnings.filterwarnings("ignore") # Remove this if you are getting errors
##########################
tempArr = [] #Temporary array used at the beginning of login
#####CUSTOM COLORS########
class bcolors:
    HEADER = '\033[95m' #Header colors
    OKBLUE = '\033[94m' #Blue
    OKCYAN = '\033[96m' #Cyan
    OKGREEN = '\033[92m' #Green
    WARNING = '\033[93m' #Red warning
    FAIL = '\033[91m' #Failure
    ENDC = '\033[0m' #End of colored message
    BOLD = '\033[1m' #Bold
    UNDERLINE = '\033[4m' #Underline
class userInfo:
    def __init__(self, username, password):
        data2 = {"Username": username, "Password": password} #Create JSON object
        url = "https://192.168.1.120/SolitaireSec/queryKeys.php/" #URL to send to
        headers = {} #Blank headers
        r = requests.post(url, data=data2, headers=headers, verify=False) #POST JSON object
        gcmdata = r.content #Get server response
        keyarray = gcmdata.split() #Split the array
        self.gcmkey = keyarray[0] #gcmkey = first element
        self.gcmiv = keyarray[1] #gcmiv = last element
    def getKey(self):
        return self.gcmkey
    def getIV(self):
        return self.gcmiv
class windowGen:
    def __init__(self, master, title, geometry, background):
        self.master = master
        self.title = title
        self.geometry = geometry
        self.background = background
        master.title(title)
        master.geometry(geometry)
        master.configure(bg=background)
    def createLabel(self, master, contents, fgcolor, bgcolor, horizontal, vertical):
        self.label = Label(master, text=contents, justify=LEFT, fg=fgcolor, bg=bgcolor, font="TkFixedFont")
        self.label.place(x=horizontal, y=vertical)
    def getEntry(self):
        return self.entry.get()
    def exitWindow(self):
        self.master.destroy()
    def createButton(self, master, contents, h, w, fgcolor, bgcolor, function, horizontal, vertical, param1, param2, param3, param4):
        if function == "getEntry":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=self.getEntry)
            self.button.place(x=horizontal,y=vertical)
        elif function == "selectArchive":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=selectArchive)
            self.button.place(x=horizontal,y=vertical)
            master.update()
        elif function == "newArchive":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=newArchive)
            self.button.place(x=horizontal,y=vertical)
            master.update()
        elif function == "displayArchive":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=displayArchive)
            self.button.place(x=horizontal,y=vertical)
        elif function == "extractArchive":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=extractArchive)
            self.button.place(x=horizontal,y=vertical)
        elif function == "deleteArchive":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=deleteArchive)
            self.button.place(x=horizontal,y=vertical)
        elif function == "logout":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=lambda: logout(None))
            self.button.place(x=horizontal,y=vertical)
        elif function == "selectFile":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=lambda: selectFile(param1, param2))
            self.button.place(x=horizontal,y=vertical)
        elif function == "getName":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=lambda: getName(param1, param2))
            self.button.place(x=horizontal,y=vertical)
        elif function == "processName":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=lambda: processName(param1, param2, param3))
            self.button.place(x=horizontal,y=vertical)
        elif function == "addToArchive":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=lambda: addToArchive(param1))
            self.button.place(x=horizontal,y=vertical)
        elif function == "removeFromArchive":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=removeFromArchive)
            self.button.place(x=horizontal,y=vertical)
        elif function == "renameArchive":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=renameArchive)
            self.button.place(x=horizontal,y=vertical)
        elif function == "closeArchive":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=closeArchive)
            self.button.place(x=horizontal,y=vertical)
        elif function == "renameFile":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=renameFile)
            self.button.place(x=horizontal,y=vertical)
        elif function == "contentsWindowObj.exitWindow":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=self.exitWindow)
            self.button.place(x=horizontal,y=vertical)
        elif function == "getPasswordZip":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=lambda: getPasswordZip(param1, param2))
            self.button.place(x=horizontal,y=vertical)
        elif function == "IssueRemove":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=lambda: IssueRemove(param1, param2))
            self.button.place(x=horizontal,y=vertical)
        elif function == "findFiles":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=lambda: findFiles(param1))
            self.button.place(x=horizontal,y=vertical)
        elif function == "interpretList":
            self.button = Button(master, text=contents, height=h, width=w, fg=fgcolor, bg=bgcolor, command=lambda: interpretList(param1))
            self.button.place(x=horizontal,y=vertical)
    def createEntry(self, master, horizontal, vertical, pw):
        if pw == "Yes":
            self.entry = Entry(master, show="*")
            self.entry.place(x=horizontal,y=vertical)
        else:
            self.entry = Entry(master)
            self.entry.place(x=horizontal,y=vertical)
##########################
#####ARRAYS###############
filearray = []
filearray2 = []
filearray3 = []
uforzip = []
fileCheck = []
##########################
#####RESET ARRAYS#########
def refreshArrays():
    global filearray
    filearray = [] #Set array to null
    global filearray2
    filearray2 = [] #Set array to null
    global filearray3
    filearray3 = [] #Set array to null
    global fileCheck
    fileCheck = [] #Set array to null
##########################
#####################LAST OPTION CONTROL PANEL#############################
#####Credits, please do not remove these###################################
def logout(windowClose):
    closeConfirm = messagebox.askokcancel("Close", "Close Solitaire Security?")
    if closeConfirm:
        print(f"{bcolors.HEADER}Thanks for using Solitaire Security.{bcolors.ENDC}") #Purple credits header
        print(f"{bcolors.OKCYAN}Credit: The Enigma Project\n\n GitHub: @projectintel-anon\n Email: leigh@enigmapr0ject.live\n Website: https://enigmapr0ject.live\n\n\n {bcolors.BOLD}Stay safe, guardian.{bcolors.ENDC}")
        #Cyan credits header with my socials :)
        exit(0)
    elif windowClose is None:
        print(f"{bcolors.HEADER}Thanks for using Solitaire Security.{bcolors.ENDC}") #Purple credits header
        print(f"{bcolors.OKCYAN}Credit: The Enigma Project\n\n GitHub: @projectintel-anon\n Email: leigh@enigmapr0ject.live\n Website: https://enigmapr0ject.live\n\n\n {bcolors.BOLD}Stay safe, guardian.{bcolors.ENDC}")
        #Cyan credits header with my socials :)
        exit(0)
###########################################################################
#####################END OF LAST OPTION CONTROL PANEL######################
######################OPTION 1 CONTROL PANEL###############################
def selectFile(newArchive, newArchiveObj):
    currentDir = os.getcwd() #Save current directory
    guiWindow.filename = askopenfilename(initialdir = currentDir, title= "Import a file") #Open a dialog box and save the file selected
    filearray.append(guiWindow.filename)
    try:
        filearray.remove(()) #Remove blank entries, prevents errors
    except ValueError: #Catch exception if there are none to remove to begin with
        pass #Skip
    updatedTitle = str(len(filearray)) + " file/s have been selected." #Text constructor to show how many files the user selected
    newArchiveObj.createLabel(newArchive, updatedTitle, "#00ffff", "#08198a", 0, 100) #Create a GUI label for it
    newArchive.update() #Update the GUI window to display aforementioned label
def checkIfExists(elem):
    for i in range(0, len(fileCheck)): #For each element in the array
        if elem == fileCheck[i]: #Set elem to current element that the program is looking at
            return True #return a boolean True value
            break #break the loop, saves time and processing power
        else:
            pass #Otherwise, skip to the next index
def processName(fileNamew, fileNamewObj, newArchiveObj):
    nameofarchive = fileNamewObj.getEntry() #Set nameofarchive to the entered name given by the user
    if len(nameofarchive) < 1: #If the array is populated
        fileNamewObj.createLabel(fileNamew, "Archive name empty", "#fa1a0a", "#08198a", 10, 100)
    else:
        obj = os.scandir(os.getcwd()) #Scan current directory
        for entry in obj: #For every entry returned
            if entry.is_file(): #If the entry is a file
                fileCheck.append(entry.name) #Add it to the array
            else:
                continue #Or if not, skip this one and keep looking
        if checkIfExists(nameofarchive) == True: #If the archive name already exists
            fileNamewObj.createLabel(fileNamew, "Archive name taken", "#fa1a0a", "#08198a", 10, 100)
        else:
            def getPasswordZip(passwordZip, passwordObj, newArchiveObj):
                zipPass = passwordObj.getEntry()
                if len(zipPass) < 1:
                    passwordObj.createLabel(passwordZip, "Empty password", "#fa1a0a", "#08198a", 0, 200)
                else:
                    passwordObj.exitWindow()
                    createArchive(newArchiveObj, nameofarchive, zipPass)
            fileNamewObj.exitWindow()
            passwordZip = Tk() #Initiate window
            passwordObj = windowGen(passwordZip, "Password for ZIP file", "250x250", "#08198a")
            passwordObj.createEntry(passwordZip, 0, 30, pw="Yes")
            passButton = Button(passwordZip, text="Continue", height=1, width=5, fg="white", bg="#fa1a0a", command=lambda: getPasswordZip(passwordZip, passwordObj, newArchiveObj))
            passButton.place(x=0, y=60)
            #passwordObj.createButton(passwordZip, "Continue", 1, 5, "white", "blue", "getPasswordZip", 0, 60, passwordZip, passwordObj, None, None)
def getNameArchive(newArchiveObj):
    fileNamew = Tk() #Initiate window
    fileNamewObj = windowGen(fileNamew, "Name (with .zip)", "250x250", "#08198a")
    fileNamewObj.createEntry(fileNamew, 0, 30, pw="No")
    fileNamewObj.createButton(fileNamew, "Continue", 1, 5, "white", "#fa1a0a", "processName", 0, 60, fileNamew, fileNamewObj, newArchiveObj, None)
def getName(newArchive, newArchiveObj):
    if len(filearray) < 1: #If this array isn't populated
        newArchiveObj.createLabel(guiWindow, "No files selected. Try again", "#fa1a0a", "white", 360, 350) #Create label to tell the
        #user about it
        newArchiveObj.exitWindow()
    else:
        pass #Or skip
    current = os.getcwd() #Save current directory again (redundant, I know)
    getNameArchive(newArchiveObj) #Progress forward
def createArchive(newArchiveObj, nameofarchive, zipPass):
    gcmkey = user.getKey()
    gcmiv = user.getIV()
    if len(gcmkey) < 1:
        GUI.createLabel(guiWindow, "Incorrect details.", "#fa1a0a", "#08198a", 360, 350)
        return None
    def path_leaf(path):
        head, tail = ntpath.split(path) #Split the path into head and tail
        return tail or ntpath.basename(head) #Only return the tail or base name of the head
    for i in range(0, len(filearray)): #For each element in array
        fileAdd = filearray[i] #Set element
        with open(fileAdd, "rb") as fileToAdd: #With the opened file as fileToAdd
            filecontents = fileToAdd.read() #Read the contents
            fileToAdd.close() #Close it (to avoid program hang)
        b64string = base64.b64encode(filecontents) #Base 64 encode it for safety
        cipher = AES.new(gcmkey, AES.MODE_CBC, gcmiv) #Create new cipherblock chain object
        data = b64string #Set the string to a new name for clarity
        length = 16 - (len(data) % 16) #Create padding length
        data += bytes([length]) * length #Add padding (avoids errors from Crypto
        ciphertext = cipher.encrypt(data) #Encrypt and save
        newName = path_leaf(fileAdd) #newName for file comes as a result of the ntpath function splitting path names
        with open(newName, "wb") as newFile: #With the new file name
            newFile.write(ciphertext) #Write the bytes in
            newFile.close() #Close (avoids program hang)
        filearray2.append(newName) #Add the name of the file to the array for later
    pyminizip.compress_multiple(filearray2, [], nameofarchive, zipPass, 5) #Compress the entire thing with PyMinizip and encrypt it with user's password
    #Args work as follows: filearray2 are the files to compress, [] is the path (we use current directory), nameofarchive for the name, pforzip[0] for password
    #and 5 for compression level, this gets the best of both worlds for compression amount and processing speed. Higher means more CPU usage but ultimate
    #storage conservation. Not necessary unless the ZIP is planned to be a HUGE archive around >250MB.
    obj2 = os.scandir(os.getcwd()) #Scan directory of the current directory
    for entry in obj2: #For each entry returned
        if nameofarchive == entry.name: #If the zip exists
            GUI.createLabel(guiWindow, "Successfully created!", "green", "#08198a", 360, 350)
            #Woohoo, tell the user it worked!
            guiWindow.update() #Let the GUI display said message
            archiveFound = 1 #Set archiveFound to 1
            newArchiveObj.exitWindow() #Close window
            for i in range(0, len(filearray2)): #For each element in this array
                if os.path.exists(filearray2[i]): #If the path exists
                    os.remove(filearray2[i]) #Remove the element
                else:
                    pass #Or if not, skip it
            break #Stop the entry in obj2 loop if the zip is found, no need for unnecessary processing when we have what we were looking for
        else:
            archiveFound = 0 #or if not found, set archiveFound = 0
    if archiveFound == 0: #If archive wasn't found
        newArchiveObj.exitWindow() #Close window
        GUI.createLabel(guiWindow, "Failed to create archive.", "#fa1a0a", "#08198a", 360, 350)
        #Tell the user
        guiWindow.update() #Let GUI display said message
def newArchive():
    refreshArrays() #Refresh all array values
    newArchive = Tk() #New window
    newArchiveObj = windowGen(newArchive, "Solitaire Security", "400x400", "#08198a")
    newArchiveObj.createButton(newArchive, "Import file", 1, 10, "white", "orange", "selectFile", 20, 20, newArchive, newArchiveObj, None, None)
    newArchiveObj.createButton(newArchive, "Create archive", 1, 10, "white", "blue", "getName", 20, 70, newArchive, newArchiveObj, None, None)
################# END OF OPTION 1 CONTROL PANEL ####################################################
################# OPTION 2 CONTROL PANEL ###########################################################
def selectArchive():
    def modifyContents(z, zipPass): #SubFunction
        updatedTitle = str(len(filearray)) + " file/s have been selected." #Show user how many files they selected
        GUI.createLabel(guiWindow, updatedTitle, "#00ffff", "#08198a", 360, 350)
        guiWindow.update()
        if len(filearray) > 0: #If the array is populated
            try:
                filelist = z.namelist()
                testfile = filelist[0]
            except Exception:
                GUI.createLabel(guiWindow, "Archive is empty.", "#fa1a0a", "#08198a", 360, 350)
                guiWindow.update()
                return 0
            try:
                z.extract(testfile, pwd=zipPass)
                os.remove(testfile)
                selectorWindow = Tk() #New window
                global chooseWindow
                chooseWindow = windowGen(selectorWindow, "Modify archive", "200x200", "#08198a")
                chooseWindow.createButton(selectorWindow, "Add files", 1, 10, "white", "#fa1a0a", "addToArchive", 0, 10, z, None, None, None)
                chooseWindow.createButton(selectorWindow, "Remove files", 1, 10, "white", "#fa1a0a", "removeFromArchive", 0, 60, None, None, None, None)
                chooseWindow.createButton(selectorWindow, "Rename archive", 1, 10, "white", "#00ffff", "renameArchive", 0, 110, None, None, None, None)
                chooseWindow.createButton(selectorWindow, "Close archive", 1, 10, "white", "#00ffff", "closeArchive", 0, 160, None, chooseWindow, None, None)
                selectorWindow.update()
            except RuntimeError as e:
                print(repr(e))
                GUI.createLabel(guiWindow, "Failed to open archive.", "#fa1a0a", "#08198a", 360, 350)
                guiWindow.update()
            #Tell the user that they don't have access to this ZIP.
                filearray.pop(0) #And remove the element that it just added
                return None #And move on
    def openArchive(zipPass):
        z = zipfile.ZipFile(filearray[0], 'a') #Set zipfile object
        zipPass = bytes(zipPass, encoding='utf-8')
        z.setpassword(zipPass) #Set password
        modifyContents(z, zipPass) #Run function
    refreshArrays() #Refresh all arrays
    currentDir = os.getcwd() #Save current directory (this is really redundant, sorry)
    guiWindow.filename = askopenfilename(initialdir=currentDir, title="Import a file", filetypes = (("ZIP archive","*.zip"),)) #Allow only selection of ZIPs
    try:
        testerfile = guiWindow.filename[0]
    except Exception:
        return 0
    filearray.append(guiWindow.filename) #Add the selected name to the array
    try:
        filearray.remove(()) #Remove blank entries to avoid errors
    except ValueError:
        pass #Or if there are none, skip step
    def getPasswordZip(passwordZip, passwordObj):
        zipPass = passwordObj.getEntry()
        if len(zipPass) < 1:
            passwordObj.createLabel(passwordZip, "Empty password", "#fa1a0a", "#08198a", 0, 200)
        else:
            passwordObj.exitWindow()
            openArchive(zipPass)
    passwordZip = Tk() #Initiate window
    passwordObj = windowGen(passwordZip, "Password for ZIP file", "250x250", "#08198a")
    passwordObj.createEntry(passwordZip, 0, 30, pw="Yes")
    passButton = Button(passwordZip, text="Continue", height=1, width=5, fg="white", bg="#fa1a0a", command=lambda: getPasswordZip(passwordZip, passwordObj))
    passButton.place(x=0, y=60)
def addToArchive(z):
    gcmkey = user.getKey()
    gcmiv = user.getIV()
    if len(gcmkey) < 1:
        GUI.createLabel(guiWindow, "Incorrect details.", "#fa1a0a", "#08198a", 360, 350)
        return None
    currentDir = os.getcwd() #Save current directory (My gosh, I am so sorry for this repetition!)
    guiWindow.filename = askopenfilename(initialdir=currentDir, title="Import a file") #Find file prompt
    filearray3.append(guiWindow.filename) #Add to array
    try:
        filearray3.remove(()) #Remove blank entry
        filearray3.remove('') #Remove blank entry
    except ValueError:
        pass #If there are none, skip step
    if len(filearray3) < 1: #If array is empty
        GUI.createLabel(guiWindow, "Cannot add empty files", "#fa1a0a", "#08198a", 360, 350) #Tell the user
        guiWindow.update()
    else:
        filearray4 = [] #Create blank array
        def path_leaf(path): #Splits path names into tails and heads
            head, tail = ntpath.split(path)
            return tail or ntpath.basename(head)
        for i in range(0, len(filearray3)): #For each element in filearray3
            fileAdd = filearray3[i] #fileAdd is current element
            with open(fileAdd, "rb") as fileToAdd: #Open current file
                filecontents = fileToAdd.read() #Read it
                fileToAdd.close() #Close it
            b64string = base64.b64encode(filecontents) #Create base64 string (allows uniformity)
            cipher = AES.new(gcmkey, AES.MODE_CBC, gcmiv) #New cipher object
            data = b64string #Switch names
            length = 16 - (len(data) % 16) #Create padding length
            data += bytes([length]) * length #Add the padding
            ciphertext = cipher.encrypt(data) #Encrypt data
            newName = path_leaf(fileAdd) #New file name without the path
            with open(newName, "wb") as newFile: #Open it
                newFile.write(ciphertext) #Write new text
                newFile.close() #Close it
            filearray4.append(newName) #Add the name to the new array
        try:
            for i in range(0, len(filearray4)): #For each element in this new array
                z.write(filearray4[i]) #Add it into the archive
            GUI.createLabel(guiWindow, "Successfully modified\nPlease close archive and\nreopen.", "green", "#08198a", 360, 350) #Success label
            guiWindow.update()
            filearray4 = [] #Empty the array
            for i in range(0, len(filearray2)): #For each element in filearray2
                if os.path.exists(filearray2[i]): #If the element is a path
                    os.remove(filearray2[i]) #Remove it
                else: #Or if it doesn't exist
                    pass #Skip it
        except:
            GUI.createLabel(guiWindow, "Failed to modify.", "#fa1a0a", "#08198a", 360, 350)
            filearray4 = [] #Empty the array
def interpretList(listWindowObj): #Subfunction
    userList = listWindowObj.getEntry() #Get list of files to remove
    global removalList
    removalList = userList.split(',') #Split the array
    removalList = list(set(removalList))
    listWindowObj.exitWindow() #Destroy GUI window
def IssueRemove(removalName, zipPass): #Subfunction
    try:
        if len(removalList) < 1: #If list is empty
            listWindowObj.createLabel(listWindow, "0 files to remove.", "#00ffff", "#08198a", 350, 350) #Tell the user
            listWindow.update()
        else:
            try: #If it is populated...
                delete_from_zip_file(removalName, file_names=removalList, password=zipPass) #Remove all files
                GUI.createLabel(guiWindow, "Successfully removed!", "green", "#08198a", 360, 350)
                guiWindow.update()
                archiveContents = [] #Clear the array
            except Exception as e:
                GUI.createLabel(guiWindow, "Failed to remove.", "#fa1a0a", "#08198a", 360, 350)
                print(repr(e))
                guiWindow.update()
                archiveContents = [] #And clear the array
    except Exception as e:
        print(repr(e))
        GUI.createLabel(guiWindow, "Failed to remove. List of files to\nremove is likely\nempty.", "#fa1a0a", "#08198a", 360, 350)
        guiWindow.update()
        return 0
def findFiles(g): #Subfunction
    global listWindow
    listWindow = Tk() #New Window and their specifications
    global listWindowObj
    listWindowObj = windowGen(listWindow, "Select for removal", "500x500", "#08198a")
    global archiveContents #Was a lot more efficient to use global here rather than pass it to almost every function anyway
    archiveContents = g.namelist() #Get archiveContents
    listWindowObj.createLabel(listWindow, archiveContents, "#fa1a0a", "#08198a", 0, 0)
    listWindowObj.createLabel(listWindow, "Please select files carefully. Your response should be like:\n 'file1,file2,file3'. Any incorrect files will be ignored and result in failure.\n THIS IS NOT REVERSIBLE.", "#fa1a0a", "#08198a", 10, 60)
    listWindowObj.createEntry(listWindow, 0, 200, pw="No") #Entry box for user to enter the removal list
    listWindowObj.createButton(listWindow, "Remove", 1, 5, "white", "#fa1a0a", "interpretList", 0, 119, listWindowObj, None, None, None) #Submit button
def removeFromArchive(): #Control Panel button
    def removal(g, removalName, zipPass): #Subfunction
        if len(zipPass) < 1:
            GUI.createLabel(guiWindow, "Failed to continue.", "#fa1a0a", "#08198a", 360, 350)
            guiWindow.update()
            return None
        else:
            try:
                filesInArray = g.namelist()
                if len(filesInArray) < 1:
                    GUI.createLabel(guiWindow, "Archive empty.", "#fa1a0a", "#08198a", 360, 350)
                    guiWindow.update()
                    return 0
                else:
                    pass
                removalWindow = Tk() #New window and it's specifications
                removalWindowObj = windowGen(removalWindow, "Remove files", "200x200", "#08198a")
                removalWindowObj.createButton(removalWindow, "Select files", 1, 10, "white", "orange", "findFiles", 10, 10, g, None, None, None) #Select files button
                removalWindowObj.createButton(removalWindow, "Remove files", 1, 10, "white", "#fa1a0a", "IssueRemove", 10, 50, removalName, zipPass, None, None)
            except Exception as er:
                GUI.createLabel(guiWindow, "Failed to continue.", "#fa1a0a", "#08198a", 360, 350)
                guiWindow.update()
                print(repr(er))
                return None
    refreshArrays() #Refresh all arrays
    currentDir = os.getcwd() #Save current directory
    removalName = askopenfilename(initialdir=currentDir, title="Import a file", filetypes=(("ZIP archive", "*.zip"),)) #File dialog for user
    def getPasswordZip(passwordZip2, passwordObj2):
        zipPass = passwordObj2.getEntry()
        if len(zipPass) < 1:
            passwordObj2.createLabel(passwordZip2, "Empty password", "#fa1a0a", "#08198a", 0, 200)
        else:
            passwordObj2.exitWindow()
            g = zipfile.ZipFile(removalName, 'a') #Zip object
            zipPass = bytes(zipPass, encoding='utf-8')
            g.setpassword(zipPass) #Set password
            removal(g, removalName, zipPass) #Call removal process
    try:
        filearray.remove(()) #Remove blank entries
    except ValueError:
        pass #Or not if there are not
    try:
        passwordZip2 = Tk() #Initiate window
        passwordObj2 = windowGen(passwordZip2, "Password for ZIP file", "250x250", "#08198a")
        passwordObj2.createEntry(passwordZip2, 0, 30, pw="Yes")
        passButton = Button(passwordZip2, text="Continue", height=1, width=5, fg="white", bg="#fa1a0a", command=lambda: getPasswordZip(passwordZip2, passwordObj2))
        passButton.place(x=0, y=60)
    except RuntimeError:
        GUI.createLabel(guiWindow, "Failed to remove.", "#fa1a0a", "#08198a", 360, 350)
        guiWindow.update()
        filearray.pop(0) #And clear the array
def renameFile(): #Subfunction
    newname = renameWindowObj.getEntry() #Get their rename title
    try:
        os.rename(renameName, newname) #Rename their archive
        GUI.createLabel(guiWindow, "Successfully renamed!", "green", "#08198a", 360, 350)
        renameWindowObj.exitWindow() #Destroy GUI window
    except:
        GUI.createLabel(guiWindow, "Failed to rename", "#fa1a0a", "#08198a", 360, 350) #Failure window
        return None
def renameArchive():
    refreshArrays() #Refresh all arrays
    def renameHandler(): #Subfunction
        renameWindowObj.createLabel(renameWindow, "Please enter new name", "green", "#08198a", 0, 0) #New label
        renameWindowObj.createEntry(renameWindow, 10, 60, pw="No") #Add entry box
        renameWindowObj.createButton(renameWindow, "Rename", 1, 5, "white", "#fa1a0a", "renameFile", 10, 110, None, None, None, None) #Place submit button
    currentDir = os.getcwd() #Save current directory
    global renameName
    renameName = askopenfilename(initialdir=currentDir, title="Import a file",
                                  filetypes=(("ZIP archive", "*.zip"),)) #File dialog for user
    try:
        renameWindow = Tk() #New global window
        global renameWindowObj
        renameWindowObj = windowGen(renameWindow, "Rename archive", "300x300", "#08198a")
        renameHandler() #Call rename handle
    except RuntimeError:
        GUI.createLabel(guiWindow, "Failed to rename", "#fa1a0a", "#08198a", 360, 350) #Failure window
        filearray.pop(0) #Clear array
        renameWindowObj.exitWindow() #Destroy GUI window
        return None
def closeArchive():
    refreshArrays() #Refresh all arrays
    chooseWindow.exitWindow() #Destroy GUI window
    z = None #Clear Z object
    GUI.createLabel(guiWindow, "Archive closed.", "green", "#08198a", 360, 350) #Failure window
################# END OF OPTION 2 CONTROL PANEL ####################################################
################# OPTION 3 CONTROL PANEL ###########################################################
def displayArchive():
    refreshArrays()
    def displayExec(zipPass):
        try:
            z = zipfile.ZipFile(filearray[0], 'a') #Set zipfile object
            zipPass = bytes(zipPass, encoding='utf-8')
            z.setpassword(zipPass) #Set password
            filesInArray = z.namelist()
            testfile = filesInArray[0]
            z.extract(testfile, pwd=zipPass)
            os.remove(testfile)
        except Exception as e:
            GUI.createLabel(guiWindow, "Exception occurred:\nIncorrect password or\nproblem with archive.", "#fa1a0a", "white", 360, 330)
            print(repr(e))
            return None #Return to mainGUI
        contentsArray = z.namelist() #Get contents of the archive
        contentsWindow = Tk() #New window and it's specifications
        contentsWindowObj = windowGen(contentsWindow, "Display Archive", "700x400", "#08198a")
        overlayHead = "Files:" + 35*" " + "Permissions:" #Overlay with padding
        contentsWindowObj.createLabel(contentsWindow, overlayHead, "#ffffff", "#08198a", 0, 0) #Create a label with it
        contentsWindowObj.createButton(contentsWindow, "Close", 1, 5, "white", "#fa1a0a", "contentsWindowObj.exitWindow", 550, 300, None, None, None, None) #Button to destroy window
        if len(contentsArray) > 10: #If the content is too big
            contentsWindowObj.createLabel(contentsWindow, "Archive too big to display.\n We dumped the contents\n to a local log file.\n.", "#e80ed2", "#08198a", 0, 200)
            randomNameLog = "log_contents_" + str(random.randint(0, 99999))
            with open(randomNameLog, "w") as logcontents:
                logcontents.write(str(contentsArray))
                logcontents.close()
        else:
            coord = 20 #Set starting Y coordinate
            for i in range(0, len(contentsArray)): #For each element
                status = os.stat(arcDisplay) #Display permissions
                status2 = oct(status.st_mode)[-3:] #Convert to readable number
                fileName1 = contentsArray[i] #Set current element
                if len(fileName1) > 25: #If name is too long
                    fileName1 = fileName1[15:] + "..." #Cut it off
                else:
                    pass #Or skip
                filler = " " * (45 - len(fileName1)) #Padding
                fullLine = str(fileName1) + filler + str(status2) #Fit padding between 2 texts
                contentsWindowObj.createLabel(contentsWindow, fullLine, "#e80ed2", "#08198a", 0, coord) #Create label
                coord += 15 #Increment Y coordinate
            contentsWindow.update() #Update GUI window
    currentDir = os.getcwd() #Save current directory
    arcDisplay = askopenfilename(initialdir=currentDir, title="Import a file", filetypes = (("ZIP archive","*.zip"),)) #File dialog for user
    try:
        testerfile = arcDisplay[0]
    except Exception:
        return 0
    filearray.append(arcDisplay)
    def getPasswordZip(passwordZip2, passwordObj2):
        zipPass = passwordObj2.getEntry()
        if len(zipPass) < 1:
            passwordObj2.createLabel(passwordZip2, "Empty password", "#fa1a0a", "#08198a", 0, 200)
        else:
            passwordObj2.exitWindow()
            displayExec(zipPass)
    passwordZip2 = Tk() #Initiate window
    passwordObj2 = windowGen(passwordZip2, "Password for ZIP file", "250x250", "#08198a")
    passwordObj2.createEntry(passwordZip2, 0, 30, pw="Yes")
    passButton = Button(passwordZip2, text="Continue", height=1, width=5, fg="white", bg="#fa1a0a", command=lambda: getPasswordZip(passwordZip2, passwordObj2))
    passButton.place(x=0, y=60)
################# END OF OPTION 3 CONTROL PANEL ####################################################
################# OPTION 5 CONTROL PANEL ###########################################################
def deleteArchive():
    refreshArrays() #Refresh all arrays
    def removeArchive(arcDisplay): #Subfunction
        try:
            os.remove(arcDisplay) #Remove specified file
            GUI.createLabel(guiWindow, "Successfully removed file", "green", "#08198a", 360, 350) #Tell the user
        except Exception: #If it failed
            GUI.createLabel(guiWindow, "Cannot remove file.", "#fa1a0a", "#08198a", 360, 350) #Tell the user
    try:
        currentDir = os.getcwd() #Save current directory
        arcDisplay = askopenfilename(initialdir=currentDir, title="Import a file", filetypes=(("ZIP archive", "*.zip"),)) #File dialog for user
        removeArchive(arcDisplay) #Call removal handler
    except:
        GUI.createLabel(guiWindow, "Exception occurred", "#fa1a0a", "#08198a", 360, 350)
        return None #Send the user back to the main GUI window
################# END OF OPTION 5 CONTROL PANEL ####################################################
################# OPTION 4 CONTROL PANEL ####################################################
def extractArchive():
    refreshArrays() #Refresh all arrays
    def extraction(j, zipPass): #Subfunction
        extractcontents = j.namelist() #Get archive contents
        j.extractall() #Extract the entire file
        gcmkey = user.getKey()
        gcmiv = user.getIV()
        for i in range(0, len(extractcontents)): #For each file
            encryptedfile = extractcontents[i] #Set element
            with open(encryptedfile, "rb") as encryptfile: #Open the file
                encryptedcontents = encryptfile.read() #Read it
                encryptfile.close() #Close
            cipher2 = AES.new(gcmkey, AES.MODE_CBC, gcmiv) #New cipher object
            plaintext = cipher2.decrypt(encryptedcontents) #plaintext = decrypted file contents
            data = plaintext[:-plaintext[-1]] #Remove padding
            plaintext = data.decode('utf-8') #Decode it
            plaintext = base64.b64decode(plaintext) #Decode it again
            with open(encryptedfile, "wb") as decryptfile: #Open new file
                decryptfile.write(plaintext) #Write original data
                decryptfile.close() #Close it
        GUI.createLabel(guiWindow, "Successfully extracted", "green", "#08198a", 360, 350) #Tell the user
    def getPasswordZip(passwordZip2, passwordObj2, arcDisplay2):
        zipPass = passwordObj2.getEntry()
        if len(zipPass) < 1:
            passwordObj2.createLabel(passwordZip2, "Empty password", "#fa1a0a", "#08198a", 0, 200)
        else:
            try:
                zipPass = bytes(zipPass, encoding='utf-8')
                j = zipfile.ZipFile(arcDisplay2, 'a') #ZIP object
                j.setpassword(zipPass) #Set password
                filesInArray = j.namelist()
                testfile = filesInArray[0]
                j.extract(testfile, pwd=zipPass)
                passwordObj2.exitWindow()
                extraction(j, zipPass)
            except Exception:
                GUI.createLabel(guiWindow, "Exception occurred:\nIncorrect password or\nproblem with archive.", "#fa1a0a", "#08198a", 360, 330)
                passwordObj2.exitWindow()
                return None
    currentDir = os.getcwd() #Save current directory
    arcDisplay2 = askopenfilename(initialdir=currentDir, title="Import a file", filetypes = (("ZIP archive","*.zip"),)) #File dialog for user
    if len(arcDisplay2) < 1:
        GUI.createLabel(guiWindow, "Exception occurred", "#fa1a0a", "#08198a", 360, 350)
        return None
    else:
        passwordZip2 = Tk() #Initiate window
        passwordObj2 = windowGen(passwordZip2, "Password for ZIP file", "250x250", "#08198a")
        passwordObj2.createEntry(passwordZip2, 0, 30, pw="Yes")
        passButton = Button(passwordZip2, text="Continue", height=1, width=5, fg="white", bg="#fa1a0a", command=lambda: getPasswordZip(passwordZip2, passwordObj2, arcDisplay2))
        passButton.place(x=0, y=60)
################# END OF OPTION 4 CONTROL PANEL ####################################################
################ CONTROL PANEL ##################################
def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=requests.get("https://icanhazip.com").content.decode('utf-8').rstrip()
        #GET request to icanhazip.com, returns the page content without the b'' and \n in it.
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return info
    except Exception as e:
        logging.exception(e)
sysinfo = "\n"
for item, val in getSystemInfo().items():
    sysinfo += item + ": " + val + "\n"
def diagnostics():
    def APICheck():
        di = requests.get("https://192.168.1.120/SolitaireSec/diagnostics.php")
        if di.content == b"Passed":
            GUI.createLabel(guiWindow, "API status: Passed", "#f0f0f0", "#a6a4a4", 500, 100)
        elif di.content == b"Failed":
            GUI.createLabel(guiWindow, "API status: Failed", "#fa1a0a", "#a6a4a4", 500, 100)
        else:
            GUI.createLabel(guiWindow, "API status: Exception", "#fa1a0a", "#a6a4a4", 500, 100)
    def internetCheck():
        try:
            urllib.request.urlopen('http://216.58.204.46', timeout=1)
            return True
        except urllib.error.URLError:
            return False
        except Exception as diagnostic:
            print(repr(diagnostic))
            return 0
    try:
        internet1 = internetCheck()
        if internet1:
            GUI.createLabel(guiWindow, "Internet status: Passed", "#f0f0f0", "#a6a4a4", 500, 130)
        else:
            GUI.createLabel(guiWindow, "Internet status: Failed", "#fa1a0a", "#a6a4a4", 500, 130)
        if sysinfo:
            GUI.createLabel(guiWindow, "System Information:\n %s" % str(sysinfo), "#f0f0f0", "#a6a4a4", 500, 160)
        else:
            GUI.createLabel(guiWindow, "System Information: Failed", "#fa1a0a", "#a6a4a4", 500, 160)
        APICheck()
    except Exception as exc:
        print(repr(exc))
def mainGUI():
    try:
        LoginPanel.exitWindow()
    except:
        pass
    global guiWindow #Leaving this here and leaving global GUI as every function uses them, so it suits it's purpose.
    guiWindow = Tk() #Control Panel and it's specifications
    guiWindow.protocol("WM_DELETE_WINDOW",lambda: logout(guiWindow))
    global GUI
    GUI = windowGen(guiWindow, "Solitaire Security", "990x400", "#08198a")
    GUI.createLabel(guiWindow, "Control Panel", "#ffffff", "#08198a", 350 , 10)
    GUI.createButton(guiWindow, "Modify existing archive", 1, 20, "white", "red", "selectArchive", 20, 60, None, None, None, None)
    GUI.createButton(guiWindow, "Show contents of an archive", 1, 25, "white", "red", "displayArchive", 20, 110, None, None, None, None)
    GUI.createButton(guiWindow, "Extract an archive", 1, 15, "white", "red", "extractArchive", 20, 210, None, None, None, None)
    GUI.createButton(guiWindow, "Delete archive", 1, 15, "white", "red", "deleteArchive", 20, 160, None, None, None, None)
    GUI.createButton(guiWindow, "Log out", 1, 15, "white", "red", "logout", 20, 260, None, None, None, None)
    GUI.createButton(guiWindow, "Create new archive", 1, 15, "white", "red", "newArchive", 20, 10, None, None, None, None)
    GUI.createLabel(guiWindow, "Currently logged in as:\n " + uforzip[0], "#9dfcee", "#a6a4a4", 500, 50)
    diagnostics()
    guiWindow.update()
################# END OF CONTROL PANEL ####################################################
################# LOGIN WINDOW ####################################################
class ImageLabel(Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = []

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)
window1 = Tk() #Login window and it's specifications
pyramid = ImageLabel(window1)
pyramid.place(x=650,y=10)
pyramid.load('bg3.gif')
window1.attributes("-fullscreen", False)
LoginPanel = windowGen(window1, "Solitaire Security", "1366x432", "#08198a")
LoginPanel.createLabel(window1, "Developed and maintained by The Enigma Project", "#e8be05", "#08198a", 200, 380)
LoginPanel.createLabel(window1, "Animation credit: https://gifer.com/en/DgfB", "#e0dbda", "#08198a", 965, 385)
LoginPanel.createLabel(window1, "Solitaire Security\nLogin:", "#ffffff", "#08198a", 100, 10)
LoginPanel.createLabel(window1, "Please enter a username:", "#ffffff", "#08198a", 100, 85)
userHandler = Entry(window1)
userHandler.place(x=100,y=130)
LoginPanel.createLabel(window1, "Please enter a password:", "#ffffff", "#08198a", 100, 165)
passHandler = Entry(window1, show="*")
passHandler.place(x=100,y=200)
LoginPanel.createLabel(window1, "Solitaire Security\nRegister:", "#ffffff", "#08198a", 400, 10)
LoginPanel.createLabel(window1, "Please enter a username:", "#ffffff", "#08198a", 400, 85)
usernameregHandler = Entry(window1)
usernameregHandler.place(x=400,y=130)
LoginPanel.createLabel(window1, "Please enter a password:", "#ffffff", "#08198a", 400, 165)
passregHandler = Entry(window1, show="*")
passregHandler.place(x=400,y=200)
def callback(url, LoginPanel):
    LoginPanel.createLabel(window1, "Opening Chrome...", "#e80ed2", "#08198a", 400, 330)
    webbrowser.get(using='google-chrome').open(url)
link1 = Button(window1, text="Change password", fg="white", bg="purple", command=lambda: callback("https://192.168.1.120/SolitaireSec/chngPw.php", LoginPanel))
link1.place(x=100,y=285)
def getPostData(usernameregHandler, passregHandler): #User registration
    userPost = usernameregHandler.get() #Get username
    uforzip.append(userPost) #Add to array
    passPost = passregHandler.get() #Get password
    if len(userPost) == 0 or len(passPost) == 0: #If they are empty
        LoginPanel.createLabel(window1, "You cannot leave these fields empty!", "#fa1a0a", "#08198a", 400, 350)
        window1.update() #Update GUI window
    else:
        data1={"Username": userPost, "Password": passPost} #Create JSON object
        url = "https://192.168.1.120/SolitaireSec/serverReg.php/" #URL
        headers={} #Blank headers
        r = requests.post(url, data=data1, headers=headers, verify=False) #set this to True when you set up
        #a valid SSL, this part relies on SSL/TLS encryption.
        if r.content == b'Success!': #If server says it is okay
            pyramid.unload()
            LoginPanel.exitWindow()
            global user
            user = userInfo(userPost, passPost)
            mainGUI() #Progress further
        else:
            response1 = r.content #if not, echo the response
            response1 = response1.decode('utf-8') #Decode it
            LoginPanel.createLabel(window1, response1, "#fa1a0a", "#08198a", 400, 350)
            window1.update() #update GUI window
def getLoginData(userhandler, passhandler): #User login
    userLogin = userhandler.get() #Get username
    uforzip.append(userLogin) #Add it to the array
    passLogin = passhandler.get() #Get password
    if len(userLogin) == 0 or len(passLogin) == 0: #If they are empty
        LoginPanel.createLabel(window1, "You cannot leave these fields empty!", "#fa1a0a", "#08198a", 100, 350) #Tell the user
        window1.update() #Update GUI window
    else:
        data2={"Username": userLogin, "Password": passLogin} #Create JSON object
        url = "https://192.168.1.120/SolitaireSec/serverLogin.php/" #URL
        headers={} #Blank headers
        r = requests.post(url, data=data2, headers=headers, verify=False) #set this to True when you set up
        #a valid SSL, this part relies on SSL/TLS encryption.
        if r.content == b'200 OK': #If server gives the green light
            pyramid.unload()
            LoginPanel.exitWindow() #Destroy login window
            global user
            user = userInfo(userLogin, passLogin)
            mainGUI() #Progress further
        else:
            response1 = r.content #Or if not, echo the response
            response1 = response1.decode('utf-8') #Decode it
            LoginPanel.createLabel(window1, response1, "#fa1a0a", "#08198a", 100, 350)
            window1.update() #Update window
button3 = Button(
                text="Submit",
                width=5,
                height=1,
                bg="red",
                fg="white",
                command=lambda: getPostData(usernameregHandler, passregHandler)
                )
button2 = Button(
                text="Submit",
                width=5,
                height=1,
                bg="red",
                fg="white",
                command=lambda: getLoginData(userHandler, passHandler)
                )
button3.place(x=400, y=235)
button2.place(x=100,y=235)
window1.protocol("WM_DELETE_WINDOW",lambda: logout(window1))
window1.mainloop()
################# END OF LOGIN WINDOW ####################################################
