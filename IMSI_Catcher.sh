#!/bin/bash
prefix = "~/.configs/srslte"
enb_configs=("AT&Tenb" "TMobileenb" "Verizonenb")
epc_configs=("AT&Tepc" "TMobileepc" "Verizonepc")
echo "Setting pwd to srslte directory"
cd ~/wireless/Project/devs/srslte/build
for i in {0..2}; do
	srsepc ${prefix epc_configs[i]} &
	epc = $! &
	srsenb ${prefix enb_configs[i]} &
	enb = $!
	sleep 45s
	kill ${epc}
	kill ${enb}
done
