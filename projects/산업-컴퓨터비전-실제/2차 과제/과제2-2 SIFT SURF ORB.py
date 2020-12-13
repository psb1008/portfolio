import cv2
import numpy as np
import matplotlib.pyplot as plt

img0 = cv2.imread('data/stitching/newspaper1.jpg', cv2.IMREAD_COLOR)
img1 = cv2.imread('data/stitching/newspaper2.jpg', cv2.IMREAD_COLOR)

detector = cv2.xfeatures2d.SIFT_create(50)

kps0, fea0 = detector.detectAndCompute(img0, None)
kps1, fea1 = detector.detectAndCompute(img1, None)

matcher = cv2.BFMatcher_create(cv2.NORM_L2, False)
matches = matcher.match(fea0, fea1)

pts0 = np.float32([kps0[m.queryIdx].pt for m in matches]).reshape(-1,1,2)
pts1 = np.float32([kps1[m.queryIdx].pt for m in matches]).reshape(-1,1,2)

H, mask = cv2.findHomography(pts0, pts1, cv2.RANSAC, 5.0)

plt.figure()
plt.subplot(211)
plt.axis('off')
plt.title('SIFT')
dbg_img = cv2.drawMatches(img0, kps0, img1, kps1, matches, None)
plt.imshow(dbg_img[:, :, [2,1,0]])
plt.subplot(212)
plt.axis('off')
plt.title('filtered matches')
dbg_img = cv2.drawMatches(img0, kps0, img1, kps1, [m for i, m in enumerate(matches) if mask[i]], None)
plt.imshow(dbg_img[:, :, [2,1,0]])
plt.tight_layout()
plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

img0 = cv2.imread('data/stitching/newspaper1.jpg', cv2.IMREAD_COLOR)
img1 = cv2.imread('data/stitching/newspaper2.jpg', cv2.IMREAD_COLOR)

detector = cv2.xfeatures2d.SURF_create(10000)
kps0, fea0 = detector.detectAndCompute(img0, None)
kps1, fea1 = detector.detectAndCompute(img1, None)

matcher = cv2.BFMatcher_create(cv2.NORM_L2, False)
matches = matcher.match(fea0, fea1)

pts0 = np.float32([kps0[m.queryIdx].pt for m in matches]).reshape(-1,1,2)
pts1 = np.float32([kps1[m.queryIdx].pt for m in matches]).reshape(-1,1,2)

H, mask = cv2.findHomography(pts0, pts1, cv2.RANSAC, 5.0)

plt.figure()
plt.subplot(211)
plt.axis('off')
plt.title('SURF')
dbg_img = cv2.drawMatches(img0, kps0, img1, kps1, matches, None)
plt.imshow(dbg_img[:, :, [2,1,0]])
plt.subplot(212)
plt.axis('off')
plt.title('filtered matches')
dbg_img = cv2.drawMatches(img0, kps0, img1, kps1, [m for i, m in enumerate(matches) if mask[i]], None)
plt.imshow(dbg_img[:, :, [2,1,0]])
plt.tight_layout()
plt.show()

import cv2
import numpy as np
import matplotlib.pyplot as plt

img0 = cv2.imread('data/stitching/newspaper1.jpg', cv2.IMREAD_COLOR)
img1 = cv2.imread('data/stitching/newspaper2.jpg', cv2.IMREAD_COLOR)

detector = cv2.ORB_create(100)
kps0, fea0 = detector.detectAndCompute(img0, None)
kps1, fea1 = detector.detectAndCompute(img1, None)

matcher = cv2.BFMatcher_create(cv2.NORM_HAMMING, False)
matches = matcher.match(fea0, fea1)

pts0 = np.float32([kps0[m.queryIdx].pt for m in matches]).reshape(-1,2)
pts1 = np.float32([kps1[m.trainIdx].pt for m in matches]).reshape(-1,2)
H, mask = cv2.findHomography(pts0, pts1, cv2.RANSAC, 3.0)

plt.figure()
plt.subplot(211)
plt.axis('off')
plt.title('ORB')
dbg_img = cv2.drawMatches(img0, kps0, img1, kps1, matches, None)
plt.imshow(dbg_img[:, :, [2,1,0]])
plt.subplot(212)
plt.axis('off')
plt.title('filtered matches')
dbg_img = cv2.drawMatches(img0, kps0, img1, kps1, [m for i, m in enumerate(matches) if mask[i]], None)
plt.imshow(dbg_img[:, :, [2,1,0]])
plt.tight_layout()
plt.show()