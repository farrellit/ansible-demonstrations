FROM python:3-alpine 
RUN apk add --no-cache alpine-sdk libffi-dev openssl-dev coreutils
RUN pip install --upgrade pip
RUN pip install ansible
WORKDIR /ansible
CMD ansible-playbook -i hosts main.yml -vvvv
