
from tkinter import *
from PIL import  ImageTk, Image

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]                       #after every 100 character another line will be printed
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text



root = Tk()
root.title("CodeWithHarry News - Aapka Apna Akhabaar")
root.geometry("1000x1000")

texts = []
photos = []
for i in range(0, 3):
    with open(f"{i+1}.txt") as f:
        text = f.read()                                 #this for loop is for reading the file
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.png")
    #TODO: Resize these images
    image = image.resize((225, 265), Image.ANTIALIAS)     #this line of code is used for resixing the image and ANTIALIAS is used for removing blur in the image
    photos.append(ImageTk.PhotoImage(image))

f0 = Frame(root, width=800, height=70)
Label(f0, text="Code With Harry News", font="lucida 33 bold").pack()   #in this tittle is given and as well as date is also provided
Label(f0, text="January 19, 2050", font="lucida 13 bold").pack()
f0.pack()


f1 = Frame(root, width=900, height=200, pady=14)
Label(f1, text=texts[0], padx=22, pady=22).pack(side="left")       #first image is placed
Label(f1, image=photos[0], anchor="e").pack()
f1.pack(anchor="w")


f2 = Frame(root, width=900, height=200, pady=14, padx=22)
Label(f2, text=texts[1], padx=22, pady=22).pack(side="right")      #second image is placed
Label(f2, image=photos[1], anchor="e", padx=22).pack()
f2.pack(anchor="w")


f3 = Frame(root, width=900, height=200, pady=34)
Label(f3, text=texts[2], padx=22, pady=22).pack(side="left")         #third image is placed
Label(f3, image=photos[2], anchor="e").pack()
f3.pack(anchor="w")

root.mainloop()

#note: here text and image files are not present
