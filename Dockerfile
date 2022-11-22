FROM python:3.8.15-slim-buster 
RUN mkdir -p /app
COPY -r . app.py /app/
WORKDIR /app 
CMD ["app.py"]
ENTRYPOINT ["python"]