import numpy as np
import numpy.random as npr
import functools

import matplotlib.pyplot as plt

def nn(act_size):
    weights = [npr.randn(act_size, act_size) / np.sqrt(act_size) for _ in range(30)]

    # def nonlinearity(res):
    #     return np.tanh(res)

    # def nonlinearity(res):
    #    new_res = res.copy()
    #    new_res[new_res < 0] *= 0.1
    #    return new_res

    def nonlinearity(res):
        return np.abs(res) / np.abs(res).sum()

    def closure_nn(inp):
        curr_res = inp
        for weight in weights:
            curr_res = nonlinearity(curr_res @ weight)
        return curr_res[10]
    return closure_nn

def res_img(f, size=256, act_size=30):
    inp = npr.randn(act_size)
    x = np.linspace(-5, 5, size)
    y = np.linspace(-5, 5, size)
    res = np.zeros((size, size))
    print("total iters: ", size * size)
    for x_idx in range(size):
        for y_idx in range(size):
            if ((x_idx * size) + y_idx) % 1000 == 0:
                print("iter: ", ((x_idx * size) + y_idx), " / ", size * size)
            inp[0] = x[x_idx]
            inp[1] = y[y_idx]
            res[x_idx, y_idx] = f(inp)
    return res

if __name__ == "__main__":
    act_size = 30
    res = res_img(nn(act_size), act_size=act_size)
    plt.imshow(res)
    plt.show()
