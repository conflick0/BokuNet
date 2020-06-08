import os
from shutil import copyfile
import tensorflow as tf
import matplotlib.pyplot as plt


def tensor2img(tensor_img):
    return tf.make_ndarray(tf.make_tensor_proto(tensor_img)).astype('uint8')


def mkdir_dataset(raw_dataset_dir, augment_dataset_dir):
    os.mkdir(augment_dataset_dir)

    os.mkdir(augment_dataset_dir + "/train")
    os.mkdir(augment_dataset_dir + "/test")

    for label in os.listdir(raw_dataset_dir):
        os.mkdir(augment_dataset_dir + "/train/" + label)
        os.mkdir(augment_dataset_dir + "/test/" + label)


def build_dataset(raw_dataset_dir, augment_dataset_dir, train_data_scale=0.8):
    print(os.listdir(raw_dataset_dir))

    for label in os.listdir(raw_dataset_dir):
        print(label)

        # split train & test dataset
        img_dirs = os.listdir(raw_dataset_dir + "/" + label)
        train_img_dirs = img_dirs[:int(len(img_dirs) * train_data_scale)]
        test_img_dirs = img_dirs[int(len(img_dirs) * train_data_scale):]

        for train_img_name in train_img_dirs:
            img_dir = raw_dataset_dir + "/" + label + "/" + train_img_name
            tar_img_dir = augment_dataset_dir + "/train/" + label

            flip_img = tensor2img(tf.image.flip_left_right(plt.imread(img_dir)))

            copyfile(img_dir, tar_img_dir + "/" + train_img_name)
            plt.imsave(tar_img_dir + "/" + 'aug_' + train_img_name, flip_img)

        for test_img_name in test_img_dirs:
            img_dir = raw_dataset_dir + "/" + label + "/" + test_img_name
            tar_img_dir = augment_dataset_dir + "/test/" + label

            flip_img = tensor2img(tf.image.flip_left_right(plt.imread(img_dir)))

            copyfile(img_dir, tar_img_dir + "/" + test_img_name)
            plt.imsave(tar_img_dir + "/" + 'aug_' + test_img_name, flip_img)


def build(raw_dataset_dir, augment_dataset_dir):
    if not os.path.isdir(augment_dataset_dir):
        mkdir_dataset(raw_dataset_dir, augment_dataset_dir)
        build_dataset(raw_dataset_dir, augment_dataset_dir)

    else:
        print("dataset dir is exist !!")


if __name__ == '__main__':
    raw_dataset_dir = "../raw_dataset/sdd_raw_dataset"

    augment_dataset_dir = "../augment_dataset/sdd"

    build(raw_dataset_dir, augment_dataset_dir)
