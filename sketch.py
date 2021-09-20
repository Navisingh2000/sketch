try:
    import cv2 #for image processing
    import sys
    import matplotlib.pyplot as plt
    import os
    import sys
except Exception as e:
    print(e)
    
def sketch(ImagePath):
    #ImagePath=r"C:/Users/Dell/Desktop/Nitish Jain/Pic.jpeg"
    img = cv2.imread(ImagePath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    if img is None:
        print("Can not find any image. Choose appropriate file")
        sys.exit()
    grey_img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    invert_img=cv2.bitwise_not(grey_img)
    blur_img=cv2.GaussianBlur(invert_img, (111,111),0)
    invblur_img=cv2.bitwise_not(blur_img)
    sketch_img=cv2.divide(grey_img,invblur_img, scale=256.0)
    cv2.imwrite('public/Sketch.jpeg', sketch_img )

oldname = sys.argv[1]
newname = oldname+'.jpg'
os.rename(oldname,newname)
sketch(newname) 