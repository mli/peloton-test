#!/usr/bin/env python
import os, sys
curr_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(curr_path)
import sqlgen
import random

res = sqlgen.generate('SELECT * FROM cmu WHERE name = NAME', dict(NAME=['andy', 'joy']))
assert(res == ['SELECT * FROM cmu WHERE name = andy', 'SELECT * FROM cmu WHERE name = joy'])

res = sqlgen.generate('SELECT * FROM COMPANY WHERE VAR1 OP VAR2',
                      dict(COMPANY=['cmu'],
                           VAR1=['age', 'height'],
                           OP=['=', '>'],
                           VAR2=[2]))
assert(res == ['SELECT * FROM cmu WHERE age = 2', 'SELECT * FROM cmu WHERE age > 2', 'SELECT * FROM cmu WHERE height = 2', 'SELECT * FROM cmu WHERE height > 2'])
