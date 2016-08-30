FROM tomcat:9-alpine
MAINTAINER Daniel Nüst <daniel.nuest@uni-muenster.de>

# Project: https://github.com/52North/sos

RUN apk --no-cache add curl unzip

# Download release and deploy in Tomcat, see docs at https://wiki.52north.org/SensorWeb/SensorObservationServiceIVDocumentation
WORKDIR /tmp
RUN curl -L -o sos-bundle.zip http://52north.org/downloads/send/3-sos/491-52n-sensorweb-sos-bundle-4-3-7 \
    && unzip -d sos-bundle sos-bundle.zip \
    # webapp name fixed in several config files of the bundle
    && cp sos-bundle/*/bin/target/*.war $CATALINA_HOME/webapps/52n-sos-webapp.war \
    && rm -r *

# FIXME http://localhost/52n-sos-webapp/static/client/jsClient and http://localhost/52n-sos-webapp/static/doc/api-doc are not available

# docker build -t 52n-sos-alpine .
# docker run --name sos -p 80:8080 52n-sos-alpine
# http://localhost/52n-sos-webapp