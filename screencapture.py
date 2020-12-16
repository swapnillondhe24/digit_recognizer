from PIL import Image
import pyscreenshot as ImageGrab
import time

if __name__ == "__main__":
	for i in range(0,10):
		images_folder = "orig_images/"+str(i)+"/"
		number = images_folder.split("/")[1]
		for i in range (45,50):
			print("Draw "+ number +" within 5 seconds")
			time.sleep(5)
			im = ImageGrab.grab(bbox=(80, 160, 300, 380)) # X1,Y1,X2,Y2
			print ("saved....",i)
			im.save(images_folder+str(i)+'.png')
			print ("clear screen now and redraw")
