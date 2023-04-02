from imgporc.imgbyte import b64ToImg, imgToB64
from imgporc import platagg
import fastapi, uvicorn

df = platagg.mevit_platagg()
app = fastapi.FastAPI()

@app.get('/')
async def checkWork():
    return 'Platelets aggregation service is work!'

@app.post('/imgproc',
          summary= "image processing to obtain "\
                   "information about cell platelets aggregation",
          status_code=200)
async def imgproc(files: fastapi.Request):
    img_proc = []
    for img in await files.json():
        img_byte = img['img']
        img_cv = b64ToImg(img_byte, 'cv')
        img_proc.append(df.imgproc(img_cv))

    return [{'img': imgToB64(i, 'cv')} for i in img_proc]

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=5204)
