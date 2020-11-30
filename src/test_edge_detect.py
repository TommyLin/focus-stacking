#!/usr/bin/env python3

import os
# import tempfile

import edge_detect as ed
import pytest

fin = "../images/fly1.jpg"
fout = "fly.jpg"


def testInvalidParameters():
    with pytest.raises(SyntaxError):
        ed.edge_detect("", "")
    with pytest.raises(SyntaxError):
        ed.edge_detect(fin, "")
    with pytest.raises(SyntaxError):
        ed.edge_detect("", fout)


def testNormalCase():
    # fout=tempfile.TemporaryFile()
    ed.edge_detect(fin, fout)
    assert os.path.isfile(fout)
    os.remove(fout)
