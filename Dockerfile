FROM python:3 

WORKDIR /usr/src/app

COPY ./back_end /usr/src/app
RUN pip install --upgrade pip && pip install -r lib_requirements.txt
RUN apt-get install -y python3

RUN python3 student_schedule.py
RUN python extract_prof_names.py
RUN python prof_schedule.py

COPY ./web_html /usr/share/web

RUN cp -r /usr/src/app/timetable /usr/share/web/
EXPOSE 5000

CMD [ "python3", "/usr/share/web/app.py" ]





