FROM python:3.6.4-alpine3.7
ADD . /code
WORKDIR /code
RUN pip install pipenv
RUN pipenv install
CMD ["python", "./rest/app.py"]