FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
# this value will be supplied by heroku, PORT is a name
EXPOSE $PORT   
# first app is modeule name(app.py) second app is the flask object(flask object in app.py)
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app 