FROM python:3.11-bullseye
RUN apt-get update && apt-get install -y python3-pip
WORKDIR /message_service
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . /message_service
EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
