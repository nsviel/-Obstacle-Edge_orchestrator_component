FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive
ENV TZ Europe/Paris

# Install dependancy packages
RUN mkdir app \
    && apt-get update \
    && apt-get install -y python3 python3-pip python3-pcapy python3-scapy \
    && pip3 install scapy requests paho-mqtt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Program parameters
COPY . /app/hubium
WORKDIR /app/hubium

# Open port
EXPOSE 344
EXPOSE 345
EXPOSE 443 

# Final command
CMD [ "python3", "main.py"]
