import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps
from scipy.interpolate import CubicSpline
from copy import deepcopy


def FuncFi(x, l, fi):
    return fi[0] + fi[1] * np.cos(np.pi * x / l) + fi[2] * np.cos(2 * np.pi * x / l)


def FuncB(x, l, fb):
    return fb[0] + fb[1] * np.cos(np.pi * x / l) + fb[2] * np.sin(np.pi * x / l) +\
           fb[3] * np.cos(2 * np.pi * x / l) + fb[4] * np.sin(2 * np.pi * x / l)


def RightConst(y, l, tau, b_params, h, size):
    result = np.zeros(size)

    #simpson = (l / 6) * (FuncB(0, l, fb) + 4 * FuncB(l/2, l, fb) + FuncB(l, l, fb))

    '''simpson = (1 / 3) * (FuncB(0, l, b_params) * y[0] + FuncB((size - 1)*h, l, b_params) * y[size-1])

    for i in range(2, size, 2):
        simpson += (2 / 3) * (FuncB(i * h, l, b_params) * y[i])

    for i in range(1, size, 2):
        simpson += (4 / 3) * (FuncB(i * h, l, b_params) * y[i])'''

    indexes = list(range(size))
    start = indexes.pop(0)
    finish = indexes.pop(len(indexes)-1)
    odds = indexes[0::2]
    evens = indexes[1::2]
    
    simpson = FuncB(0, l, b_params) * y[start] + FuncB(l, l, b_params) * y[finish]

    for i in evens:
        simpson += 2 * (FuncB(i * h, l, b_params) * y[i])

    for i in odds:
        simpson += 4 * (FuncB(i * h, l, b_params) * y[i])
    
    simpson *= h/3
    
    #simpson = simps([FuncB(i, l, fb) for i in range(size)], [i*h for i in range(size)]
    
    for i in range(1, size-1):
        result[i] = y[i] * ((1 / tau) + FuncB(i * h, l, b_params) - simpson)
        if np.isnan(result[i]):
            raise ValueError('Explosion')

    return result


def draw_solution(T, l, a, h, tau, fi_params, b_params):
    size = int(l/h)+1

    B = np.zeros((size, size))
    
    y = [FuncFi(i*h, l, fi_params) for i in range(size)]
    fi = [FuncFi(i*h, l, fi_params) for i in range(size)]
    b = [FuncB(i*h, l, b_params) for i in range(size)]

    coef1 = -a**2/h**2
    coef2 = 2*a**2/h**2 + 1/tau

    for i in range(1, size-1):
        B[i][i - 1] = coef1
        B[i][i] = coef2
        B[i][i + 1] = coef1

    B[0][0] = 1
    B[0][1] = -1
    B[1][0] = 0
    B[size-2][size-1] = 0
    B[size-1][size-2] = -1
    B[size-1][size-1] = 1
    print(B)

    y[0] = 0
    y[size-1] = 0

    for i in range(1, T + 1):
        y = np.linalg.solve(B, RightConst(y, l, tau, b_params, h, size))
        print(f'y = {y}')

    x = [i * h for i in range(size)]

    plt.plot(x, b, 'r')
    plt.plot(x, fi, 'b')
    plt.plot(x, y, 'black')

    '''cs = CubicSpline(x, y, bc_type='natural')
    xs = np.arange(0, l, h/5)
    plt.plot(xs, cs(xs), 'g')'''

    plt.grid()
    plt.show()


def main():
    draw_solution(1, 42, 2, 1, 1, (3.5, 1, 1), (0, 0.25, -0.25, -0.5, -0.5))


if __name__ == '__main__':
    main()
