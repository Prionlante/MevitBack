FROM python:3.10

WORKDIR ~/platagg
RUN python -m pip install --upgrade pip
RUN python -m pip install fastapi uvicorn opencv-python Pillow numpy

COPY ..                                                                                                                                                                                    

EXPOSE 5204
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5204"]
