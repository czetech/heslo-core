FROM alpine:3.16
RUN apk --no-cache add \
    py3-pip \
    python3
WORKDIR /app
COPY requirements.txt ./
RUN set -ex; \
    apk --no-cache add -t build-tools gcc musl-dev python3-dev; \
    pip3 --no-cache-dir install -r requirements.txt; \
    apk del build-tools
COPY . ./
RUN pip3 --no-cache-dir install -e .
EXPOSE 80
ENTRYPOINT ["heslo_core"]
