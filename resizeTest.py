import cv2
oriimg = cv2.imread("idenprof/train/engineer/engineer-1.jpg", cv2.IMREAD_COLOR)
newimg = cv2.resize(oriimg,(224,224)) 
cv2.imshow("Show by CV2",newimg)
cv2.waitKey(0)
cv2.imwrite("resizeimg.jpg",newimg)