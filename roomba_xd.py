#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import asyncio
import json
import logging
from roomba import Roomba

#Uncomment the following two lines to see logging output
logging.basicConfig(level=logging.INFO, 
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#uncomment the option you want to run, and replace address, blid and roombaPassword with your own values

address = "192.168.0.13"
blid = "80B5051842005670"
roombaPassword = ":1:1631486412:umRA2PyZJ3c3FODX"

#myroomba = Roomba(address, blid, roombaPassword)
#or myroomba = Roomba(address) #if you have a config file - will attempt discovery if you don't
myroomba = Roomba(address, blid, roombaPassword)
async def test():
    myroomba.connect()
    await asyncio.sleep(1)
    
    import json, time
    for i in range(1):
        print(json.dumps(myroomba.master_state, indent=2))
        await asyncio.sleep(1)
    myroomba.send_command("start")
    
loop = asyncio.get_event_loop()
loop.run_until_complete(test())