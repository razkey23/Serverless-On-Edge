# Licensed to the Apache Software Foundation (ASF) under one or more contributor
# license agreements; and to You under the Apache License, Version 2.0.

FROM arm32v7/openjdk:8u181-jdk

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

#RUN apk add --update sed curl bash

ENV VERSION 1.8
ENV UPDATE 141
ENV BUILD 15
ENV SIG 336fa29ff2bb4ef291e347e091f7f4a7
ENV GLIBC_VERSION 2.23-r3

ENV JAVA_HOME /usr/lib/jvm/java-${VERSION}-openjdk
ENV JRE_HOME ${JAVA_HOME}/jre
ENV PATH $JAVA_HOME/bin:$PATH


RUN apk upgrade --update && \
    apk add --update libstdc++ curl ca-certificates bash sed && \
    update-ca-certificates && \
    for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION} glibc-i18n-${GLIBC_VERSION}; do curl -sSL https://github.com/chrisanthropic/docker-alpine-rpi-glibc-builder/releases/download/0.0.1/${pkg}.apk -o /tmp/${pkg}.apk; done && \
    apk add --allow-untrusted /tmp/*.apk && \
    rm -v /tmp/*.apk && \
    ( /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8 C.UTF-8 || true ) && \
    echo "export LANG=${LANG}" > /etc/profile.d/locale.sh && \
    /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \
    echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >> /etc/nsswitch.conf && \
    # https://github.com/anapsix/docker-alpine-java/issues/18#issue-167437838
    # If you want to change the default values here, also change the values in 042-set-jvm-ttl.sh
    sed -i s/#networkaddress.cache.ttl=-1/networkaddress.cache.ttl=10/ ${JAVA_HOME}/jre/lib/security/java.security && \
    sed -i s/networkaddress.cache.negative.ttl=10/networkaddress.cache.negative.ttl=0/ ${JAVA_HOME}/jre/lib/security/java.security

RUN mkdir /logs

COPY transformEnvironment.sh /
RUN chmod +x transformEnvironment.sh

COPY copyJMXFiles.sh /
RUN chmod +x copyJMXFiles.sh
