import os

from PIL import Image
import numpy as np

input_dir = "/Users/Josh/Documents/celeb_machine_learning_matching/data/output_images/"

directories = os.listdir(input_dir)

index = 0
index2 = 0

for folder in directories:
	if folder == '.DS_Store':
		pass

	else:
		print folder

		folder2 = os.listdir(input_dir + '/' + folder)
		index += 1

		for image in folder2:
			index2 += 1
			im = Image.open(input_dir+"/"+folder+"/"+image)
			im = (np.array(im))

			try:
				r = im[:,:,0]
				g = im[:,:,1]
				b = im[:,:,2]

				if index2 != 1:
					new_array = np.array([[r] + [g] + [b]], np.uint8)
					out = np.append(out, new_array, 0)

				elif index2 == 1:
					out = np.array([[r] + [g] + [b]], np.uint8)

				if index == 1 and index2 == 1:
					index_array = np.array([[index]])

				else:
					new_index_array = np.array([[index]], np.int8)
					index_array = np.append(index_array, new_index_array, 0)

			except Exception as e:
				print e
				print image

print index
print index2
np.save('X.npy', out)
np.save('Y.npy', index_array)
