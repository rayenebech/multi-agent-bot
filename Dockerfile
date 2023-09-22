FROM nvidia/cuda:11.8.0-base-ubuntu20.04

RUN apt update && apt install -yq --no-install-recommends \
    curl wget rsync \
    gnupg openssl ca-certificates \
    apt-utils software-properties-common \
    locales tzdata

# common applications
RUN apt update && apt install -yq --no-install-recommends \
    htop tmux screen \
    vim nano \
    net-tools telnet iputils-ping \
    git \
    python3 \
    python3-pip



WORKDIR /app

COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt



