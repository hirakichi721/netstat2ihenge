#!/usr/bin/python

#
# netstat2henge.py
#
# Convert from netstat edited data to inet-henge formated data.
#
# [netstat edited data](input)
#   protocol,sourceip:sourceport,destip:destport
# 
# InputSample
#  tcp,10.0.0.1:514,10.0.0.2:10023
#  tcp,0.0.0.0:514,*:*
#  udp,10.0.0.1:10001,10.0.0.3:514
#
# [inet-henge formated json data](output)
# OutputSample
# {
#    "nodes": [
#        {
#            "name": "10.0.0.1", 
#            "icon": "./images/router.png"
#        }, 
#        {
#            "name": "10.0.0.2", 
#            "icon": "./images/router.png"
#        }, 
#        {
#            "name": "10.0.0.3", 
#            "icon": "./images/router.png"
#        }
#    ], 
#    "links": [
#        {
#            "source": "10.0.0.1", 
#            "target": "10.0.0.2"
#        }, 
#        {
#            "source": "10.0.0.1", 
#            "target": "10.0.0.3"
#        }
#    ]
# }
#
# [Pre-requirement]
# Install environment for https://github.com/codeout/inet-henge
# 1. git clone https://github.com/codeout/inet-henge.git
# 2. cd inet-henge
# 3. python -m SimpleHTTPServer (Create local server)
# 4. Edit example/index.html's index.json -> output.json(output of this script.)
# 5. Browse http://localhost:8000/example/index.html, then you can see a network graph.
#
# [Warning]
# IP of * or 0.0.0.0(listed in exclideips)are ignored.
# 

import sys
import json

if len(sys.argv)!=2:
  print("Usage: inputFile")
  sys.exit(0)

excludeips=["*","0.0.0.0"]
fp=sys.argv[1]
nodes=[]
links={}  # sourceip=>destip

with open(fp,"r") as f:
  for line in f.readlines():
    line=line.strip()
    sps=line.split(",")
    (si,sp)=sps[1].split(":")
    (di,dp)=sps[2].split(":")

    isExclude=True
    if si not in excludeips:
      nodes.append(si)
      isExclude=False
    if di not in excludeips:
      nodes.append(di)
      isExclude=False

    if not isExclude:
      if si not in links.keys():
        links[si] = []
      links[si].append(di)

nodes = sorted(list(set(nodes)))

# sample output of inet-henji
#{
#  "nodes":[
#    {"name":"A", "icon": "./images/router.png", "meta":{"description":"Gateway Server","type":"Backbone","loopback":"10.1.1.1"}},
#    {"name":"B", "icon": "./images/router.png", "meta":{"loopback":"10.1.1.2"}}
#  ],
#  "links":[
#    {"source":"A","target":"B",
#     "meta":{
#       "interface": {"source":"ens192","target":"ens224"},
#     }
#    }
#  ]
#}

output = {}
output["nodes"]=[]
output["links"]=[]
for node in nodes:
  output["nodes"].append({"name":node,"icon":"./images/router.png"})
for sip in links.keys():
  for dip in links[sip]:
    output["links"].append({"source":sip,"target":dip})

print(json.dumps(output,indent=4))
