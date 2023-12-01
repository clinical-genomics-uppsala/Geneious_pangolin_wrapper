:: Path to current directory to bundled optional files
set pluginPath=%~dp0

:: Input/output from Geneious
set inFile=%2
set outFile=%4

:: Options from Geneious
set pathToGeneiousData=%6
set pathToDocker=%8
set docker=%4
set temp=%6

python "%pluginPath%pangolin.py" -i %inFile% -o %outFile% -t %pathToGeneiousData% -d %pathToDocker% 

:: Geneious command: -i [inputFileNames] -o pangolin -g [inputFolderName] [otherOptions]