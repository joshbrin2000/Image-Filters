# import the necessary packages
import numpy as np
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image
from PIL import ImageTk
from PIL import ImageFilter
import cv2
from pykuwahara import kuwahara

def saveImage():
        global panelB
        global saveIm
        #print(panelB.image)
        saveIm.save("SavedImage.jpg")

def update():
        global panelA, panelB
        global imageOrig
        global imSwitch
        
        temp = panelA.image
        panelA.configure(image=panelB.image)
        panelA.image = panelB.image
        panelB.configure(image=temp)
        panelB.image = temp

        imageOrig = imSwitch

def addNoise():
        global panelA, panelB
        global imageOrig
        global filtLen
        #cv2.imshow('aa', imageOrig)
        row,col,ch = imageOrig.shape
        mean = 0
        var = 0.1
        sigma = var**0.1
        gauss = np.random.normal(mean,sigma,(row,col,ch))
        gauss = gauss.reshape(row,col,ch).astype('uint8')
        noisy = cv2.add(imageOrig, gauss)
        imageOrig = noisy
        #cv2.imshow('aa', imageOrig)
        #cv2.imshow('aa', noisy)
        noisyDisp = cv2.cvtColor(noisy, cv2.COLOR_BGR2RGB)
        #cv2.imshow('aa', noisyDisp)
        noisyDisp = Image.fromarray(noisyDisp)
        noisyDisp = ImageTk.PhotoImage(noisyDisp)
        panelA.configure(image=noisyDisp)
        panelA.image = noisyDisp

def triangleFilter():
        global panelA, panelB
        global imageOrig
        global filtLen
        global saveIm
        global imSwitch
        
        arr = np.arange(filtLen)
        kernelFlat = (filtLen + 1 - np.abs(arr - arr[::-1])) / 2
        kernel2D = np.outer(kernelFlat, kernelFlat)
        kernel2D /= kernel2D.sum()
        #print(kernel2d)
        
        triangle = cv2.filter2D(imageOrig, -1, kernel2D)
        imSwitch = triangle
        trianglePres = cv2.cvtColor(triangle, cv2.COLOR_BGR2RGB)
        trianglePresI = Image.fromarray(trianglePres)
        trianglePres = ImageTk.PhotoImage(trianglePresI)
        panelB.configure(image=trianglePres)
        panelB.image = trianglePres
        saveIm = trianglePresI


def gaussianFilter():
        global panelA, panelB
        global imageOrig
        global filtLen
        global sigma
        global en1
        global saveIm
        global imSwitch
        if (len(en1.get()) != 0):
                sigma = int(en1.get())
        gauss = cv2.GaussianBlur(imageOrig, (filtLen, filtLen), sigma, sigma)
        imSwitch = gauss
        gaussPres = cv2.cvtColor(gauss, cv2.COLOR_BGR2RGB)
        gaussPresI = Image.fromarray(gaussPres)
        gaussPres = ImageTk.PhotoImage(gaussPresI)
        panelB.configure(image=gaussPres)
        panelB.image = gaussPres
        saveIm = gaussPresI
        #print(type(saveIm))
        #cv2.imshow('aa', median)

def medianFilter():
        global panelA, panelB
        global imageOrig
        global filtLen
        global saveIm
        global imSwitch
        median = cv2.medianBlur(imageOrig, filtLen)
        imSwitch = median
        medianPres = cv2.cvtColor(median, cv2.COLOR_BGR2RGB)
        medianPresI = Image.fromarray(medianPres)
        medianPres = ImageTk.PhotoImage(medianPresI)
        panelB.configure(image=medianPres)
        panelB.image = medianPres
        saveIm = medianPresI
        #print(type(saveIm))
        #cv2.imshow('aa', median)

def kuwaharaFilter():
        global panelA, panelB
        global imageOrig
        global filtLen
        global saveIm
        global imSwitch
        kuw = kuwahara(imageOrig, method='mean', radius=filtLen)
        imSwitch = kuw
        kuwPres = cv2.cvtColor(kuw, cv2.COLOR_BGR2RGB)
        kuwPresI = Image.fromarray(kuwPres)
        kuwPres = ImageTk.PhotoImage(kuwPresI)
        panelB.configure(image=kuwPres)
        panelB.image = kuwPres
        saveIm = kuwPresI
        #print(type(saveIm))
        #cv2.imshow('aa', kuw)

def select_image():
	global panelA, panelB
	global en1
	global imageOrig
	global filtLen
	global sigma
	global saveIm
	global imSwitch
	sigma = 1
	path = filedialog.askopenfilename()
	if len(path) > 0:
		imageOrig = cv2.imread(path)
		filtLen = 5
		# OpenCV represents images in BGR order; however PIL represents
		# images in RGB order, so we need to swap the channels
		image = cv2.cvtColor(imageOrig, cv2.COLOR_BGR2RGB)
		# convert the images to PIL format...
		image = Image.fromarray(image)
		image = ImageTk.PhotoImage(image)
		
		if panelA is None or panelB is None:
			# the first panel will store our original image
			panelA = Label(image=image)
			panelA.image = image
			panelA.pack(side="left", padx=10, pady=10)
			# while the second panel will store the edge map
			panelB = Label(image=image)
			panelB.image = image
			panelB.pack(side="right", padx=10, pady=10)

			saveIm = imageOrig
			imSwitch = imageOrig
			
			btnSave = Button(root, text="Save Image", command=saveImage)
			btnSave.pack(side = "bottom", padx = "10", pady = "10")

			en1 = Entry(root, width = 5, background = 'white', textvariable = sigma)
			en1.pack(side="bottom")
			lbl = Label(root, text="Sigma for Gaussian Filter: ")
			lbl.pack(side="bottom", padx=(12, 10), pady=(0, 10))

			btnUp = Button(root, text="Update Source", command=update)
			btnUp.pack(side = "bottom", padx = "10", pady = "10")
			
			btn2 = Button(root, text="Add Noise", command=addNoise)
			btn2.pack(side="bottom", padx="10", pady="10")

			btn3 = Button(root, text="5x5 Triangle", command=triangleFilter)
			btn3.pack(side="bottom", padx="10", pady="10")

			btn4 = Button(root, text="5x5 Gaussian", command=gaussianFilter)
			btn4.pack(side="bottom", padx="10", pady="10")

			btn5 = Button(root, text="5x5 Median", command=medianFilter)
			btn5.pack(side="bottom", padx="10", pady="10")

			btn6 = Button(root, text="5x5 Kuwahara", command=kuwaharaFilter)
			btn6.pack(side="bottom", padx="10", pady="10")
		# otherwise, update the image panels
		else:
			# update the pannels
			sigma = en1.get()
			panelA.configure(image=image)
			panelB.configure(image=image)
			panelA.image = image
			panelB.image = image

root = tk.Tk("Image Filtering")
panelA = None
panelB = None
# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
btn1 = Button(root, text="Select an image", command=select_image)
btn1.pack(side="bottom", padx="10", pady="10")

root.mainloop()
