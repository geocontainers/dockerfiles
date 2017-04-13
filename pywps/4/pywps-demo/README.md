# PyWPS Demo Dockerfile

```bash
docker build -t pywps-demo .
docker run -p 5000:5000 pywps-demo
```
The open the following link for documents and/or services
http://localhost:5000/
http://localhost:5000/wps?request=GetCapabilities&service=WPS
http://localhost:5000/wps?request=DescribeProcess&service=WPS&identifier=all&version=1.0.0

