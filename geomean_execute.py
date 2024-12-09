import math
import numpy as np

def calculate_geomean(file_path):
    with open(file_path, 'r') as file:
        numbers = [float(line.strip()) for line in file.readlines()]
    
    # product = (numbers)

    geomean = np.exp(np.log(numbers).mean())
    # geomean = product ** (1 / len(numbers))
    
    return geomean

file_path = 'q_thresh_90_kt.txt'
print(f"q_thresh_90: {calculate_geomean(file_path)}")
file_path = 'q_thresh_70_kt.txt'
print(f"q_thresh_70: {calculate_geomean(file_path)}")
file_path = 'q_thresh_50_kt.txt'
print(f"q_thresh_50: {calculate_geomean(file_path)}")
file_path = 'k_thresh_90_kt.txt'
print(f"k_thresh_90: {calculate_geomean(file_path)}")
file_path = 'k_thresh_70_kt.txt'
print(f"k_thresh_70: {calculate_geomean(file_path)}")
file_path = 'k_thresh_50_kt.txt'
print(f"k_thresh_50: {calculate_geomean(file_path)}")
file_path = 'qk_thresh_99_kt.txt'
print(f"qk_thresh_99: {calculate_geomean(file_path)}")
file_path = 'qk_thresh_95_kt.txt'
print(f"qk_thresh_95: {calculate_geomean(file_path)}")
file_path = 'qk_thresh_995_kt.txt'
print(f"q_thresh_995: {calculate_geomean(file_path)}")
file_path = 'base_kt_seqlen.txt'
print(f"q__999: {calculate_geomean(file_path)}")
