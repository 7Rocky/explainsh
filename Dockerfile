FROM python:3.9-alpine

WORKDIR /explainsh
COPY explainsh.py .

RUN chmod +x explainsh.py
RUN mv explainsh.py /usr/bin/explainsh

USER nobody

ENTRYPOINT [ "explainsh" ]
