FROM python:3.11-bullseye
RUN apt-get update && apt-get install -y python3-pip
WORKDIR /user_service
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . /user_service
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
