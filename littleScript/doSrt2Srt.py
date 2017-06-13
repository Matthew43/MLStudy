import  os
import sys
import argparse

def doTransformSrt2Srt(a,b) :
    print(a)
    print(b)

    with open(a,'r') as sf:
        with open(b,'w') as df:
            line = sf.readline()
            while line :
                print(line)




# def parmTransform(argv):
#     parse = argparse.ArgumentParser()
#     parse.add_argument('source_file', type=str, help='source file')
#     parse.add_argument('destination_file', type=str, help='destination file')
#     return parse.parse_args(argv)


if __name__ == '__main__':
    doTransformSrt2Srt(sys.argv[1],sys.argv[2])
