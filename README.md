# IMSI_Catcher
This repository is used to store code and configurationes used to complete a CSEC 469 final project at RIT.  The shell script uses given configuration files to configure an SDR to mimic a cell tower from all three major U.S. carriers.  Any phones carried by AT&T, T-Mobile, or Verizon within range of the SDR will give away their IMSI numbers.

# Pre-requisites
- USRP B210 SDR or other similar SDR
- Correct SDR drivers, UHD drivers for B210
- srsLTE installation and build

# What the files do
- IMSI.py: Runs srsENB and srsEPCs to mimic towers contained within the configuration directorys.
- config/gen: All possible configurations for all major carriers within the U.S.
- config/POC: Configuration files used for proof of concept for the project write up
- generator.py: generates all possible configuration files
- benb.conf: file needed for generator.py to run
- bepc.conf: file needed for generator.py to run

# Installation
Installation of this project is simple.  Pull the project and move the configuration files to your srslte configuration directory.  Change directory declerations within the script as needed to fit your enviornment.  Generation of configuration files to fit your specific enviornment is also recommended.

# Running
Simply run the shell script as a super user.

# Disclaimer
The contributers of this repository are not responsible for how members of the public use this repository.  RUNNING THIS SCRIPT WITHOUT PROPER PROTECTIONS IS ILLEGAL UNDER U.S. FEDERAL LAW.
