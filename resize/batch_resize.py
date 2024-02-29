from PIL import Image
import glob
import os
list_images = [i for i in glob.glob("*.jpg")]
if not "ltl" in os.listdir():#it creates ltl file if it is not present
    os.mkdir("ltl")
for i in list_images:
    img = Image.open(i)
    img = img.resize((224,224), Image.ANTIALIAS)
    img.save("ltl\\" + i[:-4] + "_ltl.jpg")

print("Done")
os.startfile("ltl")
