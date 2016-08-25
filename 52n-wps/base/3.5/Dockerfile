FROM tomcat:9
MAINTAINER Daniel Nüst <daniel.nuest@uni-muenster.de>

# Project: https://github.com/52North/wps

# Download release and deploy in Tomcat, see docs at https://wiki.52north.org/SensorWeb/SensorObservationServiceIVDocumentation
WORKDIR $CATALINA_HOME/webapps

RUN curl -L -o wps.war http://52north.org/downloads/send/15-wps/492-52n-wps-webapp-3-5-0

# TODO geotools package: http://52north.org/downloads/send/15-wps/493-wps-3-5-0-geotools-package
# TODO replace wps-config-file with custom one

# docker build -t 52n-wps-base .
# docker run --name wps-base -p 80:8080 52n-wps
# http://localhost/wps
# Login: wps/wps