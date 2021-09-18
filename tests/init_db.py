#!/usr/bin/env python3
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))  # fix import directory
# sys.path.append('..')  # fix import directory
from app import db
db.create_all()
