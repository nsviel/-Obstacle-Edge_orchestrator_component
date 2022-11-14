FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive
ENV TZ Europe/Paris

# Install dependancy packages
RUN apt update \
    && apt install -y \
    python3 python3-pip python3-pcapy python3-scapy libiperf0 \
    && pip3 install scapy requests paho-mqtt iperf3 \
    && apt clean \
    && rm -rf /var/lib/apt/lists/* \
    && apt autoremove -y

# Program parameters
COPY . /app/hubium
VOLUME /app/hubium/data
WORKDIR /app/hubium

# Open port
EXPOSE 344  # Sock server Lidar 1
EXPOSE 345  # Sock server Lidar 2
EXPOSE 443  # HTTP server
EXPOSE 6969 # iperf3 

# Final command
CMD [ "python3", "main.py"]
