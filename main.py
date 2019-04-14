#!/usr/bin/python2
from bag2vid import bag2vid
import cv2
import sys


def main():
    path = ''
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print('Please enter filename')
        exit()
    obj = bag2vid(path)
    raw_topics = obj.getalltopic()
    img_topics = obj.filterImg(raw_topics)
    for tp_name, tp_type, tp_hz in img_topics:
        obj.convert(tp_name, tp_type, tp_hz)


if __name__ == "__main__":
    main()
