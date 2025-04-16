FROM python:3.11-slim
RUN mkdir /home/app  
WORKDIR /home/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8080
CMD ["python", "app.py"]
    
