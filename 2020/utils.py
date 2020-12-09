"""Each main sovler function loads puzzle day (inp)
using load_input_as_list(inp), simply reading the txt
file line by line and loading into a list"""

from functools import reduce
import re
from collections import Counter

def load_input_as_list(filepath):
    with open(filepath, "r") as f:
        raw = f.readlines()
    inp = [i.replace('\n', '') for i in raw]
    return inp