import json
import os
from pprint import pprint
target_dir="../ofreport"
full_path=os.path.join(target_dir,'feature.json')
json_data=open(full_path)
data = json.load(json_data)

if(data["OFPAT_OUTPUT"]):
	matching="Grp100No100,Grp100No120,Grp100No150,Grp40No50,Grp40No60,"

if(data["OFPAT_SET_DL_DST"]):
	matching= matching + "Grp70No180,"

if(data["OFPAT_SET_DL_SRC"]):
	matching= matching + "Grp70No170,"

if(data["OFPAT_SET_NW_DST"]):
	matching= matching + "Grp70No200,"
	
if(data["OFPAT_SET_NW_TOS"]):
	matching= matching + "Grp70No210,"
	
if(data["OFPAT_SET_TP_DST"]):
	matching= matching + "Grp70N0230,"

if(data["OFPAT_SET_TP_SRC"]):
	matching= matching + "Grp70No220,"

if(data["OFPAT_SET_VLAN_PCP"]):
	matching= matching + "Grp70No140,"

if(data["OFPAT_SET_VLAN_VID"]):
	matching= matching + "Grp70No120,Grp70Np130,Grp70No250,"

if(data["OFPAT_STRIP_VLAN"]):
	matching= matching + "Grp70No160,"

if(data["OFPC_ARP_MATCH_IP"]):
	matching= matching + "Grp50No210,Grp50No220,"

if(data["OFPC_FLOW_STATS"]):
	matching= matching + "Grp60No10,Grp60No20,Grp60No30,Grp60No40,"

if(data["OFPC_IP_REASM"]):
	matching= matching + "Grp80No230,Grp80No270,Grp80No300,"

if(data["OFPC_PORT_STATS"]):
	matching= matching + "Grp90No110,"

if(data["OFPC_QUEUE_STATS"]):
	matching= matching + "Grp100No190,Grp100No290,"

if(data["OFPC_STP"]):
	matching= matching + "Grp30No120"

write_path=os.path.join(target_dir,'matchingtestcases.txt')
text_file = open(write_path , "w")
text_file.write(" %s"%matching)
text_file.close()

json_data.close()
