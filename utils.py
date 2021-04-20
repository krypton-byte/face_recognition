def patternResCustom(img, res=1280):
    x, y = img.width, img.height
    if x==y:
        return [res, res]
    elif x>y:
        return [res,int(y/(x/res))]
    elif x<y:
        return  [int(x/(y/res)),res]