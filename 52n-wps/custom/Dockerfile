# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
FROM 52n-wps-base
MAINTAINER Daniel Nüst <daniel.nuest@uni-muenster.de>

# Project: https://github.com/52North/wps

WORKDIR $CATALINA_HOME/webapps
RUN unzip -d wps wps.war
COPY index.html wps/index.html

# TODO geotools package: http://52north.org/downloads/send/15-wps/493-wps-3-5-0-geotools-package
# TODO replace wps-config-file with custom one

# Build 52n-wps-base image first!
# docker build -t 52n-wps-custom .
# docker run --name wps-custom -p 80:8080 52n-wps-custom
# http://localhost/wps
# Login: wps/wps