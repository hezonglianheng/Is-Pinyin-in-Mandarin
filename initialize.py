import json
import os.path


def read_pinyin():
    abs_path = os.path.abspath(r'source')
    txt_path = os.path.join(abs_path, r'pinyin.txt')
    json_path = os.path.join(abs_path, r'pinyin_set.json')
    if os.path.exists(txt_path):
        pinyin_set = set()
        with open(r'source\pinyin.txt',
                  encoding='utf8', mode='r+') as file:
            file_lines = file.readlines()
            for line in file_lines[1:]:
                items = line.split()
                pinyin_set.add(items[-1])
            #print(pinyin_set)
            file.close()
        with open(json_path, mode='w+') as file:
            json.dump(list(pinyin_set), file)
            file.close()


if __name__ == "__main__":
    read_pinyin()