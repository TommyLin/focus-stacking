import numpy as np
import math
import time
import pytest

from _matrix import Matrix, multiply_naive, multiply_tile, multiply_mkl

def execute(func, i, j, tsize):
    k = np.random.randint(100, 200)
    np_mat1 = np.random.random((i, k))
    np_mat2 = np.random.random((k, j))
    mat1 = Matrix(np_mat1)

    mat2 = Matrix(np_mat2)
    if func == multiply_tile:
        result = func(mat1, mat2, tsize)
    else:
        result = func(mat1, mat2)

    assert result.nrow == i
    assert result.ncol == j
    assert np.array(result) == pytest.approx(np.matmul(np_mat1, np_mat2))

def test_multiply_naive():
    execute(multiply_naive, 128, 128, 0)

def test_multiply_tile1():
    execute(multiply_tile, 128, 128, 0)
    execute(multiply_tile, 128, 128, 15)
    execute(multiply_tile, 128, 128, 16)
    execute(multiply_tile, 128, 128, 17)
    execute(multiply_tile, 128, 128, 256)

def test_multiply_tile2():
    execute(multiply_tile, 128, 127, 16)
    execute(multiply_tile, 128, 128, 16)
    execute(multiply_tile, 128, 129, 16)

def test_multiply_tile3():
    execute(multiply_tile, 127, 128, 16)
    execute(multiply_tile, 128, 128, 16)
    execute(multiply_tile, 129, 128, 16)

def test_multiply_tile4():
    execute(multiply_tile, 5, 5, 3)

def test_multiply_mkl():
    execute(multiply_mkl, 128, 128, 0)

def test_performance():
    np_mat1 = np.random.random((1000, 1000))
    np_mat2 = np.random.random((1000, 1000))
    mat1 = Matrix(np_mat1)
    mat2 = Matrix(np_mat2)

    naive_timing = []
    for i in range(5):
        start = time.time()
        multiply_naive(mat1, mat2)
        end = time.time()
        naive_timing.append(end - start)

    tile_timing = []
    for i in range(5):
        start = time.time()
        multiply_tile(mat1, mat2, 8)
        end = time.time()
        tile_timing.append(end - start)

    mkl_timing = []
    for i in range(5):
        start = time.time()
        multiply_mkl(mat1, mat2)
        end = time.time()
        mkl_timing.append(end - start)

    with open('performance.txt', 'w') as f:
        naivesec = np.min(naive_timing)
        tilesec = np.min(tile_timing)
        mklsec = np.min(mkl_timing)
        print('multiply_naive runtime = {0:2.4f} seconds'.format(naivesec), file=f)
        print('multiply_tile runtime = {0:2.4f} seconds'.format(tilesec), file=f)
        print('multiply_mkl runtime = {0:2.4f} seconds'.format(mklsec), file=f)
        print('Tile speed-up over naive: {0:2.2f} x'.format(naivesec/tilesec), file=f)
        print('MKL speed-up over naive: {0:2.2f} x'.format(naivesec/mklsec), file=f)
