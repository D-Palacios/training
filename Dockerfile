FROM python:3.7-alpine

RUN apk --no-cache add curl gcc g++ libstdc++\
    && echo "Pulling watchdog binary from Github." \
    && curl -sSL https://github.com/openfaas/faas/releases/download/0.13.0/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog

RUN pip install --upgrade pip

WORKDIR /root

COPY src/ /root/src/

RUN pip install -r src/requirements.txt\
    && apk del curl gcc g++ --no-cache

ENV fprocess="python3 src/index.py"
ENV combine_output=false

EXPOSE 8080

HEALTHCHECK --interval=3s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
