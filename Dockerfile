FROM python:3.10-buster

RUN mkdir /app

COPY ./reporter /app
COPY ./reports /app
COPY pyproject.toml /app

WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN apt-get -y install pandoc

ENTRYPOINT ["python", "reporter/cli.py"]

CMD ["generate","losh2021","--out output","html" ,"--log_to console"]