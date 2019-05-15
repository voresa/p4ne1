from pysnmp.hlapi import *

result = getCmd(SnmpEngine(),
	CommunityData(community_name, mpModel=0),
	UdpTransportTarget((ipaddr_string, port_int)),
	ContextData(),
	ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

result2 = nextCmd (SnmpEngine(),
	CommunityData(community_name, mpModel=0),
	UdpTransportTarget((ipaddr_string, port_int)),
	ContextData(),
	ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
    lexicographicMode=False) # Не идти в глубину


#snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0) # По имени MIB-переменной

#snmp_object = ObjectIdentity('1.3.6.1.2.1.2.2.1.2') # По значению MIB-переменной

