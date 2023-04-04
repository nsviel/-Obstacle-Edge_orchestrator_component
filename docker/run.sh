#!/bin/sh

docker run -it \
     --network host \
     -p 344:345 \
     -p 345:345 \
     -p 443:443 \
     -p 6969:6969 \
     edge_orchestrator
