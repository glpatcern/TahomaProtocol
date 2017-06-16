#!/usr/bin/python3

import json
import tahoma.protocol

creds = open('.tahoma.credentials').read()
creds = json.loads(creds)
print('Logging in to Tahomalink')
tahoma = tahoma.protocol.Protocol(creds['USERNAME'], creds['PASSWORD'], 'tahomacookie')
tahoma.getSetup()

print('User:', tahoma.getUser())

print('All registered devices')
devbylabel = {}
devs = tahoma.getDevices()
for d in devs.keys():
    # build reverse dictionary by label
    devbylabel[devs[d].label] = devs[d]
    # print info
    print('Device %s: type = %s, label = %s' % (d, devs[d].type, devs[d].label))
    print('    commands = %s' % devs[d].commandDefinitions)
    try:
        print('    state = %s' % devs[d].activeStates)
    except AttributeError:
        pass

for ag in tahoma.getActionGroups():
	for a in ag.actions:
	    print('For device %s, command = %s' % (devs[a.deviceURL].label, a.commands))

