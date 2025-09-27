param_values = ['64', '128', '256', '512', '1024', '2048', ]
times = {  r'quicksort': ([0.3472,0.594492,1.71702,3.72268,7.87285,17.8885,],
[0.137021,0.0526348,0.676347,1.05854,1.84493,5.1103,]),
  r'bubble': ([0.619521,2.37792,8.46012,33.4657,125.534,522.808,],
[0.285753,0.928285,2.57482,6.23305,2.49574,5.68253,]),
}
import matplotlib as mpl
mpl.use('svg')
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(len(param_values))
width = 1.0 / (len(times) + 1)
multiplier = 0
fig, ax = plt.subplots()
for at, (meas, err) in times.items():
  offset = width * multiplier
  rects = ax.bar(x + offset, meas, width, label=at, alpha=0.6, yerr=err)
  multiplier += 1
ax.set_yscale('log')
ax.set_xlabel(r'n')
ax.set_ylabel(r't [ms]')
plt.xticks(x + width * (2 - 1) / 2, param_values)
ax.set_axisbelow(True)
plt.grid(axis='y')
plt.legend(loc='best')
plt.savefig(r'.csbench/group_bar_0.svg', dpi=100, bbox_inches='tight')
