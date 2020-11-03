# ICPC_Challenge

This repository contains two sets of instances: Provisional (15 instances) and Final (50 instances). 

Each instance contains 3 csv files :

- topo.csv : this file defines the network topology. It is composed of 4 columns : 
	* LinkID: id of the link (from 0 to (number of links -1))
	* src: id of the first node of the link (between 0 and (number of nodes -1))
	* dst: id of the second node of the link (between 0 and (number of nodes -1))
	* cap: the capacity of the link in mb/s
- tunnel.csv : this file defines all sending data rates, from source agents to destination agents. It is composed of 4 columns : 
	* tunnelID: id of the tunnel (from 0 to (number of tunnels -1))
	* src: id of the source agent node (between 0 and (number of nodes -1))
	* dst: id of the destination agent node (between 0 and (number of nodes -1))
	* bandwidth: size of data (mb/s) to be sent from "src" to "dst". 
- paths.csv : this file defines all possible paths for each tunnel (source, destination, sending data rate). Each line represents a path. It is composed of 2 columns :
	* tunnelId: id of the tunnel (between 0 and (number of tunnels -1))
	* links: if of the links in the path. Links are separated by "|"

The following table gives the optimal MLU for provisional instances : 

|   |  |
| ------------- | ------------- |
|Instance|Optimal MLU|
|Instance_0|0.639732|
|Instance_2|0.78932|
|Instance_4|0.425|
|Instance_5|0.406|
|Instance_15|0.409333|
|Instance_17|0.276|
|Instance_18|0.531333|
|Instance_21|0.356|
|Instance_22|0.438563|
|Instance_33|0.442914|
|Instance_36|0.666667|
|Instance_95|0.750417|
|Instance_102|0.119584|
|Instance_139|0.158731|
|Instance_146|0.0801836|
  

The following table gives the optumal MLU for final instances : 
|   |  |
| ------------- | ------------- |
|Instance|Optimal MLU|
|Instance_1|0.145047|
|Instance_3|0.343488|
|Instance_6|0.333333|
|Instance_7|0.563333|
|Instance_8|0.318|
|Instance_9|0.357333|
|Instance_10|0.367333|
|Instance_11|0.552667|
|Instance_12|0.207|
|Instance_13|0.299667|
|Instance_14|0.326667|
|Instance_16|0.589|
|Instance_19|0.502667|
|Instance_20|0.691333|
|Instance_23|0.238735|
|Instance_24|0.515599|
|Instance_25|0.381458|
|Instance_26|0.219164|
|Instance_27|0.320902|
|Instance_28|0.32546|
|Instance_29|0.415167|
|Instance_30|0.279159|
|Instance_31|0.288692|
|Instance_32|0.389243|
|Instance_34|0.238391|
|Instance_37|0.06|
|Instance_38|0.166667|
|Instance_39|0.0379176|
|Instance_74|0.23645|
|Instance_76|0.409942|
|Instance_78|0.337512|
|Instance_80|0.498126|
|Instance_82|0.369846|
|Instance_84|0.152391|
|Instance_86|0.104623|
|Instance_88|0.322512|
|Instance_90|0.230486|
|Instance_92|0.40457|
|Instance_96|0.538986|
|Instance_98|0.400757|
|Instance_100|0.126483|
|Instance_104|0.142943|
|Instance_106|0.125122|
|Instance_108|0.127883|
|Instance_110|0.113636|
|Instance_112|0.176947|
|Instance_114|0.138041|
|Instance_116|0.0858855|
|Instance_159|0.171075|
|Instance_167|0.836829|

  Contact : 
Youcef Magnouche
Email : youcef.magnouche@huawei.com
