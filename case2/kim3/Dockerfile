FROM python:3.8-slim-buster
COPY . /kim3
WORKDIR /kim3
RUN pip install Flask
RUN pip install requests
ENTRYPOINT [ "python" ]
CMD [ "kim3.py" ]
