import os

from PIL import Image
import numpy as np

#Directory containing images you wish to convert
input_dir = "/Users/14/Documents/deep-learning-project/data/output_images/"

directories = os.listdir(input_dir)

index = 0
index2 = 0

index_test = 0
index2_test = 0

for folder in directories[0:500]:
	#Ignoring .DS_Store dir
	if folder == '.DS_Store':
		pass

	else:
		print folder

		folder2 = os.listdir(input_dir + '/' + folder)
		index += 1

		len_images = len(folder2)
		len_images80 = len_images * 80 #Getting index of image on the 80% mark
		len_images20 = len_images * 20 #Getting index of image on the 20% mark

		#Iterating through first 80% of images in folder for train data
		for image in folder2[0:int(len_images80)]:
			if image == ".DS_Store":
				pass

			else:
				index2 += 1

				im = Image.open(input_dir+"/"+folder+"/"+image) #Opening image
				im = (np.array(im)) #Converting to numpy array

				try:
					r = im[:,:,0] #Slicing to get R data
					g = im[:,:,1] #Slicing to get G data
					b = im[:,:,2] #Slicing to get B data

					if index2 != 1:
						new_array = np.array([[r] + [g] + [b]], np.uint8) #Creating array with shape (3, 100, 100)
						out = np.append(out, new_array, 0) #Adding new image to array shape of (x, 3, 100, 100) where x is image number

					elif index2 == 1:
						out = np.array([[r] + [g] + [b]], np.uint8) #Creating array with shape (3, 100, 100)

					if index == 1 and index2 == 1:
						index_array = np.array([[index]])

					else:
						new_index_array = np.array([[index]], np.int8)
						index_array = np.append(index_array, new_index_array, 0)

				except Exception as e:
					print e
					print "Removing image" + image
					os.remove(input_dir+"/"+folder+"/"+image)

		#Iterating throught last 20% of image in folder for test data
		for image in folder2[len_images-int(len_images20):len_images]:
			if image == ".DS_Store":
				pass

			else:
				index2_test += 1

				im = Image.open(input_dir+"/"+folder+"/"+image) #Opening image
				im = (np.array(im)) #Converting to numpy array

				try:
					r = im[:,:,0] #Slicing to get R data
					g = im[:,:,1] #Slicing to get G data
					b = im[:,:,2] #Slicing to get B data

					if index2_test != 1:
						new_array_test = np.array([[r] + [g] + [b]], np.uint8) #Creating array with shape (3, 100, 100)
						out_test = np.append(out_test, new_array_test, 0) #Adding new image to array shape of (x, 3, 100, 100) where x is image number

					elif index2_test == 1:
						out_test = np.array([[r] + [g] + [b]], np.uint8) #Creating array with shape (3, 100, 100)

					if index == 1 and index2_test == 1:
						index_array_test = np.array([[index]])

					else:
						new_index_array_test = np.array([[index]], np.int8)
						index_array_test = np.append(index_array_test, new_index_array_test, 0)

				except Exception as e:
					print e
					print "Removing image" + image
					os.remove(input_dir+"/"+folder+"/"+image)

print index
print index2

print index2_test

np.save('X_train.npy', out) #Saving train image arrays
np.save('Y_train.npy', index_array) #Saving train labels

np.save('X_test.npy', out_test) #Saving test image arrays
np.save('Y_test.npy', index_array_test) #Saving test labels

