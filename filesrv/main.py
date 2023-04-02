import uvicorn
from fastapi import FastAPI, File, Form
from fastapi.responses import FileResponse
import requests, json
from imgporc.imgbyte import b64ToImg, fileBytesToImg, imgToB64

mevitsrv_ip = {
    "deform": "http://deform:5201/imgproc",
    "partsize": "http://partsize:5202/imgproc",
    "erythagg": "http://erythagg:5203/imgproc",
    "platagg": "http://platagg:5204/imgproc"
}

def sender(file_list:list, name_list:list, adress:str):
    """
    This function contains the main logic of interaction
    with mevit services:
    - read files from front
    - send read files to mevit service
    - get work result from mevit service
    """
    img_to_srv = []
    img_from_srv = []
    img_orig = [fileBytesToImg(i, 'imagePIL') for i in file_list]

    for i in range(len(file_list)):
        img = fileBytesToImg(file_list[i], 'cv')
        img_to_srv.append({'img': imgToB64(img, 'cv')})


    headers = {'Content-type': 'application/json',
               'Accept': 'text/plain'}
    resp = requests.post(adress,
                         data=json.dumps(img_to_srv),
                         headers=headers)

    # NOTE: PIL Image can read byte sting of cv,
    # but OpenCV can't read byte string of PIL Image
    for i in range(len(resp.json())):
        img_from_json = resp.json()[i]['img']
        img = b64ToImg(img_from_json, 'imagePIL')
        img_from_srv.append(img)

    return img_orig, img_from_srv

# ToDev: Then service and profile pages will be
# ready, need to develop code, that interact
# with the database
def dbstub(img_orig:list, img_proc:list, name_list:list):
    for i in range(len(name_list)):
        img_orig[i].save(f'./origimg/{name_list[i]}')
        img_proc[i].save(f'./procimg/{name_list[i]}')


app = FastAPI()

@app.get('/', status_code=200)
async def checkWork():
    return 'File server is work!'

@app.get('/img/', status_code=200)
def getImage(name: str):
    return FileResponse(f'procimg/{name}')


@app.post('/upload/deformsrv',
          summary="Api-gateway between front "\
                  "and deformation service",
          status_code=200)
async def deformSend(files: list[bytes] = File(...),
                     names: list[str] = Form(...)):

    img_orig, img_from_srv = sender(file_list = files,
                                    name_list = names ,
                                    adress = mevitsrv_ip['deform'])
    dbstub(img_orig = img_orig,
           img_proc = img_from_srv,
           name_list = names)

@app.post('/upload/partsizesrv',
          summary="Api-gateway between front "\
                  "and particle size service",
          status_code=200)
async def partsizeSend(files: list[bytes] = File(...),
                     names: list[str] = Form(...)):

    img_orig, img_from_srv = sender(file_list = files,
                                    name_list = names ,
                                    adress = mevitsrv_ip['partsize'])
    dbstub(img_orig = img_orig,
           img_proc = img_from_srv,
           name_list = names)

@app.post('/upload/erythaggsrv',
          summary="Api-gateway between front "\
                  "and erythrocyte aggregation service",
          status_code=200)
async def erythaggSend(files: list[bytes] = File(...),
                     names: list[str] = Form(...)):

    img_orig, img_from_srv = sender(file_list = files,
                                    name_list = names ,
                                    adress = mevitsrv_ip['erythagg'])
    dbstub(img_orig = img_orig,
           img_proc = img_from_srv,
           name_list = names)

@app.post('/upload/plataggsrv',
          summary="Api-gateway between front "\
                  "and platelets aggregation service",
          status_code=200)
async def plataggSend(files: list[bytes] = File(...),
                     names: list[str] = Form(...)):

    img_orig, img_from_srv = sender(file_list = files,
                                    name_list = names ,
                                    adress = mevitsrv_ip['platagg'])
    dbstub(img_orig = img_orig,
           img_proc = img_from_srv,
           name_list = names)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5100)
