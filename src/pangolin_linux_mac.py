#!/usr/bin/env python3

import sys
import os
import re
import subprocess

# Geneious input/output and options
inFile = os.path.join("/geneious", sys.argv[2])
outFile = os.path.join("/geneious", sys.argv[4])

pathToDocker = sys.argv[6]
pathToGeneiousData = sys.argv[8]

# Find path to temporary Geneious folder - folders named with largest numbers
# Example: /Users/user/Geneious 2022.1 Data/transient/1660719270002/x/8/
def getTaskPath(path):
    sessionDirs = os.listdir(path)
    sessions = [int(s) for s in sessionDirs if re.search('^([0-9]{13,13}){1}$', s)]
    sessionsSort = sorted(sessions, reverse=True)
    session = str(sessionsSort[0])

    taskDirsPath = os.path.join(path, session, "x")
    taskDirs = os.listdir(taskDirsPath)
    tasks = [int(t) for t in taskDirs if re.search('^([0-9]{1,5}){1}$', t)]
    tasksSort = sorted(tasks, reverse=True)
    task = str(tasksSort[0])

    taskPath = os.path.join(taskDirsPath, task, ":/geneious")

    return taskPath


# Get latest pangolin Docker image
subprocess.run( [pathToDocker, "pull", "covlineages/pangolin"] )

# Run pangolin docker container: update pangolin + data and run fasta file from Geneious

mountPath = getTaskPath(pathToGeneiousData)
pangoCmd = ("pangolin --update ; pangolin " + str(inFile) + " --outfile " + str(outFile))

subprocess.run( [pathToDocker, "run", "--rm" ,"-v", mountPath, \
    "covlineages/pangolin", "/bin/bash", "-c", \
    pangoCmd] ) # inFile = input all consensus fasta outFile = output pangolin .txt table
