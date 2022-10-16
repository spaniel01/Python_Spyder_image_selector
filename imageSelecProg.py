# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.image as img
import os
import shutil
plt.rcParams['figure.dpi'] = 300

def showImage(image):
        testImage = img.imread(image)
        # displaying the image
        plt.imshow(testImage)
        plt.axis('off')
        plt.pause(0.0001)  

# Set working directory where images are located
while True:
    try: 
        workingDirec = input("Please provide working directory! ")
        os.chdir(workingDirec)
        break
    except:
        print("Working directory invalid! Try again! ")
        pass

# Select images files only
direcList = os.listdir()
fileTypeList = [".jpg", ".jpeg", ".png"]
selec = []
for fileName in direcList:
    for fileType in fileTypeList:
        if fileName.endswith(fileType) :
            selec += [fileName]

# Choosing selected images
print("Press 'w' for like, 's' for don't like and 'a' for reviewing the previous image again!")
keep = []
for image in selec:
# Showing the image
    showImage(image)
    userInput = input("Please evaluate! ")
    while userInput not in ["w", "s", "a"]:
        userInput = input("Please enter acceptable input! ")
#Keep image
    if userInput == "w":
        keep.append(image)
# Review previous image
    elif userInput == "a":
        reviewImage = selec[selec.index(image)-1]
        if reviewImage in keep:
            keep = keep.remove(reviewImage)
        showImage(reviewImage)
        userInput = input("Please evaluate with 'w' or 's'! ")
        while userInput not in ["w", "s"]:
            userInput = input("Please enter acceptable input! ")
        if userInput == "w":
            keep.append(reviewImage)
        else:
            pass
# Evaluate image that was not reviewed before option "a" was chosen 
        showImage(image)
        userInput = input("Please evaluate! ")
        while userInput not in ["w", "s", "a"]:
            userInput = input("Please enter acceptable input! ")
            if userInput == "w":
                keep.append(image)    
# Discard image, i.e. name of image not added to keep list            
    else:
        pass

# Create keep folder if it does not yet exist
if "keep" not in os.listdir():
    os.mkdir("keep")
# Moves selected images to folder
for file in keep:
    # construct full file path
    source = os.getcwd() + "\\"  + file
    destination = os.getcwd() + "\\" + "keep" + "\\"  + file
    # move file
    shutil.move(source, destination)
    print('Moved:', file)



