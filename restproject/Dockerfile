FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt 
RUN pip install --upgrade pip


# CMD ["python3","app.py"]

COPY . .

CMD [ "python3", "manage.py" , "runserver" , "0.0.0.0:8000" ]