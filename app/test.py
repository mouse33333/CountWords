#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import json

from PIL import Image
import xlrd
from hsk_modules import *
import jieba
import chardet
import pyperclip
import matplotlib.pyplot as plt
import pandas as pd

x = [0.29, 0.13, 0.15, 0.07, 0.05, 0.06, 0.25]

plt.rcParams['font.family'] = 'Kaiti'
plt.title("HSK各级别词汇占比")
plt.pie(x, labels=["HSK1", "HSK2", "HSK3", "HSK4", "HSK5", "HSK6", "超纲"],
        autopct="%1.0f%%", startangle=90,
        counterclock=False, radius=1.2)

plt.savefig("test.png")
img = Image.open("test.png")
img.show()

