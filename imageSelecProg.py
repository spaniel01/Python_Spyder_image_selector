# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.image as img
import pickle
import os
import shutil
plt.rcParams['figure.dpi'] = 300

def showImage(image):
    testImage = img.imread(image)
# displaying the image
    plt.imshow(testImage)
    plt.axis('off')
    plt.pause(0.0001)

def createSelec():
    direcList = os.listdir()
    fileTypeList = [".jpg", ".jpeg", ".png"]
    selec = []
    for fileName in direcList:
        for fileType in fileTypeList:
            if fileName.endswith(fileType) :
                selec += [fileName]
    return selec

### Start procedure
# Set working directory where images are located
while True:
    try: 
        workingDirec = input("Please provide working directory! ")
        os.chdir(workingDirec)
        break
    except:
        print("Working directory invalid! Try again! ")
        pass

# If program has not run here, make list of photos to review; otherwise, if not yet reviewed, load list of photos; if reviewed completely, ask if to start again
if "photosToReview.pkl" not in os.listdir():
# Select images files only
    selec = createSelec()
    with open('photosToReview.pkl', 'wb') as file:
        pickle.dump(selec, file)
else:
    with open('photosToReview.pkl', 'rb') as file:
        selec = pickle.load(file)
        if selec[0] == "empty":
            userInput = input("Please note: You have already once reviewed the photos in this folder! If you want to repeat this process, please type 'repeat', otherwise type 'exit'! ")
            while userInput not in ["repeat", "exit"]:
                userInput = input("Please enter acceptable input! ")
            if userInput == "repeat":
                selec = createSelec()
                with open('photosToReview.pkl', 'wb') as file:
                    pickle.dump([selec], file)
            else:
                quit()

### Review images
# Choosing selected images
keep = []
discard = []
for image in selec:
# Showing the image
    showImage(image)
    userInput = input("Please evaluate with 'w' (keep) , 's' (discard) or 'a' (re-evaluate previous image) or 'exit'! ")
    while userInput not in ["w", "s", "a", "exit"]:
        userInput = input("Please enter acceptable input! ")
#Keep image
    if userInput == "exit":
        break
    elif userInput == "w":
        keep.append(image)
        print("To keep: " + image)
    # Discard image, i.e. name of image not added to keep list
    elif userInput == "s":
        discard.append(image)
        print("To discard: " + image)
# Option "a": review previous and then current image
    else:
        reviewImage = selec[selec.index(image)-1]
# Undo previous eval
        if len(keep) > 0 and reviewImage in keep:
            keep.remove(reviewImage)
        if len(discard) > 0 and reviewImage in discard:
            discard.remove(reviewImage)
# Show previous image and rate
        showImage(reviewImage)
        userInput = input("Please evaluate with 'w' (keep) or 's' (discard)! '")
        while userInput not in ["w", "s"]:
            userInput = input("Please enter acceptable input! ")
        if userInput == "w":
            keep.append(reviewImage)
            print("To keep: " + image)
        else:
            discard.append(reviewImage)
            print("To discard: " + image)
# Evaluate image that was not reviewed before option "a" was chosen 
        showImage(image)
        print(image)
        userInput = input("Please evaluate with 'w' (keep) or 's' (discard)! '")
        while userInput not in ["w", "s"]:
            userInput = input("Please enter acceptable input! ")
            if userInput == "w":
                keep.append(image)
                print("To keep: " + image)
            else:
                discard.append(image)
                print("To discard: " + image)


### Exit procedure
#If finished or users chooses to exit
if userInput == "exit":
    print("You've chosen to exit. Your progress will be saved and already selected photos copied to the 'keep' folder in this directory! See ya!")
else:
    print("You have finished reviewing all the photos in this folder! Your selected photos are available in the 'keep' folder in this directory! See ya!")

# Create keep folder if it does not yet exist
if "keep" not in os.listdir():
    os.mkdir("keep")
#Move selected images to folder
for file in keep:
    # construct full file path
    source = os.getcwd() + "\\"  + file
    destination = os.getcwd() + "\\" + "keep" + "\\"  + file
    # move file
    shutil.move(source, destination)
    print('Moved:', file)

if userInput == "exit":
# Store images to still be reviewed
    for i in discard:
        selec.remove(i)
    for i in keep:
        selec.remove(i)
else:
    selec = ["empty"]
with open('photosToReview.pkl', 'wb') as file:
    pickle.dump(selec, file)
