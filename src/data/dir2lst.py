
import sys
import os
print(sys.path)
sys.path.insert(0, '/home/ti/Downloads/insightface/src/common')
import face_image

input_dir = sys.argv[1]
pairs_filepath = "listik.lst"
dataset = face_image.get_dataset_common(input_dir, 2)

#for item in dataset:
#	print("%d\t%s\t%d" % (1, item.image_path, int(item.classname)))

f = open(pairs_filepath, 'a+')
for item in dataset:
	f.write("%d\t%s\t%d" % (1, item.image_path, int(item.classname)))
f.close()
