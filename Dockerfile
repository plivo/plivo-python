FROM python:3.7-alpine

WORKDIR /usr/src/app
RUN apk update && apk add git vim bash wget make && apk add --update --no-cache g++ gcc libxslt-dev

# Copy setup script
COPY setup_sdk.sh /usr/src/app
RUN chmod a+x /usr/src/app/setup_sdk.sh

ENTRYPOINT [ "/usr/src/app/setup_sdk.sh" ]