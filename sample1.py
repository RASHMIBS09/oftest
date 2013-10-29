import json
import os
from pprint import pprint
target_dir="../ofreport"
full_path=os.path.join(target_dir,'feature.json')
json_data=open(full_path)
data = json.load(json_data)
matching={}
if(data["OFPAT_OUTPUT"]):
	matching["OFPAT_OUTPUT"]={}
        matching["OFPAT_OUTPUT"]["0"]="Grp100No100"
	matching["OFPAT_OUTPUT"][1]="Grp100No120"
	matching["OFPAT_OUTPUT"][2]="Grp100No150"
	matching["OFPAT_OUTPUT"][3]="Grp40No50"
	matching["OFPAT_OUTPUT"][4]="Grp40No60"
	#"Grp100No100,Grp100No120,Grp100No150,Grp40No50,Grp40No60,"


if(data["OFPAT_SET_DL_DST"]):
	matching["OFPAT_SET_DL_SRC"]={}
	matching["OFPAT_SET_DL_SRC"]="Grp70No180"
		



#matching= matching + "Grp70No180,"

if(data["OFPAT_SET_DL_SRC"]):
	matching["OFPAT_SET_DL_SRC"]={}
	matching["OFPAT_SET_DL_SRC"]="Grp70No170"


#	matching= matching + "Grp70No170,"

if(data["OFPAT_SET_NW_DST"]):
	matching["OFPAT_SET_NW_DST"]={}
	matching["OFPAT_SET_NW_DST"][0]={}

#	matching= matching + "Grp70No200,"
	
if(data["OFPAT_SET_NW_TOS"]):
	matching["OFPAT_SET_NW_TOS"]={}
	matching["OFPAT_SET_NW_TOS"][0]="Grp70No210"
	
#	matching= matching + "Grp70No210,"
	
if(data["OFPAT_SET_TP_DST"]):
	matching["OFPAT_SET_TP_DST"]={}
	matching["OFPAT_SET_TP_DST"][0]="Grp70No230"

#	matching= matching + "Grp70N0230,"

if(data["OFPAT_SET_TP_SRC"]):
	matching["OFPAT_SET_TP_SRC"]={}
	matching["OFPAT_SET_TP_SRC"][0]="Grp70No220"

#	matching= matching + "Grp70No220,"

if(data["OFPAT_SET_VLAN_PCP"]):
	matching["OFPAT_SET_VLAN_PCP"]={}
	matching["OFPAT_SET_VLAN_PCP"]="Grp70No140"



#	matching= matching + "Grp70No140,"

if(data["OFPAT_SET_VLAN_VID"]):
	matching["OFPAT_SET_VLAN_VID"]={}
	matching["OFPAT_SET_VLAN_VID"][0]="Grp70No120"
	matching["OFPAT_SET_VLAN_VID"][1]="Grp70No130"
	matching["OFPAT_SET_VLAN_VID"][2]="Grp70NO250"


#	matching= matching + "Grp70No120,Grp70No130,Grp70No250,"

if(data["OFPAT_STRIP_VLAN"]):
	matching["OFPAT_STRIP_VLAN"]={}
	matching["OFPAT_STRIP_VLAN"][0]="Grp70No160"


#	matching= matching + "Grp70No160,"

if(data["OFPC_ARP_MATCH_IP"]):
	matching["OFPC_ARP_MATCH_IP"]={}
	matching["OFPC_ARP_MATCH_IP"][0]="Grp50No210"
	matching["OFPC_ARP_MATCH_IP"][1]="Grp50No220"

#	matching= matching + "Grp50No210,Grp50No220,"

if(data["OFPC_FLOW_STATS"]):
	matching["OFPC_FLOW_STATS"]={}
	matching["OFPC_FLOW_STATS"][0]="Grp60No10"
	matching["OFPC_FLOW_STATS"][1]="Grp60No20"
	matching["OFPC_FLOW_STATS"][2]="Grp60No30"
	matching["OFPC_FLOW_STATS"][3]="Grp60No40"

#	matching= matching + "Grp60No10,Grp60No20,Grp60No30,Grp60No40,"

if(data["OFPC_IP_REASM"]):
	matching["OFPC_IP_REASM"]={}
	matching["OFPC_IP_REASM"][0]="Grp80No230"
	matching["OFPC_IP_REASM"][1]="Grp80NoNo270"
	matching["OFPC_IP_REASM"][2]="Grp80No300"

#	matching= matching + "Grp80No230,Grp80No270,Grp80No300,"

if(data["OFPC_PORT_STATS"]):
	matching["OFPC_PORT_STATS"]={}
	matching["OFPC_PORT_STATS"][0]="Grp60No60"
	matching["OFPC_PORT_STATS"][1]="Grp60No70"
	matching["OFPC_PORT_STATS"][2]="Grp60No80"
	matching["OFPC_PORT_STATS"][3]="Grp60No90"
	matching["OFPC_PORT_STATS"][4]="Grp60No100"
	matching["OFPC_PORT_STATS"][5]="Grp60No110"
	matching["OFPC_PORT_STATS"][6]="Grp60No120"
	matching["OFPC_PORT_STATS"][7]="Grp60No130"
	matching["OFPC_PORT_STATS"][8]="Grp60No140"
	matching["OFPC_PORT_STATS"][9]="Grp60No150"
	matching["OFPC_PORT_STATS"][10]="Grp60No160"
	
	

#	matching= matching + "Grp90No110,"

if(data["OFPC_QUEUE_STATS"]):
	matching["OFPC_QUEUE_STATS"]={}
	matching["OFPC_QUEUE_STATS"][0]="Grp60No170"
	matching["OFPC_QUEUE_STATS"][1]="Grp60No180"
	matching["OFPC_QUEUE_STATS"][2]="Grp60No190"


#	matching= matching + "Grp100No190,Grp100No290,"

if(data["OFPC_STP"]):
	matching["OFPC_STP"]={}
	matching["OFPC_STP"][0]="Grp30No120"

#	matching= matching + "Grp30No120"

if(data["OFPC_TABLE_STATS"]):
	matching["OFPC_TABLE_STATS"]={}
	matching["OFPC_TABLE_STATS"]="Grp60No200"
	matching["OFPC_TABLE_STATS"]="Grp60No210"

target_dir="../ofreport"
full_path=os.path.join(target_dir,'matching.json')
f=open(full_path, "w")
f.write(json.dumps(matching))
f.close



"""
write_path=os.path.join(target_dir,'matchingtestcases.txt')
text_file = open(write_path , "w")
text_file.write(" %s"%matching)
text_file.close()

json_data.close()

"""
