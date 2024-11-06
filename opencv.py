import cv2

path="Kucing.jpg"
image=cv2.imread(path)
window_name="Membuka Gambar"
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
