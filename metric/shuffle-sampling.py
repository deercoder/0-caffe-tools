#!/usr/bin/env python
import random

n = 2252
all_set = [1182, 560, 202, 2252]
all_name = ['CA', 'OT', 'LI', 'AI']


for i in range(1, 5):
	a = random.sample(range(n), n)
	print a
	a = [x % all_set[i-1] for x in a ]
	print a
