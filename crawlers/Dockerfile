FROM python:3.9-slim

ENV DEBIAN_FRONTEND noninteractive
ENV GECKODRIVER_VER v0.30.0
ENV FIREFOX_VER 96.0

RUN apt update
RUN apt upgrade -y
RUN apt install -y --no-install-recommends firefox-esr
RUN apt install -y bzip2 xvfb wget unzip curl
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN wget https://download-installer.cdn.mozilla.net/pub/firefox/releases/${FIREFOX_VER}/linux-x86_64/en-US/firefox-${FIREFOX_VER}.tar.bz2
RUN tar -jxvf firefox-${FIREFOX_VER}.tar.bz2 -C /opt/ 
RUN chmod 755 /opt/firefox 
RUN chmod 755 /opt/firefox/firefox
RUN rm firefox-${FIREFOX_VER}.tar.bz2

RUN wget https://github.com/mozilla/geckodriver/releases/download/${GECKODRIVER_VER}/geckodriver-${GECKODRIVER_VER}-linux64.tar.gz
RUN tar -zxvf geckodriver-${GECKODRIVER_VER}-linux64.tar.gz
RUN mv geckodriver /usr/bin/
RUN rm geckodriver-${GECKODRIVER_VER}-linux64.tar.gz

WORKDIR /opt/crawlers

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt