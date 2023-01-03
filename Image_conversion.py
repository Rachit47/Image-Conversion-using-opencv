import cv2
import easygui
import matplotlib.pyplot as plt
import os
import tkinter as tk # provides buttons, labels and text boxes used in GUI application
from tkinter import *

root = tk.Tk() # Tkinter window that are containers having other GUI elements
root.geometry('720x720') # setting window size to 720 by 720
root.title('Select image to convert!')
root.configure(background = 'medium turquoise')
label = Label(root, background = "black", font = ("Copperplate Gothic Bold",30,"bold"))
def u():
	Imagepath =  easygui.fileopenbox() # file-box opens up to select the image for conversion
	c(Imagepath)

def c(Imagepath):
	originalimage = cv2.imread(Imagepath)
	originalimage = cv2.cvtColor(originalimage, cv2.COLOR_BGR2RGB)
	if originalimage is None:
		print("Image not found/selected !!")
		sys.exit()

	Resize_1 = cv2.resize(originalimage, (920 , 500))

	greyScaleImage = cv2.cvtColor(originalimage , cv2.COLOR_BGR2GRAY)
	Resize_2 = cv2.resize(greyScaleImage, (920 , 500))

	smoothGrayScale = cv2.medianBlur(greyScaleImage , 5)
	Resize_3 = cv2.resize(smoothGrayScale, (920 , 500))

	getedge = cv2.adaptiveThreshold(smoothGrayScale , 255 , cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY , 9 , 9)
	Resize_4 = cv2.resize(getedge , (920 , 500))

	colorImage = cv2.bilateralFilter(originalimage,9, 360, 360)
	Resize_5 = cv2.resize(colorImage , (920 , 500))

	cartoonImage = cv2.bitwise_and(colorImage , colorImage , mask = getedge)
	Resize_6 = cv2.resize(cartoonImage, (920 , 500))

	images = [Resize_1, Resize_2, Resize_3, Resize_4, Resize_5, Resize_6]

	fig , axes = plt.subplots( 3, 2 , figsize = (16,8), gridspec_kw = dict(
		hspace = 0.2 , wspace = 0.2))

	for i, ax in enumerate(axes.flat):
		ax.imshow(images[i] , cmap = 'gray')

	save1 = Button(root , text = "Save Cartoon Image" , command = lambda : save(Resize_6, Imagepath), padx = 28 , pady = 4)
	save1.configure( background = "teal" , foreground = "yellow" , font = ('arial', 22, "bold"))
	save1.pack(side = TOP, pady = 50)

	plt.show()
def save(Resized_6, Imagepath):
	Rename = "Converted Image !!!"
	path_1 = os.path.dirname(Imagepath)
	extension = os.path.splitext(Imagepath)[1]
	path = os.path.join(path_1 , Rename + extension)
	cv2.imwrite( path, cv2.cvtColor(Resized_6 , cv2.COLOR_RGB2BGR))
	I = "The saved image: " + Rename + " stored at" + path
	tk.messagebox.showinfo(title = None , message = I)
a = Button(root, text = "Your image please !!", command = u, padx = 15, pady = 10)
a.configure(background = "DarkSlateGrey", foreground = "LightYellow", font = ("Copperplate Gothic Bold", 30 , "bold"))
a.pack(side = TOP , pady = 50)

root.mainloop()
