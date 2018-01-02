FROM python:3.6.4-alpine3.7
ADD ./Pipfile /code/
WORKDIR /code
RUN pip install pipenv
# RUN pipenv lock -r|cut -d"=" -f1 > /code/requirments.txt
RUN pipenv install
# RUN pip install -r /code/requirments.txt
CMD pipenv run python ${PYTHON_APP}