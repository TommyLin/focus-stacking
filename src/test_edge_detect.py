#!/usr/bin/env python3

import os
import pytest
import tempfile
import edge_detect as ed

fin='../images/fly1.jpg'

def testInvalidParameters():
    with pytest.raises(SyntaxError):
        ed.edge_detect('', '')
    with pytest.raises(SyntaxError):
        ed.edge_detect(fin, '')
    with pytest.raises(SyntaxError):
        ed.edge_detect('', 'fly1_edge1.jpg')

def testNormal():
#    fout=tempfile.TemporaryFile()
    fout='fly.jpg'
    ed.edge_detect(fin, fout)
    assert (os.path.isfile(fout)) == True
    os.remove(fout)

