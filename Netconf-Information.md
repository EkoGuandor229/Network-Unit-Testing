# Netconf information

## Basic Information

The Network Configuration Protocol provides operations to CRUD configurations of network devices. It is located on top of a Remote Procedure Call (RPC) layer.
Netconf uses XML based encoding for the config data and the protocol messages which are exchanged over a secure transport protocol.
It can basically be partitioned into four layers:
1. Content - Configuration and notification data
2. Operations - Definitions on how to fetch and edit configuration data
3. Messages - Mechanism for RPC and notifications
4. Secure Transport - Encrypted Client - Server messaging 

## Operations

The protocols defines a few standard protocol operations which can be extended. 
For the project, the following operations should be the most interesting

Operation | Description
--------- | -----------
get       | retrieve running Configuration and device state information
get-config | Retrieve all or parto of a specified configuration datastore
close-session | Request the termination of the NETCONF session

