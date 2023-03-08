:: Path to current directory to bundled optional files
set pypath=%~dp0

:: Input/output from Geneious
set input=%1
set output=%2

:: Options from Geneious
set docker=%4
set temp=%6

python "%pypath%pangolin_win.py" -i %input% -o %output% -d %docker% -t %temp%
