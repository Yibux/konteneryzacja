FROM python

RUN mkdir -p /home/app

COPY . /home/app

RUN pip install -r /home/app/requirement.txt

CMD ["python", "/home/app/server.py"]