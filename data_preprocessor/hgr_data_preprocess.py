import os
from shutil import copyfile

RAW_DATA_DIR = "../raw_data/hgr"

RAW_DATASET_DIR = "../raw_dataset/hgr_raw_dataset"


def mkdir_raw_dataset():
    os.mkdir(RAW_DATASET_DIR)

    sub_dirs = os.listdir(RAW_DATA_DIR)

    for label in os.listdir(RAW_DATA_DIR + "/" + sub_dirs[0]):
        os.mkdir(RAW_DATASET_DIR + "/" + label)


def build_raw_dataset():
    for sub_dir in os.listdir(RAW_DATA_DIR):
        for label in os.listdir(RAW_DATA_DIR + "/" + sub_dir):

            src_label_dir = RAW_DATA_DIR + "/" + sub_dir + "/" + label
            tar_label_dir = RAW_DATASET_DIR + "/" + label

            for img in os.listdir(src_label_dir):
                print(img)
                copyfile(src_label_dir + "/" + img, tar_label_dir + "/" + img)


if __name__ == '__main__':

    if not os.path.isdir(RAW_DATASET_DIR):

        mkdir_raw_dataset()

        build_raw_dataset()

    else:
        print("hgr raw dataset is exist !!")
