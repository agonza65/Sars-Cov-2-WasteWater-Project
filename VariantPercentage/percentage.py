#!/usr/bin/env python 

# First input the syn file, then the other desired file (vcf file)
# variantFile = input("Enter the first desired file to compare wiht another file: ")
# vfile = input("Enter VCF file: ")

"""
Function that takes in two file specific strain and finds the percentage of the variants to a specific sample. 
This will identify the percentage of any variant, that was worked in the Univeristy, is contained in a human sample. 
"""
def variantPercentage(file1, file2):
    
    count = 0
    synSNP = []

    file1 = open(file1)          #The syn variant; Open the synFile 
    content = file1.readlines()  #Content that exist in the syn file
    stripped = [i.rstrip() for i in content]  #stripp the next lines from the lines
    
    #Iterate through the file and append the SNP column to variable `synSNP
    for i in range(0,len(stripped)):
        lines = stripped[i].split()
        
        # We care more about this,SNP's, to compare with the other files
        SNP=lines[2] 

        synSNP.append(SNP)
        file1.close()
    

    vcfFile = open(file2)      #Open the desired file that is being compared
    c = vcfFile.readlines()            #content of the file
    stripped = [i.rstrip() for i in c]
    vcfSNP = []       #Store the snp's of the file into vcfSNP
    
    #
    for i in range(3,len(stripped)):
        lines = stripped[i].split()
        snp = lines[2]
        vcfSNP.append(snp)

        vcfFile.close()


    #each snp of the syn file
    sStr = [i for i in synSNP]
    # vstr = str([i for i in vcfSNP])
    # print(sStr)
    
    matches = [] #list that stores the matches of the two files
    
    #search for the matches
    for snp in vcfSNP:
        if snp in sStr:
            count+=1 #increment the count if there is a match between the two files
            matches.append(snp) #add the matches to the match list
    #         print(snp+": ",matchPercent)
            continue

    countMatches = {i:matches.count(i) for i in matches}    #Count the each matches
    
    # print("Percentage of the individual matches: \n")
    
    for key in countMatches:
        
        matchPercent = round(countMatches.get(key)/len(vcfSNP),4)
        print(key+":",countMatches.get(key))

        totalPercentage = round((count/len(vcfSNP)),4)
        print(key+":",matchPercent)
        
    # print("Total percentage of all the matches found: ", totalPercentage)
    
# print(variantPercentage(variantFile, vfile))