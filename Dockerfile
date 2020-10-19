FROM python:alpine
COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]