FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2 && apt-get -y install postgresql postgresql-contrib

# set work directory
RUN mkdir -p /usr/src/ResumeParser
WORKDIR /usr/src/ResumeParser
COPY . /usr/src/ResumeParser
RUN apt-get update && apt-get install -y netcat
RUN pip install --upgrade pip
RUN pip install -r /usr/src/ResumeParser/requirements.txt
RUN python /usr/src/ResumeParser/pre_requisites.py
RUN python /usr/src/ResumeParser/manage.py migrate
RUN python /usr/src/ResumeParser/db_populate.py
RUN python /usr/src/ResumeParser/manage.py collectstatic --no-input



# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/ResumeParser/entrypoint.sh
RUN chmod +x /usr/src/ResumeParser/entrypoint.sh

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/ResumeParser/entrypoint.sh"]
