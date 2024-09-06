###########
# BUILDER #
###########

# pull official base image
FROM python:3.12-bullseye as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get -y update \
    && apt-get install -y \
    python3-pip python3-cffi python3-brotli libpango-1.0-0 libpangoft2-1.0-0 \
    && apt-get -y clean

# lint
RUN pip install --upgrade pip

# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt
COPY . .

#########
# FINAL #
#########

# pull official base image
FROM python:3.12-bullseye

# create directory for the app user && create the app user
RUN mkdir -p /home/app && addgroup --system techyao && adduser --system --group techyao

# create the appropriate directories
ENV HOME=/home/app \
    APP_HOME=$HOME/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy project
COPY . $APP_HOME

# chown all the files to the app user
RUN chown -R techyao:techyao $APP_HOME

# change to the app user
USER techyao

CMD ["python", "manage.py", "runserver", "0.0.0.0:8005"]
