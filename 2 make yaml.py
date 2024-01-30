# 학습을 위한 yaml file 생성
import glob
import os

root_dir = "./contents/dataset/FaceMaskDetection/" # 이걸 절대 위치로 바꿔야 작동을 하네
img_dir = os.path.join(root_dir, "images")
label_dir = os.path.join(root_dir,"labels")

data = glob.glob(os.path.join(img_dir,"*.png"))

train = data[:650]
valid = data[650:750]
test = data[750:]

# train.txt
with open(os.path.join(root_dir, "train.txt"), 'w') as f:
	f.write('\n'.join(train) + '\n')

# valid.txt
with open(os.path.join(root_dir, "valid.txt"), 'w') as f:
	f.write('\n'.join(valid) + '\n')

# test.txt
with open(os.path.join(root_dir, "test.txt"), 'w') as f:
	f.write('\n'.join(test) + '\n')
	
# !pip install pyyaml
import yaml

yaml_data = {"names":['with_mask', 'without_mask', 'mask_weared_incorrect'], # 클래스 이름
             "nc":3, # 클래스 수
             "path":root_dir, # root 경로
             "train":os.path.join(root_dir, "train.txt"), # train.txt 경로
             "val":os.path.join(root_dir, "valid.txt"), # valid.txt 경로
             "test":os.path.join(root_dir,"test.txt") # test.txt 경로
             }

with open(os.path.join(root_dir, "custom.yaml"), "w") as f:
  yaml.dump(yaml_data, f)