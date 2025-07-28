FROM python:3.8
WORKDIR /app
COPY . /backend
RUN pip install flask
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app.py"]