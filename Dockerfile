FROM python:3 
RUN apt-get install -y python3 && pip install --upgrade pip && RUN pip install --upgrade setuptools

WORKDIR /usr/src/app

COPY ./back_end /usr/src/app

RUN pip install -r lib_requirements.txt

RUN python student_schedule.py && python extract_prof_names.py && python prof_schedule.py

COPY ./web_html /usr/share/web

RUN cp -r /usr/src/app/timetable /usr/share/web/ && rm -rf /usr/src/app

EXPOSE 5000

CMD [ "python3", "/usr/share/web/app.py" ]





