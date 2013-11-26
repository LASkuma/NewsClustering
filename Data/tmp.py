from gensim import corpora, models, similiarities
import re
import csv
strings = ("Frequency", "Symbol", "Polar", "Mod", "FEC", "RF", "Signal", "Carrier", "BitRate")  
sat_raw = open('/BLScan/reports/1520.txt', 'r') 
sat_out = open('1520out.txt', 'w') 
for line in sat_raw: 
    if any(s in line for s in strings): 
        for word in line.split(): 
            if ':' in word:
                sat_out.write(line.split(':')[-1])
sat_raw.close()
sat_out.close()