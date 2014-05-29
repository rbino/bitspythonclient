#!/usr/bin/env python

import websocket
import json
import time
import thread

prev_status = ""

def on_message(ws, message):
    global prev_status
    try:
        cur_status = json.loads(message)["status"]["value"]
        if cur_status != prev_status:
            prev_status = cur_status
            if cur_status == "open":
                print "Now it's opened!" # Mettete qui le cose da fare all'apertura della sede
            elif cur_status == "closed":
                print "Now it's closed!" # Mettete qui le cose da fare alla chiusura della sede
            else:
                print "WTF?" # Se entra qui, non va bene
    except:
        pass

def on_error(ws, error):
    print "Error: " + error.message
    print "Reconnecting..."    
    start_websocket()

def on_close(ws):
    print "Connection closed"

def on_open(ws):
    def ping(*args):
        while 1:
            #print "Keep-alive"
            ws.send("Hi")
            time.sleep(15)
    thread.start_new_thread(ping, ())    

def start_websocket():
    ws = websocket.WebSocketApp("wss://bits.poul.org/ws",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close,
                                on_open = on_open)
    ws.run_forever()

if __name__== "__main__":
    start_websocket()
