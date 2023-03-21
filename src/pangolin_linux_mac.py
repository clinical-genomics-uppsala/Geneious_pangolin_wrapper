#!/usr/bin/env python3

# This script runs the nextclade analysis on sequencing data. 
# It can either be directily run in the terminal (command: python nc_terminal.py <sequence data> <batch name>)
# or it can be used as a plugin in Geneious. 

# Variables to be updates for each individual computer:
    # 1. path (leave as an empty string if this will be used as a Geneious plugin)
    # 2. output_path
    # 3. nextclade_path

import os
import subprocess
import sys
import json
import csv
from datetime import date
from os import listdir
from os.path import isfile, join

def terminal(var_name):
    output, error= subprocess.Popen(var_name, universal_newlines=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    return output

def slash_correct(path, symbol):
    correct_path = path.replace("\\", symbol)
    return correct_path

# obtain today's date for the folder name
today = str(date.today())
today = today.replace("-", "_")


infile=sys.argv[1]      # The selected sequences to analyse in Geneious
batch_name=sys.argv[2]  # Name of the batch. Can be modified in Geneious.

# If this is to be run in genious, variable "path" should be left as an empty string. If run in terminal, update it to where you want everything to be run.
path=""

# This is the path where all nextclade's output files should be saved.
output_path=sys.argv[6]
output_path=slash_correct(output_path, "/")

# Correct end by adding / if necessary 
if (output_path[-1] != "/"):
    output_path+="/"

nextclade_name= "nextclade_analysis_{}".format(today)

# get a list of folders present in output_path
onlyfiles = [f for f in listdir(output_path) if os.path.isdir(join(output_path, f))]

counter = 1

#if nextcalde_name already exists, the name is updated with a counter until it's unique. 
while nextclade_name in onlyfiles:
    nextclade_name="nextclade_analysis_{}_{}".format(today,str(counter))
    counter +=1
    onlyfiles = [f for f in listdir(output_path) if os.path.isdir(join(output_path, f))]

# the path to where all files will end up
output_permanent = output_path+nextclade_name

# Path to where nextclade is installed.
nextclade_path=sys.argv[4]
nextclade_path=slash_correct(nextclade_path, "/")

output=path+"output/"   #Path to where your results should be saved.

# Path to where you want to store your downloaded database.
# If you already have a database up-to-date, this step will be skipped.
database_path=path+"data/sars-cov-2" 

get_data=[nextclade_path, "dataset", "get", "--name=sars-cov-2", "--output-dir={}".format(database_path)]
get_data_permanent=[nextclade_path, "dataset", "get", "--name=sars-cov-2", "--output-dir={}database/".format(output_permanent)]
run_nextclade=[nextclade_path, "run", "--in-order", "--input-dataset", "{}".format(database_path), "--output-all={}".format(output), "--output-basename={}".format(batch_name), "{}".format(infile)]

terminal(get_data)
terminal(run_nextclade)
#terminal(get_data_permanent)


# Save software and database info

#open the json-file
f = open(database_path+"/tag.json")

#convert the json-file to a dict
data = json.load(f)

#r.write(("Database version: {}").format(data['tag']))

r = open("{}{}_final.csv".format(output, batch_name), 'w', newline='')
writer = csv.writer(r)

nextclade_vers = [nextclade_path, "--version"]

output_results2  = terminal(nextclade_vers)

with open('{}{}.csv'.format(output,batch_name), 'r') as csvfile:
     spamreader = csv.reader(csvfile, delimiter=";")
     for row in spamreader:
         if "seqName" in row[0]:
             row.append("Software version")
             row.append("Database version")
             writer.writerow(row)
         else:
             row.append(output_results2)
             row.append(data['tag'])
             writer.writerow(row)
         
f.close()
r.close()

# Copy all files from the temporary Geneious file to a new permanent file.
copy_files=["cp", "-a", "{}.".format(output), "{}".format(output_permanent)]


terminal(copy_files)
