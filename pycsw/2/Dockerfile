FROM alpine:3.4
MAINTAINER Daniel Nüst <daniel.nuest@uni-muenster.de>

# http://docs.pycsw.org/en/2.0.0/installation.html#for-developers-and-the-truly-impatient

WORKDIR /
RUN apk add --no-cache \
  #linux-headers \
  build-base \
  git \
  python \
  python-dev \
  py-pip \
  libxslt-dev \
  libxml2-dev \
  #py-libxml2 \
  && git clone https://github.com/geopython/pycsw.git

RUN apk add --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted \
  geos

WORKDIR /pycsw
RUN pip install -e .
RUN pip install -r requirements-standalone.txt

COPY default.cfg default.cfg

RUN pycsw-admin.py -c setup_db -f default.cfg

EXPOSE 8000
CMD ["python", "/pycsw/pycsw/wsgi.py"]
# docker build -t pycsw .
# docker run -p 80:8000 pycsw