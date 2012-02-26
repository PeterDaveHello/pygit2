# -*- coding: utf-8 -*-
#
# Copyright 2012 Carlos Martín Nieto
#
# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License, version 2,
# as published by the Free Software Foundation.
#
# In addition to the permissions in the GNU General Public License,
# the authors give you unlimited permission to link the compiled
# version of this file into combinations with other programs,
# and to distribute those combinations without any restriction
# coming from the use of this file.  (The General Public License
# restrictions do apply in other respects; for example, they cover
# modification of the file, and distribution when not linked into
# a combined executable.)
#
# This file is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; see the file COPYING.  If not, write to
# the Free Software Foundation, 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301, USA.

"""Tests for Index files."""

from __future__ import absolute_import
from __future__ import unicode_literals
from binascii import b2a_hex
import os
import unittest

import pygit2
from . import utils


__author__ = 'carlos@cmartin.tk (Carlos Martín Nieto)'

TREE_SHA = '967fce8df97cc71722d3c2a5930ef3e6f1d27b12'

class TreeBuilderTest(utils.BareRepoTestCase):
    def test_new_empty_treebuilder(self):
        bld = pygit2.TreeBuilder()

    def test_noop_treebuilder(self):
        tree = self.repo[TREE_SHA]
        bld = pygit2.TreeBuilder(tree)
        result = bld.write(self.repo)
        self.assertEqual(tree.oid, result)

    def test_rebuild_treebuilder(self):
        tree = self.repo[TREE_SHA]
        bld = pygit2.TreeBuilder(tree)
        for e in tree:
            bld.insert(e)

        result = bld.write(self.repo)
        self.assertEqual(tree.oid, result)

if __name__ == '__main__':
    unittest.main()