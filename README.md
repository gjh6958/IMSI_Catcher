# IMSI_Catcher
This repository is used to store code and configurationes used to complete my CSEC 469 final project at RIT.  The shell script uses given configuration files to configure an SDR to mimic a cell tower from all three major U.S. carriers.  Any phones carried by AT&T, T-Mobile, or Verizon within range of the SDR will give away their IMSI numbers.

# Pre-requisites
- USRP B210 SDR or other similar SDR
- Correct SDR drivers, UHD drivers for B210
- srsLTE installation and build

# Installation
Installation of this project is simple.  Pull the project and move the configuration files to your srslte configuration directory.  Change directory declerations within the script as needed to fit your enviornment.

# Running
Simply run the shell script as a super user, total execution time is around 2m 30s.
