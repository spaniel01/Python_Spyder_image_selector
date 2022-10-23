# Description
Small program to make the task of selecting photos, involving a lot of clicking if done manually, easier. 

Must be opened in **Spyder** to work.

Basic features:
- Prompts for setting photo location (working directory, wd)
- Checks whether program has been run before:
  - If not, (only) image files are "selected" from wd
  - If so and some photos are still pending evaluation, these are loaded. If all photos in folder have already been reviewed before, user may choose to restart process or exit
- Displays image in Spyder via matplotlib
- Prompts user to decide whether to keep or discard an image. Users may also view the last previously kept or discarded image and revise their decision
- If the user either chooses to exit or has reviewed all the photos:
  - The photos selected for keeping are copied into a folder called "keep", which - if it does not yet exist - is created
  - If the user has chosen to exit without reviewing all photos, the remaining photos are written to file, to be loaded again if the program is run again. Otherwise, the file will signal the program, upon starting again in the same directory, that the images in the folder have already been reviewed  
