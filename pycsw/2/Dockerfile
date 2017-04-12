FROM python:2.7-alpine

MAINTAINER Daniel Nüst <daniel.nuest@uni-muenster.de>

WORKDIR /tmp

ARG pycsw_version=2.0.2

RUN apk add --no-cache \
    build-base \
    ca-certificates \
    postgresql-dev \
    python-dev \
    libpq \
    libxslt-dev \
    libxml2-dev \
    wget \
  && apk add --no-cache \
    --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \
    --allow-untrusted \
      geos \
  && wget https://github.com/geopython/pycsw/archive/${pycsw_version}.tar.gz \
  && tar --extract --verbose --file ${pycsw_version}.tar.gz \
  && pip install --requirement pycsw-${pycsw_version}/requirements-standalone.txt \
  && pip install --requirement pycsw-${pycsw_version}/requirements-pg.txt \
  && pip install pycsw-${pycsw_version}/ \
  && pip install gunicorn \
  && mkdir /etc/pycsw \
  && mv pycsw-${pycsw_version}/default-sample.cfg /etc/pycsw/pycsw.cfg \
  && rm -rf ${pycsw_version}.tar.gz \
  && rm -rf pycsw-${pycsw_version}

ENV PYCSW_CONFIG=/etc/pycsw/pycsw.cfg

EXPOSE 8000

ENTRYPOINT ["gunicorn", "--workers=2", "--bind=0.0.0.0:8000", "--access-logfile", "-", "pycsw.wsgi"]
