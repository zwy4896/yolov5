import json
import os

label_list = ['epoxy', 'matter', 'copper_line']
def convert(img_size, box):
    dw = 1. / (img_size[0])
    dh = 1. / (img_size[1])
    x = (box[0] + box[2]) / 2.0 - 1
    y = (box[1] + box[3]) / 2.0 - 1
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    # x1 = box[0]
    # y1 = box[1]
    # x2 = box[2]
    # y2 = box[3]
    return (x, y, w, h)


def decode_json(json_floder_path, json_name):
    txt_name = './data/datasets/ch4/labels/' + json_name[0:-5] + '.txt'
    txt_file = open(txt_name, 'w')

    json_path = os.path.join(json_floder_path, json_name)
    data = json.load(open(json_path, 'r', encoding='utf-8'))

    img_w = data['imageWidth']
    img_h = data['imageHeight']

    for i in data['shapes']:

        if (i['shape_type'] == 'rectangle' and i['label']):
            label = i['label']
            x1 = int(i['points'][0][0])
            y1 = int(i['points'][0][1])
            x2 = int(i['points'][1][0])
            y2 = int(i['points'][1][1])

            bb = (x1, y1, x2, y2)
            bbox = convert((img_w, img_h), bb)
            txt_file.write('{} {}'.format(label_list.index(label), " ".join([str(a) for a in bbox]) + '\n'))


if __name__ == "__main__":

    json_floder_path = '/home/trd/share/DATASET/train/CH4_seg/json_yolo'
    json_names = os.listdir(json_floder_path)
    for json_name in json_names:
        decode_json(json_floder_path, json_name)

