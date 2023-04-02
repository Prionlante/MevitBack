FROM python:3.10

WORKDIR /partsizesrv
RUN python -m pip install --upgrade pip
RUN python -m pip install fastapi uvicorn opencv-python Pillow

COPY . /partsizesrv                                                                                                                                                                                                  

EXPOSE 5202
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5202"]
