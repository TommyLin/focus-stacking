#!/usr/bin/env python3

import pytest
import math
import numpy as np
import focus_stacking as fs

def testInvalidVector():
    with pytest.raises(TypeError):
        fs.angle([0, 0], [])
    with pytest.raises(TypeError):
        fs.angle([], [0, 0])
    with pytest.raises(TypeError):
        fs.angle([], [])
    with pytest.raises(TypeError):
        fs.angle(["1", 2], [1, 1])

# Test for zero-length 2-vector (invalid input).
def testZeroLengthVector():
    with pytest.raises(ValueError):
        fs.angle([1, 1], [0, 0])
    with pytest.raises(ValueError):
        fs.angle([0, 0], [1, 1])
    with pytest.raises(ValueError):
        fs.angle([0, 0], [0, 0])

# Test for zero angle.
def testZeroAngle():
    for i in range(10):
        mult = np.random.randint(1, 10)
        vec1 = np.random.randint(1, 10, 2)
        vec2 = vec1 * mult
        assert (fs.angle(vec1, vec2)) == 0
