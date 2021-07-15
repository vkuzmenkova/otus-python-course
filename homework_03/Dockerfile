#docker run -p 8000:8000 app

FROM python:3.9.6-buster

WORKDIR /wapp

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY ./app/pyproject.toml .
COPY ./app/poetry.lock .

RUN poetry install

COPY app ./

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0"]