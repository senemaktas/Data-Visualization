#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

width=0.3
block1=[78]
block2=[88]
block3=[88]

plt.style.use('seaborn-darkgrid')
plt.bar("block1",block1, width=width,color = 'w', edgecolor='black', hatch = 'x')
plt.bar("block2",block2, width=width,color = 'w', edgecolor='black', hatch = '*')
plt.bar("block3",block3,width=width,color = 'w', edgecolor='black', hatch = '+')
#plt.grid(color='gray',linestyle='--',axis='y',linewidth=1,alpha=0.2)
plt.title('This is a title')
plt.xlabel('x-label')
plt.ylabel('y-label')
plt.ylim((0,90))
#plt.ylim(ymax = 250, ymin = 25)
plt.legend()
plt.show()
