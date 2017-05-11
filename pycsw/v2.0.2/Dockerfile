FROM python:2.7-alpine

MAINTAINER Daniel Nüst <daniel.nuest@uni-muenster.de>

WORKDIR /tmp

ENV \
  PYCSW_VERSION=2.0.2 \
  PYCSW_CONFIG=/etc/pycsw/pycsw.cfg

# There's bug in libxml2 v3.9.4 that prevents using an XMLParser with a schema
# file.
#
# https://bugzilla.gnome.org/show_bug.cgi?id=766834
#
# It seems to have been fixed upstream, but the fix has not been released into
# a new libxml2 version. As a workaround, we are sticking with the previous
# version, which works fine.
# This means that we need to use alpine's archives for version 3.1, which are
# the ones that contain the previous version of libxml2
RUN \
    echo 'http://dl-cdn.alpinelinux.org/alpine/v3.1/main' >> /etc/apk/repositories \
  && apk add --no-cache \
    build-base \
    ca-certificates \
    postgresql-dev \
    python-dev \
    libpq \
    libxslt-dev \
    'libxml2-dev<2.9.4' \
    wget \
  && apk add --no-cache \
    --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \
    --allow-untrusted \
    geos \
  && wget https://github.com/geopython/pycsw/archive/${PYCSW_VERSION}.tar.gz \
  && tar --extract --verbose --file ${PYCSW_VERSION}.tar.gz \
  && pip install --requirement pycsw-${PYCSW_VERSION}/requirements-standalone.txt \
  && pip install --requirement pycsw-${PYCSW_VERSION}/requirements-pg.txt \
  && pip install pycsw-${PYCSW_VERSION}/ \
  && mkdir /etc/pycsw \
  && mv pycsw-${PYCSW_VERSION}/default-sample.cfg /etc/pycsw/pycsw.cfg \
  && rm -rf ${PYCSW_VERSION}.tar.gz \
  && rm -rf pycsw-${PYCSW_VERSION}

COPY launch-pycsw.py /usr/bin/launch-pycsw

RUN chmod a+x /usr/bin/launch-pycsw \
  && adduser -D -u 1000 user user \
  && mkdir -p /pycsw \
  && chown -R 1000:1000 /pycsw \
  && pip install pysu

EXPOSE 8000

ENTRYPOINT ["launch-pycsw"]

CMD ["run"]
