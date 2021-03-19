import json
from PIL import Image
import base64

'''
820,827,1559,827,1559,930,820,930,textline
2846,850,3188,850,3188,947,2846,947,textline
3281,879,3572,879,3572,934,3281,934,textline
'''
#data=[820,827,1559,827,1559,930,820,930]

img=Image.open('./IMG_6550.JPG')
(h,w)=img.size

with open('./IMG_6550.JPG','rb') as f1:
    base64_data = base64.b64encode(f1.read())

with open('./IMG_6550.txt')as f:
    x1=[]
    x2=[]
    x3=[]
    x4=[]
    t=[]
    lines=f.readlines()
    for line in lines:
        line=line.strip()
        words=line.split(',')
        x1.append([float(words[0]),float(words[1])])
        x2.append([float(words[2]),float(words[3])])
        x3.append([float(words[4]),float(words[5])])
        x4.append([float(words[6]),float(words[7])])
        t.append(words[8])

    jsontext={'shapes':[]}
    for i in range(len(x1)):
        jsontext['version']='4.2.10'
        jsontext['flags']={}
        #jsontext['shapes']=
        jsontext['shapes'].append({'label':t[i],'points':[x1[i],x2[i],x3[i],x4[i]],'shape_type': 'polygon','flags': {},"group_id": None,})
        jsontext['imagePath']='IMG_6550.JPG'
        jsontext['imageData']=str(base64_data)
        jsontext['imageHeight']=int(h)
        jsontext['imageWidth']=int(w)

    jsondata = json.dumps(jsontext,indent=2,separators=(',',': '))

    f=open('filename.json','w')
    f.write(jsondata)
    f.close()
