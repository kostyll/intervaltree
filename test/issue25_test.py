"""
intervaltree: A mutable, self-balancing interval tree for Python 2 and 3.
Queries may be by point, by range overlap, or by range envelopment.

Test module: IntervalTree, insertion and removal of float intervals
Submitted as issue #25 (Incorrect KeyError) by sciencectn

Copyright 2013-2014 Chaim-Leib Halbert

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from __future__ import absolute_import
from intervaltree import IntervalTree
from test.intervaltrees import trees
import pytest


def test_original_sequence():
    t = IntervalTree()
    t.addi(6.37,11.37)
    t.addi(12.09,17.09)
    t.addi(5.68,11.58)
    t.removei(6.37,11.37)
    t.addi(13.23,18.23)
    t.removei(12.09,17.09)
    t.addi(4.29,8.29)
    t.removei(13.23,18.23)
    t.addi(12.04,17.04)
    t.addi(9.39,13.39)
    t.removei(5.68,11.58)
    t.removei(4.29,8.29)
    t.removei(12.04,17.04)
    t.addi(5.66,9.66)     # Value inserted here
    t.addi(8.65,13.65)
    t.removei(9.39,13.39)
    t.addi(16.49,20.83)
    t.addi(11.42,16.42)
    t.addi(5.38,10.38)
    t.addi(3.57,9.47)
    t.removei(8.65,13.65)
    t.removei(5.66,9.66)    # Deleted here


def test_debug_sequence():
    t = IntervalTree()
    t.addi(6.37,11.37)
    t.verify()
    t.addi(12.09,17.09)
    t.verify()
    t.addi(5.68,11.58)
    t.verify()
    t.removei(6.37,11.37)
    t.verify()
    t.addi(13.23,18.23)
    t.verify()
    t.removei(12.09,17.09)
    t.verify()
    t.addi(4.29,8.29)
    t.verify()
    t.removei(13.23,18.23)
    t.verify()
    t.addi(12.04,17.04)
    t.verify()
    t.addi(9.39,13.39)
    t.verify()
    t.removei(5.68,11.58)
    t.verify()
    t.removei(4.29,8.29)
    t.verify()
    t.removei(12.04,17.04)
    t.verify()
    t.addi(5.66,9.66)     # Value inserted here
    t.verify()
    t.addi(8.65,13.65)
    t.verify()
    t.removei(9.39,13.39)
    t.verify()
    t.addi(16.49,20.83)
    t.verify()
    t.addi(11.42,16.42)
    t.verify()
    t.addi(5.38,10.38)
    t.verify()
    t.addi(3.57,9.47)
    t.verify()
    t.removei(8.65,13.65)
    t.verify()
    t.removei(5.66,9.66)    # Deleted here
    t.verify()


if __name__ == "__main__":
    pytest.main([__file__, '-v'])