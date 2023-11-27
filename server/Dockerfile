FROM python:3 AS data_find

WORKDIR /usr/src/app

COPY ./back_end /usr/src/app
RUN pip install --upgrade pip && pip install -r lib_requirements.txt

RUN python run_all.py



