FROM python:3.12

RUN mkdir /usr/src/app

# COPY fire_detector.py /usr/src/app

# COPY temperature_mock.py /usr/src/app

# COPY app.py /usr/src/app

# COPY network.py /usr/src/app


RUN pip3 install setuptools

# COPY requirements.txt /usr/src/app

WORKDIR /usr/src/app

COPY  . .

# COPY dataset ./

# COPY test_assets ./

RUN pip3 install -r requirements.txt

RUN apt update && apt install -y libgl1-mesa-glx
RUN pip install --upgrade pip

CMD [ "python3", "./app.py"]