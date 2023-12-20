#!/usr/bin/python3
""" Checks data set if UTF-8 Validation """


def validUTF8(data):
    """ Checks data set """
    num_bytes = 0

    for byte in data:
        if num_bytes == 0:
            if byte < 128:
                continue

            if 192 <= byte < 224:
                num_bytes = 1
            elif 224 <= byte < 240:
                num_bytes = 2
            elif 240 <= byte < 248:
                num_byes = 3
            else:
                return False
        else:
            if 128 <= byte < 192:
                num_bytes -= 1
            else:
                return False
    return True
