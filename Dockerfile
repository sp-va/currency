

FROM python:3.10

WORKDIR /app

COPY pyproject.toml ./

COPY ./currency_converter ./currency_converter

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
RUN poetry add python-dotenv


CMD ["poetry", "run", "python", "currency_converter/manage.py", "runserver", "0.0.0.0:8000"]