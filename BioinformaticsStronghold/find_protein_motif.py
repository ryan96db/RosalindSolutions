# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 09:49:08 2020

@author: rdebo2
"""
from urllib.request import urlopen
code = "P07204_TRBM_HUMAN"
from Bio import SeqIO

#proxy_support = urllib.request.ProxyHandler({'http' : 'http://proxy.swmed.edu:3128', 'https' : 'https://proxy.swmed.edu:3128'})
#openr = urllib.request.build_opener(proxy_support)
#urllib.request.install_opener(openr)

url = "http://www.uniprot.org/uniprot/" + code + ".fasta"
response = urlopen(url)

fasta = response.read().decode("utf-8", "ignore")

#Removes header from fasta data for each protein sequence
def removeHeader(fastaSequence):
    headerArray = []
    header = ""

    for elem in fastaSequence:
        headerArray.append(elem)
        if elem == '\n':
            break

    for elem in headerArray:
        header += elem

    fastaSequence = fastaSequence.replace(header, '')
    return fastaSequence

prot = removeHeader(fasta)

#NLinked Glycosylation will look for N-X-Y, and N-X-S
def findNLinks(fastaSequence):

    instances = [fastaSequence[x:x+3] for x in range(0, len(fastaSequence))]
    #Finds all possible 3-letter substrings in the fasta sequence
    for index, element in enumerate(instances):
        beginsWithN = element[0] == 'N'
        endsWithSY = element[2] == 'S' or element[2] == 'Y'
        if beginsWithN and endsWithSY:
            return index
            

print(findNLinks(prot))

    
