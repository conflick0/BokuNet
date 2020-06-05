import os
from shutil import copyfile


def mkdir_dataset(raw_dataset_dir, dataset_dir):
    os.mkdir(dataset_dir)

    os.mkdir(dataset_dir + "/train")
    os.mkdir(dataset_dir + "/test")

    for label in os.listdir(raw_dataset_dir):
        os.mkdir(dataset_dir + "/train/" + label)
        os.mkdir(dataset_dir + "/test/" + label)


def build_dataset(raw_dataset_dir, dataset_dir, train_data_scale=0.8):
    print(os.listdir(raw_dataset_dir))

    for label in os.listdir(raw_dataset_dir):
        print(label)

        # split train & test dataset
        img_dirs = os.listdir(raw_dataset_dir + "/" + label)
        train_img_dirs = img_dirs[:int(len(img_dirs) * train_data_scale)]
        test_img_dirs = img_dirs[int(len(img_dirs) * train_data_scale):]

        for train_img_dir in train_img_dirs:
            copyfile(raw_dataset_dir + "/" + label + "/" + train_img_dir,
                     dataset_dir + "/train/" + label + "/" + train_img_dir)

        for test_img_dir in test_img_dirs:
            copyfile(raw_dataset_dir + "/" + label + "/" + test_img_dir,
                     dataset_dir + "/test/" + label + "/" + test_img_dir)


def build(raw_dataset_dir, dataset_dir):
    if not os.path.isdir(dataset_dir):
        mkdir_dataset(raw_dataset_dir, dataset_dir)
        build_dataset(raw_dataset_dir, dataset_dir)

    else:
        print("dataset dir is exist !!")


if __name__ == '__main__':
    raw_dataset_dir = "../raw_dataset/hgr_raw_dataset"

    dataset_dir = "../dataset/hgr"

    build(raw_dataset_dir, dataset_dir)
