import time
import sys

import unittest
import random
import os
from oftest import config
import oftest.controller as controller
import oftest.cstruct as ofp
import oftest.message as message
import oftest.dataplane as dataplane
import oftest.action as action
import oftest.parse as parse
import oftest.base_tests as base_tests
import oftest.illegal_message as illegal_message
import json
from oftest.oflog import *
from oftest.testutils import *
from time import sleep
from FuncUtils import *
from functools import partial
from collections import defaultdict


class Grp110No10(base_tests.SimpleProtocol):
        """ Send Features_Request to the switch from the controller 
            and Verify the Features_Reply and redirect that to json 
            file.
        """
 
	#@wireshark_capture
 	def runTest(self):
   	    logging=get_logger()
	    of_ports = config["port_map"].keys()
     	    of_ports.sort()
	    self.assertTrue(len(of_ports) > 1, "No Enough Ports")
            
           
            #Sending Features_Request
 	    logging.info("Sending features_request...")
 	    request = message.features_request()
	    (reply , pkt) = self.controller.transact(request)
	    self.assertTrue(reply is not None, "Failed to get Features_Reply Message")
	    self.assertEqual(reply.header.type ,ofp.OFPT_FEATURES_REPLY, " Response is not features Reply")
 	    self.assertEqual(reply.header.xid,request.header.xid, "Transaction ID doesnot match")

            #Capabilities
    	    format(bin(reply.capabilities))
	    features={}
	    # tripledict = partial(defaultdict, partial(defaultdict, dict))
	    # features = tripledict()
	    features_port={}

            if(reply.actions &1<<ofp.OFPAT_OUTPUT):
            	features['OFPAT_OUTPUT']=True
	    else:
		features['OFPAT_OUTPUT']=False  

	    if(reply.actions &1<<ofp.OFPAT_SET_VLAN_VID):
		features['OFPAT_SET_VLAN_VID']=True
	    else:
		features['OFPAT_SET_VLAN_VID']=False
	
	    if(reply.actions &1<<ofp.OFPAT_SET_VLAN_PCP):
		features['OFPAT_SET_VLAN_PCP']=True
	    else:
		features['OFPAT_SET_VLAN_PCP']=False
		
	    if(reply.actions &1<<ofp.OFPAT_STRIP_VLAN):
		features['OFPAT_STRIP_VLAN']=True
	    else:
		features['OFPAT_STRIP_VLAN']=False

	    if(reply.actions &1<<ofp.OFPAT_SET_DL_SRC):
		features['OFPAT_SET_DL_SRC']=True
	    else:
		features['OFPAT_SET_DL_SRC']=False

	    if(reply.actions &1<<ofp.OFPAT_SET_DL_DST):
		features['OFPAT_SET_DL_DST']=True
	    else:
		features['OFPAT_SET_DL_DST']=False
	
      	    if(reply.actions &1<<ofp.OFPAT_SET_NW_DST):
		features['OFPAT_SET_NW_DST']=True
	    else:
		features['OFPAT_SET_NW_DST']=False

	    if(reply.actions &1<<ofp.OFPAT_SET_NW_TOS):
		features['OFPAT_SET_NW_TOS']=True
	    else:
		features['OFPAT_SET_NW_TOS']=False
    
            if(reply.actions &1<<ofp.OFPAT_SET_TP_SRC):
		features['OFPAT_SET_TP_SRC']=True
	    else:
		features['OFPAT_SET_TP_SRC']=False
            if(reply.actions &1<<ofp.OFPAT_SET_TP_DST):
		features['OFPAT_SET_TP_DST']=True
	    else:
		features['OFPAT_SET_TP_DST']=False

            if(reply.actions &1<<ofp.OFPAT_SET_TP_DST):
		features['OFPAT_SET_TP_DST']=True
	    else:
		features['OFPAT_SET_TP_DST']=False 
            if(reply.actions &1<<ofp.OFPAT_ENQUEUE):
		features['OFPAT_ENQUEUE']=True
	    else:
		features['OFPAT_ENQUEUE']=False




            if(reply.capabilities & ofp.OFPC_FLOW_STATS):
		features['OFPC_FLOW_STATS']=True
            else:
  	 	features['OFPC_FLOW_STATS']=False
	   
            if(reply.capabilities & ofp.OFPC_TABLE_STATS):
		features['OFPC_TABLE_STATS']=True
	    else:
		features['OFPC_TABLE_STATS']=False
	   
	    if(reply.capabilities & ofp.OFPC_PORT_STATS):
		features['OFPC_PORT_STATS']=True
	    else:
		features['OFPC_PORT_STATS']=False

	    if(reply.capabilities & ofp.OFPC_STP):
		suppported_capabilities['OFPC_STP']=True
  	    else:
		features['OFPC_STP']=False
	 
	    if(reply.capabilities & ofp.OFPC_RESERVED):
		features['OFPC_RESERVED']=True
  	    else:
		features['OFPC_RESERVED']=False
	    
  	    if(reply.capabilities & ofp.OFPC_IP_REASM):
		supported_capabilites['OFPC_IP_REASM']=True
	    else:
		features['OFPC_IP_REASM']=False
	    
	    if(reply.capabilities & ofp.OFPC_QUEUE_STATS):
		features['OFPC_QUEUE_STATS']=True
	    else:
		features['OFPC_QUEUE_STATS']=False

	    if(reply.capabilities & ofp.OFPC_ARP_MATCH_IP):
		features['OFPC_ARP_MATCH_IP']=True
	    else:
		features['OFPC_ARP_MATCH_IP']=False
	    
	    
	    
	    if(reply.datapath_id !=0 ):
		features['datapath_id']=True
	    else:
		features['datapath_id']=False

            
	
            features['buffer_size']= str(reply.n_buffers)
	        
	    features['No_of_Tables']= str(reply.n_tables)

	    features['No_of_Ports']=len(reply.ports)
	    
	
	    for x in range(0,len(reply.ports)):
		    features_port[x]={}
		    features_port[x]['port_no']=reply.ports[x].port_no
		    features_port[x]['Port_hw_addr']=str(reply.ports[x].hw_addr)
		    features_port[x]['Port_name']=reply.ports[x].name
		    features_port[x]['Port_config']=reply.ports[x].config
		    features_port[x]['Port_state']=reply.ports[x].state
		    features_port[x]['Port_curr']=reply.ports[x].curr
		    features_port[x]['Port_advertised']=reply.ports[x].advertised
		    features_port[x]['Port_supported']=reply.ports[x].supported
		    features_port[x]['Port_peer']=reply.ports[x].peer

           
 	    target_dir="../ofreport/jsonffiles/"
	    full_path=os.path.join(target_dir,'feature.json')
	    full_path_port=os.path.join(target_dir,'featureport.json')
	    f=open(full_path, "w")
	    f.write(json.dumps(features))
	    f.close	
	    fd=open(full_path_port, "w")
	    fd.write(json.dumps(features_port))
	    fd.close
	   




class Grp110No20(base_tests.SimpleDataPlane):

  	"""
  	Verify port mapping.
  	Check if the dataplane port on which the packet is being sent is the port
  	on which the packet is received
  	"""

	
	def runTest(self):
		logging = get_logger()
		of_ports = config["port_map"].keys()
		of_ports.sort()
		

		rc = delete_all_flows(self.controller)
		self.assertEqual(rc, 0, "Failed to delete all flows")
		self.assertEqual(do_barrier(self.controller), 0, "Barrier failed")

		logging.info("Sending a Simple tcp packet a dataplane port")
		logging.info("Expecting a packet_in event on the control plane")

		pkt = simple_tcp_packet()
		for x in range(4):
			self.dataplane.send(of_ports[x], str(pkt))
			print "Sending packet to dp port " + str(of_ports[x]) 
			print "Expecting packet on port " +str(of_ports[x])
			     
			(response,pkt) = self.controller.poll(exp_msg=ofp.OFPT_PACKET_IN,timeout=2)
			try:

				if(str(of_ports[x]) != str(response.in_port)):
					print "PORT MAPPING MISMATCH:Packet received on different port" +str(response.in_port)
                        	else:                                                                                        
                	        	print "Packet received on expected port " +str(response.in_port)
			except:
				pass







#Port Stats

class Grp110No30(base_tests.SimpleDataPlane):
	
	"""
	Send a port_stats request and
	redirect the port_stats reply to a json file
	"""
	def runTest(self):
		port_stats={}
		logging = get_logger()
		

		of_ports = config["port_map"].keys()
		of_ports.sort()
		self.assertTrue(len(of_ports) > 1, "Not enough ports for test")
		
		#Clear switch state
		rv = delete_all_flows(self.controller)
		self.assertEqual(rv, 0, "Failed to delete all flows")

		        
        	
        	(counter)=get_portstats(self,of_ports[1])
		
		
		port_stats['received_packets']=counter[0] #No of received packets
		port_stats['transmitted_packets']=counter[1] # No of transmitted packets
		port_stats['received_bytes']=counter[2]# No of received bytes
		port_stats['transmitted_bytes']=counter[3] # No of transmitted bytes
		port_stats['packetsdropped_rx']=counter[4]# No of packets dropped rx
		port_stats['packetsdropped_tx']=counter[5] # No of packets dropped tx
		port_stats['receive_errors']=counter[6] # No of receive errors
		port_stats['transmit_errors']=counter[7] # No of transmit errors
		port_stats['framealignment_errors']=counter[8] # No of frame alignment errors
		port_stats['packetsRX_overrun']=counter[9] # No of packets with RX overrun
		port_stats['CRC_errors']=counter[10] # No of CRC errors
		port_stats['collisions']=counter[11] # No of collisions
                port_stats['transmission_errors']=counter[12] # No of Transmission errors
 
		
 	    	target_dir="../ofreport/jsonfiles/"
	    	full_path=os.path.join(target_dir,'portstats.json')
		f=open(full_path, "w")
	    	f.write(json.dumps(port_stats))
	    	f.close




# FLOW STATS

class Grp110No40(base_tests.SimpleDataPlane):
	
	"""
	Send flow_stats request and redirect the flow_stats reply to a json file
	"""
	


	def runTest(self):
		port_stats={}

             	of_ports = config["port_map"].keys()
		of_ports.sort()
		self.assertTrue(len(of_ports) > 1, "Not enough ports for test")
		
		#Clear switch state
		rv = delete_all_flows(self.controller)
		self.assertEqual(rv, 0, "Failed to delete all flows")
		
		(pkt,match) = wildcard_all_except_ingress(self,of_ports)
       
        	#Send Packets matching the flow 
        	num_pkts=5
        	for pkt_cnt in range(num_pkts):
            		self.dataplane.send(of_ports[0],str(pkt))
		
		flow_stats={}
		(reply)=get_flowstats(self,match)
                flow_stats['length']=reply.stats[0].length
		flow_stats['table_id']=reply[0].stats[0].table_id
		flow_stats['duration_sec']=reply[0].stats[0].duration_sec
		flow_stats['duration_nsec']=reply[0].stats[0].duration_nsec
		flow_stats['priority']=reply[0].stats[0].priority
		flow_stats['idle_timeout']=reply[0].stats[0].idle_timeout
		flow_stats['hard_timeout']=reply[0].stats[0].hard_timeout
		flow_stats['cookie']=reply[0].stats[0].cookie
		flow_stats['packet_count']=reply[0].stats[0].packet_count
		flow_stats['byte_count']=reply[0].stats[0].byte_count
		flow_stats['match_in_port']=reply[0].stats[0].match.in_port
		#flow_stats['match dl_src']=reply[0].stats[0].match.dl_src[OFP_ETH_ALEN]
		#flow_stats['match dl_dst']=reply[0].stats[0].match.dl_dst[OFP_ETH_ALEN]
		flow_stats['match_dl_vlan']=reply[0].stats[0].match.dl_vlan
		flow_stats['match_dl_vlan_pcp']=reply[0].stats[0].match.dl_vlan_pcp
		flow_stats['match_dl_type']=reply[0].stats[0].match.dl_type
		flow_stats['match_nw_src']=reply[0].stats[0].match.nw_src
		flow_stats['match_nw_dst']=reply[0].stats[0].match.nw_dst
		flow_stats['match_tp_src']=reply[0].stats[0].match.tp_src
		flow_stats['match_tp_dst']=reply[0].stats[0].match.tp_dst
		flow_stats['match_nw_tos']=reply[0].stats[0].match.nw_tos
		flow_stats['match_nw_proto']=reply[0].stats[0].match.nw_proto
	
		
 	   	target_dir="../ofreport/jsonfiles/"
	    	full_path=os.path.join(target_dir,'flowstats.json')
		f=open(full_path, "w")
	    	f.write(json.dumps(flow_stats))
	    	f.close

# TABLE STATS

class Grp110No50(base_tests.SimpleDataPlane):

	"""
	Send table_stats request to the switch and direct the table_stats reply to a json file
	
	"""

	def runTest(self):
		logging = get_logger()
		logging.info("Running Grp60No200 Active Counter test")

		of_ports = config["port_map"].keys()
		of_ports.sort()
		self.assertTrue(len(of_ports) > 1, "Not enough ports for test")
		 
		#Clear Switch state
		rv = delete_all_flows(self.controller)
		self.assertEqual(rv, 0, "Failed to delete all flows")

		logging.info("Installing a flow entry matching on in_port=ingress_port,action = output to egress_port T ")
	       

		#Insert a flow with match on all ingress port
		
		(pkt,match) = wildcard_all_except_ingress(self,of_ports)
       
        	#Send Packets matching the flow 
        	num_pkts=5
        	for pkt_cnt in range(num_pkts):
            		self.dataplane.send(of_ports[0],str(pkt))


		(reply) = get_tablestats(self)
		table_stats={}
                
                table_stats['lookup_count']=reply[0]
                table_stats['matched_count']=reply[1]
                table_stats['active_count']=reply[2]


	        
 	    	target_dir="../ofreport/jsonfiles/"
	    	full_path=os.path.join(target_dir,'tablestats.json')
                f=open(full_path, "w")
                f.write(json.dumps(table_stats))
                f.close




