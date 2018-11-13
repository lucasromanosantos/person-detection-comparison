import os
import xml.etree.ElementTree

xml_path = '/home/lrs14/inria/Xmls/Test/xmls/'
images_path = '/home/lrs14/inria/INRIAPerson/Train/pos/'
result_path = './ground-truth/'

label = 'shoulder' # head / shoulder / inria_person

for filename in os.listdir(xml_path):
  png_filename = images_path + filename.replace('xml', 'png') + '\n'

  # if not jpg_filename in test_reduced:
  #   continue
   
  e = xml.etree.ElementTree.parse(xml_path + filename).getroot()
  treated_filename = filename.split('.')[0] + '.txt'
  txt = open(result_path + treated_filename, 'w')

  size = e.find('size')
  width = float(size.find('width').text)
  height = float(size.find('height').text)

  for obj in e.iter('object'):
    if label != obj.find('name').text:
      continue
    bndbox = obj.find('bndbox')

    xmin = float(bndbox.find('xmin').text)
    ymin = float(bndbox.find('ymin').text)
    xmax = float(bndbox.find('xmax').text)
    ymax = float(bndbox.find('ymax').text)

    line = ' '.join(map(str, [label, xmin, ymin, xmax, ymax, '\n']))
    txt.write(line)

  txt.close()

