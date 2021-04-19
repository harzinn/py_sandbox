FROM harzinn/pydev:alpine

WORKDIR /home/src
COPY . .

CMD ["main.py"]
ENTRYPOINT ["python3"]