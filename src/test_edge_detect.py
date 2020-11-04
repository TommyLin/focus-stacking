#!/usr/bin/env python3

import os
import pytest
import edge_detect as ed

def testInvalidParameters():
    with pytest.raises(SyntaxError):
        ed.edge_detect('', '')
    with pytest.raises(SyntaxError):
        ed.edge_detect('../images/fly1.jpg', '')
    with pytest.raises(SyntaxError):
        ed.edge_detect('', 'fly1_edge1.jpg')

def testNormal():
    # TODO Replace fixed to temporary file name
    fout='fly1_edge1.jpg'
    ed.edge_detect('../images/fly1.jpg', fout)
    assert (os.path.isfile(fout)) == True
    # TODO Remove temporary file

