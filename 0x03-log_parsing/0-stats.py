#!/usr/bin/python3
""" Computes stdin metrics """
from sys import stdin
import sys


def main():
    """ Checks the metrics"""
    file_size = 0
    counter = 0

    status_codes = {200: 0, 301: 0, 400: 0,
                    401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    try:
        for line in stdin:
            counter += 1
            strlen = len(line.split())
            if strlen < 9:
                continue

            code = line.split()[7]
            if int(code) in status_codes.keys():
                status_codes[int(code)] += 1
            file_size += int(line.split()[8])
            if counter == 10:
                counter = 0

                print("File size: {}".format(file_size))
                for key, value in sorted(status_codes.items()):
                    if value:
                        print("{}: {}".format(key, value))
    except KeyboardInterrupt:
        counter = 0

        print("File size: {}".format(file_size))
        for key, value in sorted(status_codes.items()):
            if value:
                print("{}: {}".format(key, value))

    print("File size: {}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value:
            print("{}: {}".format(key, value))


if __name__ == "__main__":
    main()
