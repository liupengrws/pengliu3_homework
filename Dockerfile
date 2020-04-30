FROM python:3
USER root

ADD query_vendor_by_mac.py /

RUN pip install requests

