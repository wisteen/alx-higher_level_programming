#!/usr/bin/python
import sys

if __name__ == "__main__":
    for content in dir(sys):
        #if content[:2] != "__":
        print("{:s}".format(content))
