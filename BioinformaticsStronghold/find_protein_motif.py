# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 14:50:34 2019

@author: rdebo2
"""

import urllib.request
code = "Q7Z7W5"


proxy_support = urllib.request.ProxyHandler({'http' : 'http://proxy.swmed.edu:3128', 'https' : 'https://proxy.swmed.edu:3128'})
openr = urllib.request.build_opener(proxy_support)
urllib.request.install_opener(openr)

data=urllib.request.urlopen("http://www.uniprot.org/uniprot/" + code + ".fasta")
content = data.read()
print(content)