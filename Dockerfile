FROM python:3.10.6

ARG DOCKER_BUILD_ENVIRONMENT=production
ENV DOCKER_BUILD_ENVIRONMENT=${DOCKER_BUILD_ENVIRONMENT}

# Install core libs
RUN apt-get update -y
RUN apt-get install -y \
  apt-utils \
  netcat-traditional

# Install deps
RUN pip install poetry>=1.3.2
RUN poetry config virtualenvs.create false
COPY poetry.lock /tmp/install/
COPY pyproject.toml /tmp/install/
WORKDIR /tmp/install
RUN poetry install

# Limited scope (User) context
# Prepare app user
# TODO: use non root user
#RUN useradd --create-home app
#WORKDIR /home/app
#USER app

RUN mkdir -p /home/app
WORKDIR /home/app

# Create media folder
RUN mkdir -p /home/app/data/media

# Prepare app bin
#COPY --chown=app ./bin /home/app/bin
COPY ./bin /home/app/bin
RUN chmod -R +xr /home/app/bin
ENV PATH="/home/app/bin:${PATH}"

#COPY --chown=app ./ /home/app
COPY ./ /home/app
COPY ./static /home/app/static
RUN chmod -R +xr /home/app

WORKDIR /home/app
ENV PYTHONPATH="/home/app:$PYTHONPATH"
ENV TZ="Asia/Dubai"

EXPOSE 8031

ENTRYPOINT ["entrypoint.sh"]