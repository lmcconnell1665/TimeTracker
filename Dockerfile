# Dockerfile for building application container (django web app)
# L. McConnell
# Updated: 2021-02-02

# Starting container image
FROM python:3.7
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /code

# Copy requirements file into working directory
COPY requirements.txt /code/

# Install packages from requirements.txt
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

# Copy everything to working directory
COPY . /code/
