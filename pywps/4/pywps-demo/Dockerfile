FROM alpine:3.4
MAINTAINER Daniel Nüst <daniel.nuest@uni-muenster.de>

WORKDIR /
RUN apk add --no-cache \
  linux-headers \
  build-base \
  git \
  python \
  python-dev \
  py-pip \
  libxslt-dev \
  libxml2-dev \
  #py-libxml2 \
  # http://geopython.github.io/pywps/docs/_build/html/install.html
  && pip install -e git+https://github.com/geopython/pywps.git@master#egg=pywps-dev \
  # https://github.com/geopython/pywps-demo
  && git clone https://github.com/geopython/pywps-demo.git

WORKDIR /pywps-demo
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "demo.py"]
# docker build -t pywps-demo .
# docker run -p 80:5000 pywps-demo