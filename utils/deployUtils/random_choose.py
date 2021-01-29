import os
import random
import shutil


def chooseFile(filepath, tarpath):
    filedir = os.listdir(filepath)
    sample = random.sample(filedir, 500) # random choose 500 contracts

    for s in sample:
        shutil.copyfile(filepath+"/" + s, tarpath+ "/" +s)


if __name__ == '__main__':
    filepath = "/Users/luliu/PycharmProjects/my_smartbugs/contract"
    targetpath = "/Users/luliu/PycharmProjects/my_smartbugs/contract500"
    chooseFile(filepath, targetpath)
    print("Sucessfully Output!")