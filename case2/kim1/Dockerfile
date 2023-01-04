FROM python:3.8-slim-buster
COPY . /kim1
WORKDIR /kim1
RUN pip install Flask
RUN pip install requests
ENTRYPOINT [ "python" ]
CMD [ "kim1.py" ]
