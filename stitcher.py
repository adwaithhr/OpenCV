import cv2
#image_paths = ['Images/iv/iv1.jpg', 'Images/iv/iv2.jpg', 'Images/iv/iv3.jpg']
imgs = []

for path in image_paths:
    img = cv2.imread(path)
    if img is None:
        print(f"Error loading image: {path}")
    else:
        imgs.append(img)
        cv2.imshow(f'Loaded Image - {path}', img)

if len(imgs) < 2:
    print("Insufficient images for stitching. Need at least 2.")
else:
    stitcher = cv2.Stitcher.create()
    status, output = stitcher.stitch(imgs)

    if status != cv2.Stitcher_OK:
        print("Stitching was not successful.")
    else:
        print('Your Panorama is ready!!!')
        cv2.imshow('Final Panorama', output)

cv2.waitKey(0)
cv2.destroyAllWindows()