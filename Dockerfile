FROM python:3.13-bullseye AS python-base

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    vim \
    nano \
    unzip \
    git \
    wget \
    iputils-ping \
    openssh-client \
    chromium \
    chromium-driver \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    libfontconfig1 \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    unixodbc \
    unixodbc-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

COPY requirements.txt /workspace/requirements.txt

WORKDIR /workspace

RUN pip install --no-cache-dir -r requirements.txt