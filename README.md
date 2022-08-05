# REVERIE Challenge 2022 (Findwell)

This repository is the official implementation of our method.

## Requirements

1. Install Matterport3D simulators: follow instructions [here](https://github.com/peteanderson80/Matterport3DSimulator). We use the latest version instead of v0.1.
```
export PYTHONPATH=Matterport3DSimulator/build:$PYTHONPATH
```

2. Install requirements:
```setup
conda create --name vlnduet python=3.8.5
conda activate vlnduet
pip install -r requirements.txt
```

3. Data preperation:

- Download datasets from [Baidu Cloud Disk](https://pan.baidu.com/s/1dgQq0X4iQNAvHrXPiInGEg) [code: cim7], including annotations, features and trained models of REVERIE datasets. 
- Download the object features [reverie_obj_feats_v2.pkl] from [Google Drive](https://drive.google.com/file/d/1zwV3QDPUVt7YmBNqTaCdS6v01U4b6p7M/view?usp=sharing) or [Baidu Cloud Disk](https://pan.baidu.com/s/1hxNypQZLz21RQpMD6yQNag?pwd=nubg) [code: nubg] and put it under datasets/REVERIE/features.
- After downloading data you should see the following folder structure:
```
    ├── datasets
    │   ├── REVERIE
    │   │   ├── exprs_map
    │   │   │   └── pretrain
    │   │   │       └── model_step_100000.pt
    │   │   │   └── finetune
    │   │   │       └── best_val_unseen
    │   │   ├── features
    │   │   │   ├── pth_vit_base_patch16_224_imagenet.hdf5
    │   │   │   ├── obj.avg.top3.min80_vit_base_patch16_224_imagenet.hdf5
    │   │   │   └── reverie_obj_feats_v2.pkl
    │   │   └── annotations
    │   │       ├── REVERIE_train.json
    │   │       ├── REVERIE_val_seen.json
    │   │       ├── REVERIE_val_unseen.json
    │   │       ├── REVERIE_test.json
    │   │       ├── objpos.json
    │   │       ├── BBoxes_v2
    │   │       └── pretrain
    │   ├── R2R
    │   │    ├── annotations
    │   │    └── connectivity
    │   └── pretrained
    │       └── LXMERT
    │           └── model_LXRT.pth
```


## Pretraining

Combine behavior cloning and auxiliary proxy tasks in pretraining:
```pretrain
cd pretrain_src
bash run_reverie.sh
```

## Fine-tuning & Evaluation

Use pseudo interative demonstrator to fine-tune the model:
```finetune
cd map_nav_src
bash scripts/run_reverie.sh
```
## Reproducing Testing Results 

- Use trained model to reproduce the results on the test split:
```finetune
cd map_nav_src
bash scripts/test_reverie.sh
```
- After runing test_reverie.sh, you should run the `replace_reverie_to_number.py` to convert json files into the format required by the competition

