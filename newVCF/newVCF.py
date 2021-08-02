import os

"""
Function vcf filters an existing vcf 
The main function ask what vcf file to filter and to rename it
"""
def vcf(file):

    #Check if file is empty or not
    if (os.stat(file).st_size == 0):
        print("ERROR: Empty File")

    #If not empty continue
    else:
        nvcf = open(nameNewVCF,"w")
        f = open(file)
        lines = f.readlines()
        #removes tabs from right 
        stripped = [i.rstrip() for i in lines]
        header = "#CHROM \t POS \t ID \t REF \t ALT \n"

        #Header
        nvcf.write(header)

        for i in range(18,len(stripped)):

            input = stripped[i].split()

            CHROM = input[0]
            POS  = input[1]
            # snpID = input[3][0]+POS+input[4].rstrip()
            REF = input[3]  
            ALT = input[4]

            #Deletion
            if(len(REF) > len(ALT)):
                snpID = "deletion_"+POS
            #Insertion
            elif(len(REF) < len(ALT)):
                snpID = "insertion_"+POS
            #No Indel
            else:
                snpID = input[3]+POS+input[4].rstrip()

            #Write into new file
            nvcf.write(CHROM + "\t")
            nvcf.write(POS+ "\t")
            nvcf.write(snpID+ "\t")
            nvcf.write(REF+ "\t")
            nvcf.write(ALT + "\n")

# Main
nameNewVCF = input("Name of the new VCF name: ")
file = input("Desired file to modify: ")
vcf(file)