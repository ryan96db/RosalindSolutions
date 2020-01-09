import urllib.request
import ssl

prot = 'P04637'

baseUrl="http://www.uniprot.org/uniprot/"
currentUrl=baseUrl+prot+".fasta"

contxt = ssl._create_unverified_context()

stuff = urllib.request.urlopen(currentUrl, context=contxt)

stuf = stuff.read()

print(stuf)
