FROM python:3.10

WORKDIR /erythaggsrv
RUN python -m pip install --upgrade pip
RUN python -m pip install fastapi uvicorn opencv-python Pillow

COPY . /erythaggsrv                                                                                                                                                                                                    

EXPOSE 5203
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5203"]
