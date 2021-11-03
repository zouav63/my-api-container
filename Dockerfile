
FROM python:3.7

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./blog ./blog

EXPOSE 80

CMD ["uvicorn", "blog.main:app","--host", "0.0.0.0","--port", "80"]


