FROM oraclelinux:latest

ARG JDK_ARCHIVE
ARG WLS_ARCHIVE
ARG PROXY_URL

ENV ORACLE_HOME=/opt/wls/Oracle_Home
ENV WL_HOME=$ORACLE_HOME/wlserver
ENV DOMAIN_HOME=/opt/wls
ENV DOMAIN_NAME=domain
ENV JAVA_HOME=/usr/java
ENV PATH=$JAVA_HOME/bin:$PATH
ENV USER_MEM_ARGS="-Djava.security.egd=file:/dev/./urandom"

COPY $JDK_ARCHIVE $WLS_ARCHIVE create-domain.py /tmp/

# Set up proxy if needed
RUN if [ -n "$PROXY_URL" ]; then echo "proxy=$PROXY_URL" >> /etc/yum.conf; fi

# Install Java
RUN yum update -y > /dev/null && \
    yum install -y curl tar > /dev/null && \
    yum clean all > /dev/null && \
    mkdir -p $JAVA_HOME && \
    tar xfz /tmp/$JDK_ARCHIVE -C $JAVA_HOME --strip-components=1

# Install WebLogic
RUN useradd install && \
    mkdir -p -m 777 $ORACLE_HOME && \
    mkdir -m 777 /opt/wls/.inventory && \
    echo 'inventory_loc=/opt/wls/.inventory' >> /opt/wls/oraInst.loc && \
    su -c "$JAVA_HOME/bin/java -jar /tmp/$WLS_ARCHIVE -silent \
        -invPtrLoc /opt/wls/oraInst.loc \
        ORACLE_HOME=$ORACLE_HOME" install

RUN $ORACLE_HOME/oracle_common/common/bin/wlst.sh /tmp/create-domain.py

CMD $DOMAIN_HOME/$DOMAIN_NAME/bin/startWebLogic.sh

EXPOSE 7001
