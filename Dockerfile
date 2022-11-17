FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive
ENV TZ Europe/Paris

# Install dependancy packages
RUN apt update \
    && apt install -y \
    python3 python3-pip python3-pcapy python3-scapy libiperf0 iputils-ping nano \
    && pip3 install scapy requests paho-mqtt iperf3 pymongo \
    && rm -rf /var/lib/apt/lists/*

# Program parameters
COPY . /app/hubium
VOLUME /app/hubium/data
WORKDIR /app/hubium

# Open port
# Sock server Lidar 1
EXPOSE 344
# Sock server Lidar 2
EXPOSE 345
# HTTP server
EXPOSE 443
# iperf3
EXPOSE 6969

# Final command
CMD [ "python3", "main.py"]
