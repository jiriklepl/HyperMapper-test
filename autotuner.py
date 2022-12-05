#!/usr/bin/env python3
from hypermapper import optimizer

import time
import sys
import os
import math

def measure(X):
    bs = X['BLOCK_SIZE']
    o = X['OPT_LEVEL']
    c = X['COMPILER']
    name = './tmp.bin'

    # compile
    compl = os.popen(c + ' kernels/c_kernel.c -DBLOCK_SIZE=' + str(bs) + ' -O' + str(o) + ' -o' + name).close()
    if not compl is None and not compl // 256 == 0:
        return {'val': math.inf, 'Valid': False}

    start = time.time()

    # run
    run = os.popen(name).close()

    end = time.time()

    return {'Value': end - start, 'Valid': run is None or run // 256 == 0}

parameters_file = "./parameters.json"
parameters2_file = "./parameters2.json"

optimizer.optimize(parameters_file, measure)
optimizer.optimize(parameters2_file, measure)
