# netstat2henge.py
  Convert from netstat edited data to inet-henge formated data.

# Basic Information
## input
 [netstat edited data](input)
   protocol,sourceip:sourceport,destip:destport
 
 InputSample
  ```
  tcp,10.0.0.1:514,10.0.0.2:10023
  tcp,0.0.0.0:514,*:*
  udp,10.0.0.1:10001,10.0.0.3:514
  ```

## output
 [inet-henge formated json data](output)
 OutputSample
 ```
 {
    "nodes": [
        {
            "name": "10.0.0.1", 
            "icon": "./images/router.png"
        }, 
        {
            "name": "10.0.0.2", 
            "icon": "./images/router.png"
        }, 
        {
            "name": "10.0.0.3", 
            "icon": "./images/router.png"
        }
    ], 
    "links": [
        {
            "source": "10.0.0.1", 
            "target": "10.0.0.2"
        }, 
        {
            "source": "10.0.0.1", 
            "target": "10.0.0.3"
        }
    ]
 }
 ```

# Pre-requirement
 Install environment for https://github.com/codeout/inet-henge
 1. git clone https://github.com/codeout/inet-henge.git
 2. cd inet-henge
 3. python -m SimpleHTTPServer (Create local server)
 4. Edit example/index.html's index.json -> output.json(output of this script.)
 5. Browse http://localhost:8000/example/index.html, then you can see a network graph.

# Warning
 IP of * or 0.0.0.0(listed in exclideips)are ignored.

