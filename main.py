from src import http_server
from src import mqtt_client


print("---- Start program ----")
#-------------

#HTTP server
http_server.run();

#MQTT client
mqtt_client.run();

#Loop
while 1:
    pass

#-------------
print("---- Stop program ----")
