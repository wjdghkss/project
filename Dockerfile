FROM python:3.11

WORKDIR /app
COPY requirements.txt requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

COPY . .

CMD ["python", "app.py"]