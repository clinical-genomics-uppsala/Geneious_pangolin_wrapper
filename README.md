# Geneious wrapper plugin for Pangolin

[Geneious](https://www.geneious.com) wrapper plugin to run [Pangolin](https://cov-lineages.org/resources/pangolin.html) to assign pango lineages to SARS-CoV-2 genomes. The plugin downloads the latest docker image for pangolin and also checks for updates each time it is run.

- Input: SARS-CoV-2 genome sequence(s). To run on multiple sequences, first create a sequence list in Geneious.
- Output: .txt report which is imported into Geneious

## System requirements
- Geneious 2021.1.1 or later (for older versions it may be possible to install the plugin from source)
- Python 3
- Docker Desktop

## Mac or linux
1. Download `pangolin_linux_mac_x.x.gplugin`
2. In Geneious, go to 'Tools' --> 'Plugins' --> 'Install plugin from a gplugin file' and select the gplugin file and click 'Install'. The plugin should now appear under the 'Tools' menu.
3. When running the plugin the user will be prompted to enter the path to Docker (for example: `/usr/local/bin/docker`) and the path to where Geneious stores temporary data (for example: `/Users/yourusername/Geneious 2022.2 Data/transient`).

## Windows
1. Download `pangolin_windows_x.x.gplugin`
2. In Geneious, go to 'Tools' --> 'Plugins' --> 'Install plugin from a gplugin file' and select the gplugin file and click 'Install'. The plugin should now appear under the 'Tools' menu.
3. When running the plugin the user will be prompted to enter the path to Docker (for example: `C:\Program Files\Docker\Docker\resources\bin\docker.exe`) and the path to where Geneious stores temporary data (for example: `C:\Geneious 2022.2 Data\transient`).  
<br />
<br />
## Installation from source

First install the [Geneious Wrapper Plugin Creator](https://www.geneious.com/api-developers/).

### Create wrapper plugin in Geneious
1. Go to 'File' --> 'Create/Edit Wrapper Plugin..'. Press '+New'
2. Step 1: 
	- Fill in 'Plugin Name:' and 'Menu/Button Text:' of your choice. 
	- 'Plugin Type:' select 'General Operation'. 
	- 'Bundled Program Files (optional)'
		- Linux/mac: add the `pangolin_linux_mac.py` script under 'Linux' or 'Mac OSX' respectively.
		- Windows: add the `pangolin_win.bat` script under 'Windows' and the `pangolin_win.py` script under 'Additional Bundled Files'.
3. Step 2: 
	- 'Sequence Type:' select 'Nucleotide only'.
	- 'Document Type:' select 'Unanaligned Sequences (1+)'.
	- 'Command Line'
		- Windows: '[inputFileNames] pangolin [otherOptions]' 
		- Linux/Mac: '-i [inputFileNames] -o pangolin [otherOptions]'
	- Under 'Output' 'File Name:' fill in 'pangolin' and select 'Format:' 'Text file (plain)'
4. Step 3:
	Press 'Add' to add two user options (in this order):   
	- 'Command Line Switch': pathToDocker, 'Option Label': Docker path  
	- 'Command Line Switch': pathToData, 'Option Label': Data path  
	Both 'Command Line Switch' and 'Option Label' should be filled in, but can be modified.
