FROM python:3.6.7-alpine3.7

RUN pip install --upgrade pip setuptools wheel

# Environment vars
ENV APP_HOME /app

# Config app dir
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# Copy codebase into workdir
COPY . $APP_HOME

RUN pip install -r requirements.txt
RUN python -m pytest