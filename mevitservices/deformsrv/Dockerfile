FROM python:3.10

WORKDIR /deformsrv
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y
RUN python -m pip install --upgrade pip
RUN python -m pip install fastapi uvicorn Pillow numpy opencv-python


COPY . /deformsrv                                                                                                                                                                                                     

EXPOSE 5201
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5201"]
