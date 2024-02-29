from PIL import Image
import glob
import os
list_images = [i for i in glob.glob("*.jpg")]
if not "s8" in os.listdir():#it creates ltl file if it is not present
    os.mkdir("s8")
for i in list_images:
    img = Image.open(i)
    img = img.resize((500,500))
    img.save("s8\\" + i[:-4] + "_ltl.jpg")

print("Done")
os.startfile("s8")
#Just change the file name s1 to s2 or anything you would like to do.
