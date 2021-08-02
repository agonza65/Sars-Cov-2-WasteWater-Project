#!/usr/bin/env python 
"""
Runs two vcf to find the percentage of the variants that were specified
Outputs the the number of variants that are matched and the percentage 
"""
from percentage import * 

# First input the syn file, then the other desired file (vcf file)
variantFile = input("Enter the first desired file to compare wiht another file: ")
vfile = input("Enter VCF file: ")

print(variantPercentage(variantFile, vfile))