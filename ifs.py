import numpy as np
import numpy.random as npr
import functools

import matplotlib.pyplot as plt

def nn():
    weights = [npr.randn(20, 20) / np.sqrt(20) for _ in range(100)]

    def nonlinearity(res):
        new_res = res.copy()
        new_res[new_res < 0] *= 0.3
        return new_res

    # def nonlinearity(res):
    #     return res / res.sum()

    def closure_nn(inp):
        curr_res = inp
        for weight in weights:
            curr_res = nonlinearity(curr_res @ weight)
        return curr_res.sum()
    return closure_nn

def res_img(f, size=50):
    inp = npr.randn(20)
    x = np.linspace(-5, 5, size)
    y = np.linspace(-5, 5, size)
    res = np.zeros((size, size))
    for x_idx in range(size):
        for y_idx in range(size):
            inp[0] = x[x_idx]
            inp[1] = y[y_idx]
            res[x_idx, y_idx] = f(inp)
    return res

if __name__ == "__main__":
    res = res_img(nn())
    plt.imshow(res)
    plt.show()
