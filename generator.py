# These are the 'blank' configuration files
# which are being converted to strings

# Blank enb reading
blankEnb = open('benb.conf','r')
enbLines = blankEnb.readlines()
toFixEnb = ''
for line in enbLines:
	toFixEnb+=line
blankEnb.close()

# Blank epc reading
blankEpc = open('bepc.conf','r')
epcLines = blankEpc.readlines()
toFixEpc = ''
for line in epcLines:
	toFixEpc+=line

# Conceptual checking
#fix1 = toFix.replace('{mcc}','hello')
#fix2 = fix1.replace('{mnc}','hello1')
#fix3 = fix2.replace('{dl_earfcn}','hello2')
#fix4 = fix3.replace('{filename}','hello3')

# Lists to store known operational MNCs 
tmobile310 = ['160','260','490']
tmobile311 = ['660']
att310 = ['030','070','080','090','150','170','410','680','950']
att311 = ['070','090']
verizon310 = ['004','005','006','012']
verizon311 = ['012','480']
masterMnc310 = [tmobile310,att310,verizon310]
masterMnc311 = [tmobile311,att311,verizon311]

# Lists to store known operational EARFCNs
tmobileband = ['900','1170','1171','1172','1173','1175','2024','2025','2030','2173','2175','2557','2558','2560','2562','5035','5107','5110','5112','66511','66661','66664','66665','66811']
attband =  ['900','1170','1171','1172','1173','1175','2024','2025','2030','2173','2175','2557','2558','2560','2562','5035','5107','5110','5112','5775','5780','66511','66661','66664','66665','66811']
verizonband =  ['900','1170','1171','1172','1173','1175','2024','2025','2030','2173','2175','2557','2558','2560','2562','5230','66511','66661','66664','66665','66811']
masterBand = [tmobileband, attband, verizonband]

# Extra Variables needed
unitedStatesMcc = ['310','311']
currentMncList = []
providers = ['tmobile','att','verizon']
capitalProviders = ['TMobile','ATT','Verizon']
providerFiles = ['TMobileFiles','ATTFiles','VerizonFiles']

# Conceptual checking
#print(len(tmobileband))
#print(len(attband))
#print(len(verizonband))

for mcc in unitedStatesMcc:
	if mcc == '310':
		currentMncList = masterMnc310
	else:
		currentMncList = masterMnc311
	for i in range(3):
		counter1 = 0
		counter2 = 0
		for mnc in currentMncList[i]:
			enbFix1 = toFixEnb.replace('{mcc}','mcc = ' + mcc)
			epcFix1 = toFixEpc.replace('{mcc}','mcc = ' + mcc)
			enbFix2 = enbFix1.replace('{mnc}','mnc = ' + mnc)
			epcFix2 = epcFix1.replace('{mnc}','mnc = ' + mnc)
			for band in masterBand[i]:
				enbFix3 = enbFix2.replace('{dl_earfcn}','dl_earfcn = ' + band)
				enbFix4 = enbFix3.replace('{filename}','filename = /home/gray/IMSIpcaps/'+providers[i]+'enb_'+mcc+'_'+str(counter2)+'_'+str(counter1)+'.pcap')
				epcFix3 = epcFix2.replace('{filename}','filename = /home/gray/IMSIpcaps/'+providers[i]+'epc_'+mcc+'_'+str(counter2)+'.pcap')
				enbFix5 = enbFix4.replace('{logging}','filename = /home/gray/IMSIlogs/'+providers[i]+'enb_'+mcc+'_'+str(counter2)+'_'+str(counter1)+'.log')
				epcFix4 = epcFix3.replace('{logging}','filename = /home/gray/IMSIlogs/'+providers[i]+'epc_'+mcc+'_'+str(counter2)+'.log')
				filledEnb = open('./'+providerFiles[i]+'/'+capitalProviders[i]+'enb_'+mcc+'_'+str(counter2)+'_'+str(counter1)+'.conf','w')
				filledEpc = open('./'+providerFiles[i]+'/'+capitalProviders[i]+'epc_'+mcc+'_'+str(counter2)+'.conf','w')
				filledEnb.write(enbFix5)
				filledEpc.write(epcFix4)
				filledEnb.close()
				filledEpc.close()
				counter1 += 1
			counter1 = 0
			counter2 += 1

