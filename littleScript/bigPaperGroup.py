import os
from _ctypes import sizeof


def main(path):
    files = os.listdir(path)
    author_dict = {}
    for file in files:
        file_path = os.path.join(path,file)
        with open(file_path,'r')  as f:
            for line in f.readlines():
                seps = line.strip('\n').split('|')
                if seps[0]:
                    print(seps)
                    authors = seps[2].split(';')
                    for author in authors:
                        k = author.strip()
                        v = author_dict.get(k,[])
                        v.append(seps[1])
                        author_dict[k] = v

    # 排序 输出
    list = [(v,k) for v,k in author_dict.items()]
    # print(list[0])
    # print(len(list[0][1]))
    list.sort(key = lambda x: len(x[1]))


    for item in list:
        print(item[0],':' ,len(item[1]),':',item[1])






if __name__ == '__main__':
    main('E:\基金\顶会\IGARSS')
