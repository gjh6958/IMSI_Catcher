import os
import subprocess
import time
import os.path

# Initializes the variables to be used by the rest of the program
# This is where changes in directorys, output files, etc. should go
def init():
    prefix = "/home/gray/.config/srslte/gen/"
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
                    epcargs = ["sudo", "srsepc", epcFile]
                    epc = subprocess.Popen(epcargs, stdout=output)
                    print("\tRunning epc...")
                    enbFile = prefix + carrier + "/" + carrier + "enb_" + i + "_" + str(epcNum) + "_" + str(enbNum) + conf
                    # Loop through all enb files coorelating to the epc file
                    while( os.path.isfile(enbFile) ):
                        print("\t\tLoading enb configuration: %s" % enbFile)
                        enbargs = ["sudo", "srsenb", enbFile]
                        enb = subprocess.Popen(enbargs, stdout=output)
                        print("\t\tRunning enb...")
                        time.sleep(2) # Run for 15s
                        print("\t\tTerminating enb...")
                        enb.terminate() # Terminate the enb backround process
                        enbNum += 1
                        enbFile = prefix + carrier + "/" + carrier + "enb_" + i + "_" + str(epcNum) + "_" + str(enbNum) + conf
                    print("\tTerminating epc...")
                    epc.terminate() # Terminate the epc backgroud process
                    epcNum += 1
                    epcFile = epcCarrierPrefix + i + "_" + str(epcNum) + conf

def findIMSI(outputFile):
    IMSI = set()
    with open(outputFile, 'r') as output:
        content = output.readlines()
        for line in content:
            line = line.split(" ")
            if "IMSI:" in line:
                index = [x for x in range(len(line)) if line[x] == "IMSI:"] + 1
                IMSI.add(line[index])




initConf = init()
runConfigs(initConf[0], initConf[1], initConf[2], initConf[3], initConf[4], initConf[5])
IMSI = findIMSI(initConf[4])
if len(IMSI) == 0:
    print("No IMSIs found...")
else:
    print("IMSIs found!")
    for i in IMSI:
        print("IMSI: " + i)
