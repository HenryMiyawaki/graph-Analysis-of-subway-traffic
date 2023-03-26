FROM python
RUN pip install igraph && pip install pycairo
RUN apt-get update && apt-get install -y nano
COPY . .