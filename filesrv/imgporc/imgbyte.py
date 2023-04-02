import cv2, io, base64, numpy as np
from PIL import Image

def suplibs(libname=''):
    """
    This function print all supports computer vision library's
    (without parameters)
    or
    check checks if the library is supported
    (with parameter ---> libname)
    """

    __libs = {
        "OpenCV": 'cv',
        "PIL": "imagePIL"
    }

    match libname:
        case '':
            print(f"Library's support:\n{', '.join(list(__libs.keys()))}")
        case _ :
            try:
                print(f"This library is supported,"\
                      f"\nname to params ---> {__libs[libname]}")
            except:
                print("This library not supported")

def imgToB64 (imgtarget, lib = 'cv'):
    """
    This function convert image to base64 string
    or
    images list to base64 strings list

    lib parameter indicates to format, that image
    will be converted to byte.

    Before convert images to byte strings, please check supports
    computer vision library's ---> suplibs()
    """

    match lib:
        case 'cv':
            if (type(imgtarget) is list):

                # Method using .png format because
                # medical image requires save quality
                # for any type of medical image

                reslist = []
                for i in imgtarget:
                    _, img_arr = cv2.imencode('.png', i)
                    img_bytes = img_arr.tobytes()
                    img64 = base64.b64encode(img_bytes).decode("utf8")
                    reslist.append(img64)
                return reslist
            else:
                _, img_arr = cv2.imencode('.png', imgtarget)
                img_bytes = img_arr.tobytes()
                img64 = base64.b64encode(img_bytes).decode("utf8")
                return img64

        case 'imagePIL':
            if (type(imgtarget) is list):
                reslist = []
                for i in imgtarget:
                    buf = io.BytesIO()
                    i.save(buf, format="png")
                    img_bytes = buf.getvalue()
                    img64 = base64.b64encode(img_bytes).decode("utf8")
                    reslist.append(img64)
                return reslist
            else:
                buf = io.BytesIO()
                imgtarget.save(buf, format="png")
                img_bytes = buf.getvalue()
                img64 = base64.b64encode(img_bytes).decode("utf8")
                return img64
        case _:
            print("This library not supported")


def b64ToImg (imgtarget, lib='cv'):
    """
    This function convert base64 string to image
    or
    base64 strings list to images list.

    lib parameter indicates what image format bytes will be
    converted.

    Before convert byte strings to images, please check supports
    computer vision library's ---> suplibs()
    """

    match lib:
        case 'cv':
            if (type(imgtarget) is list):
                reslist =[]
                for i in imgtarget:
                    img64 =base64.b64decode(i.encode('utf-8'))
                    img_np = np.frombuffer(img64, dtype=np.uint8)
                    img_cv = cv2.imdecode(img_np, flags=1)
                    reslist.append(img_cv)
                return reslist
            else:
                img64 = base64.b64decode(imgtarget.encode('utf-8'))
                img_np = np.frombuffer(img64, dtype=np.uint8)
                img_cv = cv2.imdecode(img_np, cv2.IMREAD_COLOR)
                return img_cv

        case 'imagePIL':
            if (type(imgtarget) is list):
                reslist = []
                for i in imgtarget:
                    img64 = base64.b64decode(i.encode('utf-8'))
                    img_pil = Image.open(io.BytesIO(img64))
                    reslist.append(img_pil)
                return reslist
            else:
                img64 = base64.b64decode(imgtarget.encode('utf-8'))
                img_pil = Image.open(io.BytesIO(img64))
                return img_pil
        case _ :
            raise Exception("This library not support")

def fileBytesToImg(imgtarget, lib='cv'):
    """
    This function convert file_bytes string to image
    or
    file_bytes strings list to images list.

    lib parameter indicates what image format bytes will be
    converted.

    Before convert byte strings to images, please check supports
    computer vision library's ---> suplibs()
    """
    match lib:
        case 'cv':
            if (type(imgtarget) is list):
                reslist = []
                for i in imgtarget:
                    img_np = np.frombuffer(i, dtype=np.uint8)
                    img_cv = cv2.imdecode(img_np, flags=1)
                    reslist.append(img_cv)
                return reslist
            else:
                img_np = np.frombuffer(imgtarget, dtype=np.uint8)
                img_cv = cv2.imdecode(img_np, flags=1)
                return img_cv

        case 'imagePIL':
            if (type(imgtarget) is list):
                reslist = []
                for i in imgtarget:
                    img_pil = Image.open(io.BytesIO(i))
                    reslist.append(img_pil)
                return reslist
            else:
                img_pil = Image.open(io.BytesIO(imgtarget))
                return img_pil
        case _:
            raise Exception("This library not support")
