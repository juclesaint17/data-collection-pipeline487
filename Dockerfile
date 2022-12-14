
FROM python:latest

RUN apt -f install -y

RUN apt-get install -y wget

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable

RUN apt-get -y update


RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip

RUN apt-get install -yqq unzip

RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/


WORKDIR  /home/juc-lesaint/Desktop/data-collection-pipeline487/

 
COPY . .

#RUN pip install -r requirements.txt
RUN  pip install -e .


ENTRYPOINT ["python3", "main.py"]
