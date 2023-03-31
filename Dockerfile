FROM python

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y nano