#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Minimal implementation of Git with simplified versions of Git commands.
It is not meant for anything serious, just for fun. Feel free to extend!

@author: Patrick Kariuki
"""

# To parse command-line arguments
import argparse
# Container types
import collections
# To read and write configuration files
import configparser
# To access the SHA-1 function
import hashlib
# ceil from math module
from math import ceil
# To provide filesystem abstraction routines
import os
# Regex
import re
# To access actual command-line arguments
import sys
# To compress everything like Git
import zlib