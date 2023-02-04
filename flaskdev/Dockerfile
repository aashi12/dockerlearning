FROM python
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=getdata.py
CMD ["flask", "run", "--host=0.0.0.0"]

