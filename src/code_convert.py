
import numpy as np

def util_grayToBinary(num, bits):

    shift = 1
    while shift < bits:
        num ^= (num >> shift)
        shift <<= 1

    return num

def grayToBinary(num, offset):

    return util_grayToBinary(num, 64) - offset


def convert_pattern(pattern_img, proj_size, offset):
    for r in xrange(0, pattern_img.shape[0]):
        for c in xrange(0, pattern_img.shape[1]):
            pattern = pattern_img[r,c,:]

            if not np.isnan(pattern[0]):
                code = grayToBinary(np.int(pattern[0]), offset[0])
                if code < 0 : code = 0
                if code >= proj_size[0]: code = proj_size[0] - 1
                pattern_img[r, c, 0] = code

            if not np.isnan(pattern[1]):
                code = grayToBinary(np.int(pattern[1]), offset[1])
                if code < 0: code = 0
                if code >= proj_size[1]: code = proj_size[1] - 1
                pattern_img[r, c, 1] = code

    return pattern_img



print util_grayToBinary(8,4)