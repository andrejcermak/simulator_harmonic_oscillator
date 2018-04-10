import sys,os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))+os.sep+'source')

from function import GraphPlot
from animate import Animation

# a = Animation().animate()
g = GraphPlot().simulate()
