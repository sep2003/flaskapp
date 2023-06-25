FROM python:3-slim-buster
COPY . /python-flask
WORKDIR /python-flask
RUN pip install flask
RUN pip install templates
ENTRYPOINT [&quot;python&quot;, &quot;hello.py&quot;]