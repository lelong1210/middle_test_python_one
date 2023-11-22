FROM python:3.9.18-bookworm

WORKDIR /app/working_proxy 
COPY src/main.py .
COPY resource/ .

RUN apt-get update && apt-get upgrade -y
CMD ["./mitmdump","-s","main.py"]

EXPOSE 8080