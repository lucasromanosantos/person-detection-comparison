import os
import xml.etree.ElementTree

images_path = '/home/lrs14/inria/INRIAPerson/Train/pos/'
xml_path = '/home/lrs14/inria/Xmls/Train/xmls'

LABEL = 'inria_person' # head / shoulder / inria_person

txt = open('train.txt', 'w')
for filename in os.listdir(xml_path):

  e = xml.etree.ElementTree.parse(xml_path + '/' + filename).getroot()
  treated_filename = filename.split('.')[0] + '.txt'

  size = e.find('size')
  width = float(size.find('width').text)
  height = float(size.find('height').text)

  objs = []
  for obj in e.iter('object'):
    if obj.find('name').text == LABEL:

      bndbox = obj.find('bndbox')
      xmin = float(bndbox.find('xmin').text)
      ymin = float(bndbox.find('ymin').text)
      xmax = float(bndbox.find('xmax').text)
      ymax = float(bndbox.find('ymax').text)

      xmin = int(xmin)
      ymin = int(ymin)
      xmax = int(xmax)
      ymax = int(ymax)
     
      obj = ','.join(map(str, [xmin, ymin, xmax, ymax, '0']))
      objs.append(obj)

  img_filename = filename.replace("xml", "png")
  line = images_path + img_filename + " " + " ".join(objs) + "\n"
  txt.write(line)

txt.close()

