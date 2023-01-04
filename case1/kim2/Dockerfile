FROM python:3.8-slim-buster
COPY . /kim2
WORKDIR /kim2
RUN pip install Flask
RUN pip install requests
ENTRYPOINT [ "python" ]
CMD [ "kim2.py" ]
