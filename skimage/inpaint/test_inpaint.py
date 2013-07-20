import numpy as np
from numpy.testing import assert_array_equal
from fmm import inpaint


def test_basic():
    mask = np.array(
        [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.uint8)

    image = np.array(
        [[186, 187, 188, 185, 183, 185, 185, 176, 160, 129, 93, 51, 18, 8, 10],
         [186, 187, 187, 184, 182, 184, 180, 159, 127, 77, 32, 18, 16, 13, 13],
         [185, 185, 185, 184, 184, 183, 174, 146, 107, 59, 18, 10, 13, 12, 13],
         [186, 185, 184, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 12, 14],
         [186, 185, 185, 0, 0, 0, 0, 0, 0, 0, 0, 0, 13, 13, 14],
         [187, 187, 187, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 14, 15],
         [187, 187, 187, 0, 0, 0, 0, 0, 0, 0, 0, 0, 14, 13, 13],
         [189, 188, 188, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 13, 11],
         [190, 189, 190, 0, 0, 0, 0, 0, 0, 0, 0, 0, 12, 10, 10],
         [191, 191, 192, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 9, 10],
         [187, 188, 191, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 10],
         [185, 187, 190, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 10, 10],
         [188, 191, 191, 189, 170, 98, 29, 12, 13, 10, 10, 9, 10, 9, 9],
         [192, 196, 194, 174, 140, 76, 19, 10, 16, 13, 11, 10, 11, 9, 9],
         [189, 196, 193, 159, 113, 58, 13, 6, 13, 12, 11, 10, 10, 8, 9]],
        dtype=np.uint8)

    expected = np.array(
        [[186, 187, 188, 185, 183, 185, 185, 176, 160, 129, 93, 51, 18, 8, 10],
         [186, 187, 187, 184, 182, 184, 180, 159, 127, 77, 32, 18, 16, 13, 13],
         [185, 185, 185, 184, 184, 183, 174, 146, 107, 59, 18, 10, 13, 12, 13],
         [186, 185, 184, 184, 183, 180, 170, 158, 134, 99, 65, 23, 13, 12, 14],
         [186, 185, 185, 184, 183, 181, 167, 138, 105, 72, 26, 19, 13, 13, 14],
         [187, 187, 187, 184, 183, 183, 169, 130, 91, 42, 27, 21, 14, 14, 15],
         [187, 187, 187, 187, 185, 182, 157, 121, 70, 45, 25, 18, 14, 13, 13],
         [189, 188, 188, 188, 181, 169, 147, 112, 78, 46, 20, 14, 15, 13, 11],
         [190, 189, 190, 187, 171, 157, 136, 104, 65, 38, 18, 14, 12, 10, 10],
         [191, 191, 192, 181, 166, 162, 137, 102, 67, 23, 17, 13, 10, 9, 10],
         [187, 188, 191, 174, 174, 156, 129, 95, 55, 28, 13, 12, 9, 9, 10],
         [185, 187, 190, 186, 174, 148, 115, 66, 32, 17, 12, 9, 10, 10, 10],
         [188, 191, 191, 189, 170, 98, 29, 12, 13, 10, 10, 9, 10, 9, 9],
         [192, 196, 194, 174, 140, 76, 19, 10, 16, 13, 11, 10, 11, 9, 9],
         [189, 196, 193, 159, 113, 58, 13, 6, 13, 12, 11, 10, 10, 8, 9]],
        dtype=np.uint8)

    assert_array_equal(inpaint(image, mask, epsilon=5), expected)

if __name__ == "__main__":
    np.testing.run_module_suite()
