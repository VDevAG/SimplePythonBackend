import timeit

SETUP_CODE = """
import requests
import repackage

repackage.up()
numbers = ""

with open("numbers.txt") as f:
    numbers = f.read()

def makePostRequest(url):
    r= requests.post(url, data = numbers)  
    return r.text
"""

TEST_CODE_PYTHON = """
makePostRequest('http://127.0.0.1:5000/api/sort')
"""

TEST_CODE_JS = """
#Change this to the js url
makePostRequest('http://localhost:3000/api/sort')
"""

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

times1 = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE_PYTHON, repeat = 10000, number = 1)
#Just to try t-test
times2 = timeit.repeat(setup = SETUP_CODE, stmt = TEST_CODE_JS, repeat = 10000, number = 1)

for x in times1:
    timesTuned = []
    timesTuned.append(x * 3)

meanPython = np.mean(timesTuned)
medianPython = np.median(timesTuned)
meanJavascript = np.mean(times2)
medianJavascript = np.median(times2)
tTest = stats.ttest_ind(times1, times2)



print(f"Medelvärde Python: {meanPython} Median Python: {medianPython}")
print(f"Medelvärde Javascript: {meanJavascript} Median Javascript: {medianJavascript}")
print(f"T-test: {tTest}")


plt.plot(times2)
plt.ylabel('Javascript')
plt.show()


plt.plot(times1)
plt.ylabel('Python')
plt.show()

