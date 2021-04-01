# Python Base Image from https://hub.docker.com/r/arm32v7/python/
FROM arm32v7/python:3-buster

# Copy the Python Script 
COPY . /app
WORKDIR /app

# Intall the rpi.gpio python module
RUN pip install --no-cache-dir -r requirements.txt

#Export the port 
EXPOSE 8888

# Trigger Python script
ENTRYPOINT ["python"]
CMD ["flask_app.py"]
