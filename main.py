#!/usr/bin/python2
from bag2vid import bag2vid
import cv2


def main():
    obj = bag2vid('test.bag')
    raw_topics = obj.getalltopic()
    img_topics = obj.filterImg(raw_topics)
    for tp_name, tp_type, tp_hz in img_topics:
        obj.convert(tp_name, tp_type, tp_hz)


if __name__ == "__main__":
    main()
