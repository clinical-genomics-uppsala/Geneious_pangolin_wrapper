#!/usr/bin/env python3

import sys
import os
import subprocess

# Geneious input/output and options
inFile = os.path.join("/geneious", sys.argv[2]).replace("\\","/")
outFile = os.path.join("/geneious", sys.argv[4]).replace("\\","/")

# Path to temporary Geneious folder
# Example: /Users/user/Geneious 2022.1 Data/transient/1660719270002/x/8/
pathToGeneiousData = sys.argv[6].strip()
pathToDocker = sys.argv[8].strip()

mountPath = os.path.join(pathToGeneiousData, ":/geneious").replace("\\","/")
 
# Get latest pangolin Docker image
subprocess.run( [pathToDocker, "pull", "covlineages/pangolin"] )

# Run pangolin docker container: update pangolin + data and run fasta file from Geneious

pangoCmd = ("pangolin --update ; pangolin " + str(inFile) + " --outfile " + str(outFile))

subprocess.run( [pathToDocker, "run", "--rm" ,"-v", mountPath, \
    "covlineages/pangolin", "/bin/bash", "-c", \
    pangoCmd] ) # inFile = input all consensus fasta outFile = output pangolin .txt table