#!/bin/sh

sudo docker run -it \
     --network host \
     -p 344:345 \
     -p 345:345 \
     -p 443:443 \
     hubium
