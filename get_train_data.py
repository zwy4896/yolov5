import os
import pandas as pd
from shutil import copyfile

home = os.environ['HOME']


def read_csv(xlsPath: str) -> pd:
    data_frame = pd.read_csv(xlsPath)
    return data_frame

def get_data(dataFrame: pd, channel: str = 'CH2') -> list:
    data_list = []
    data = dataFrame[(dataFrame['标注结果'] == 'NG')& (dataFrame['相机'] == 'CH2')]
    data_list = list(map(lambda x: os.path.join(x.split('_')[0], channel, '_'.join(x.split('_')[1:])), data['图片文件名']))
    return data_list

def copy_file(dataList: list, oriDir: str, saveDir: str):
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)
    for data in dataList:
        copyfile(os.path.join(oriDir, data), os.path.join(saveDir, '_'.join(data.split('/')[::2])))
if __name__ == '__main__':
    data_set = '2021.09_NG_92组'
    csv_path = os.path.join(home, 'share/830-1-AI_Integration_Test/52.Dataset/02. H70/GroundTruth/GroundTruth_' + data_set+'.csv')
    ori_path = os.path.join(home, 'share/nas/dataset/H70/raw_data', data_set)
    save_path = os.path.join(home, 'share/DATASET/train/CH2/imgs')

    df = read_csv(csv_path)
    dt_list = get_data(df)
    copy_file(dt_list, ori_path, save_path)