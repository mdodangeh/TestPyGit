# import subprocess
# import pandas as pd
import sys
import requests
import os
import math

print("Hello")
print(sys.version)
r = requests.get("https://coreyms.com")
print(r.status_code)

# name = input(" Input your name! ")
# print("Hello ", name)

# data = [[1,45.2,53.3,99,99,10,20,1,0]]
# in_df = pd.DataFrame(data, columns=['ID', 'T1', 'T2', 'N_Biop', 'HypPlas', 'AgeMen', 'Age1st', 'N_Rels', 'Race'])


# in_df.to_excel('test.xlsx',index=False)


# retcode = subprocess.call(['C:/Program Files/R/R-4.0.2/bin/Rscript.exe','My_Rscript.R'], shell = True)

# df = pd.read_excel('out_data.xlsx')
