FROM python:3.10

WORKDIR /filesrv
RUN python -m pip install --upgrade pip
RUN python -m pip install fastapi uvicorn opencv-python Pillow

COPY . /filesrv                                                                                                                                                                                                      

EXPOSE 5100
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5100"]
