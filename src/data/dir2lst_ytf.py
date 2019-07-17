import sys
import os
from easydict import EasyDict as edict

input_dir = '/home/ti/Downloads/insightface/src/align/our_dataset'
pairs_filepath = '/home/ti/Downloads/insightface/src/align/our_data.lst'
ret = []
label = 0
person_names = []
for person_name in os.listdir(input_dir):
  person_names.append(person_name)
person_names = sorted(person_names)
# print(person_names)
for person_name in person_names:
  _subdir = os.path.join(input_dir)
  # print(_subdir)
  if not os.path.isdir(_subdir):
    continue
  cnt = 0
  for _subdir2 in os.listdir(_subdir):
    _subdir2 = os.path.join(_subdir, _subdir2)
    cnt = cnt + 1  
    #if not os.path.isdir(_subdir2):
      #continue
    _ret = []  
    #print('got')
    for img in os.listdir(_subdir2):
      # print(label)
      fimage = edict()
      #print('here')
      fimage.id = os.path.join(_subdir2, img)
      fimage.classname = str(label)
      fimage.image_path = os.path.join(_subdir2, img)
      #print(fimage.image_path)
      fimage.bbox = None
      fimage.landmark = None
      _ret.append(fimage)
      # print(fimage)
    ret += _ret
    print(label)
  label+=1
  print(label)
  # print(ret)
f = open(pairs_filepath, 'a+')
# print(len(person_names))
i = 1
for item in ret:
    #print(item.classname)
    f.write(str(1) + '\t' + str(item.image_path) + '\t' + item.classname + '\n')
    i = i + 1
#f.close()

#for item in ret:
#  print("%d\t%s\t%d" % (1, item.image_path, int(item.classname)))
