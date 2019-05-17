from pysnmp.hlapi import *

result = getCmd(SnmpEngine(),
	CommunityData('public', mpModel=0),
	UdpTransportTarget(('10.31.70.107', '161')),
	ContextData(),
	ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

result2 = nextCmd (SnmpEngine(),
	CommunityData('public', mpModel=0),
	UdpTransportTarget(('10.31.70.107', '161')),
	ContextData(),
	ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.2')),
    lexicographicMode=False) # Не идти в глубину

for i in result:
	for j in i[3]:
		print(j)
for i in result2:
	for j in i[3]:
		print(j[1])


#rez1 = result(UdpTransportTarget(('10.31.70.107', '161')))
#snmp_object = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0) # По имени MIB-переменной
#snmp_object = ObjectIdentity('1.3.6.1.2.1.2.2.1.2') # По значению MIB-переменной
