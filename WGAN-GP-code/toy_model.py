import random
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import sklearn.datasets

import tflib as lib
import tflib.ops.linear
import tflib.plot

# Real data geneneration: 8 Gaussians
scale = 3.0

centers = [
	(1, 0),
	(-1, 0),
	(0, 1),
	(0, -1),
	(1, 1),
	(1, -1),
	(-1, 1),
	(-1, -1)
]


