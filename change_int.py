import os

txt_path='./ch4_training_localization_transcription_gt/'
txt_save_path='./1/'

txt_list=os.listdir(txt_path)
for txt in txt_list:
    with open(txt_path+txt)as f, open(txt_save_path+txt,'w')as f1:
        lines=f.readlines()
        for line in lines:
            line=line.strip()
            words=line.split(',')
            f1.write(str(int(float(words[0])))+','+str(int(float(words[1])))+','+str(int(float(words[2])))+','+str(int(float(words[3])))+','+str(int(float(words[4])))+','+str(int(float(words[5])))+','+str(int(float(words[6])))+','+str(int(float(words[7])))+','+'textline'+'\n')
