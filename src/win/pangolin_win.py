import os
import re
import sys
import subprocess

# Geneious input/output
inFile = os.path.join("/geneious", sys.argv[2]).replace("\\","/") # From .bat script
outFile = os.path.join("/geneious", sys.argv[4]).replace("\\","/") # From .bat script

pathToDocker = sys.argv[6].strip()
pathToGeneiousData = sys.argv[8].strip()


# Find path to temporary Geneious folder - folders named with largest numbers
# Example: C:/Geneious 2021.1 Data/transient/1660719270002/x/8/
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

    taskPath = os.path.join(taskDirsPath, task, ":/geneious").replace("\\","/")

    return taskPath
  

# Get latest pangolin Docker image
subprocess.run( [pathToDocker, "pull", "covlineages/pangolin"] )

# Run pangolin docker container: update pangolin + data and run fasta file from Geneious

mountPath = getTaskPath(pathToGeneiousData)
pangoCmd = f'pangolin --update ; pangolin {inFile} --outfile {outFile}'

subprocess.run( [pathToDocker, "run", "--rm" ,"-v", mountPath, \
    "covlineages/pangolin", "/bin/bash", "-c", \
    pangoCmd] ) # inFile = input all consensus fasta outFile = output pangolin .txt table