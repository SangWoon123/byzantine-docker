FROM python:3.8-slim-buster
COPY . /kim4
WORKDIR /kim4
RUN pip install Flask
RUN pip install requests
ENTRYPOINT [ "python" ]
CMD [ "kim4.py" ]
