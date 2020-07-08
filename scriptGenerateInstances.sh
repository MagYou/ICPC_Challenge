#!/bin/bash
#################################################################################
#     File Name           :     InstanceGenerator.py
#     Created By          :     Youcef Magnouche
#     Creation Date       :     [2020-07-07 11:00]
#     Description         :     This script calls python code to generate instances
#     Company             :     Huawei Technologies France (FRC)
#################################################################################

typeSet="Type0 Type1"
nbTunnelNodes="10 20 30 40"
nbTunnels="5 10 15 20"
nbNeighbours="3 4 5 6"

for type in $typeSet; do   # The quotes are necessary here
	for tunnelNodes in $nbTunnelNodes; do
		for tunnel in $nbTunnels; do
			for neighbour in $nbNeighbours; do
				echo "Generating instance ${type}_${tunnelNodes}_${tunnel}_${neighbour}"
	    		mkdir "${type}_${tunnelNodes}_${tunnel}_${neighbour}"
	    		py InstanceGenerator.py $type $tunnelNodes $tunnel $neighbour "${type}_${tunnelNodes}_${tunnel}_${neighbour}"
			done
		done
	done
done