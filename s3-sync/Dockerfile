FROM python:3.7-alpine

RUN pip install --upgrade pip
RUN pip install boto3==1.9.237

COPY action.py /action.py

ENTRYPOINT ["/action.py"]
