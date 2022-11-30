# base image  
FROM python:3.8.15-bullseye   
# setup environment variable  
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# RUN pip install --upgrade pip  

# Set work directory
WORKDIR /code

# Install dependencies
COPY ./requirments.txt .
RUN pip install -r requirments.txt

# Copy project
COPY . .


# EXPOSE 8000  
# # start server we use this if no docker-compose and one image only 
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


