from os import listdir
from os.path import isfile, join
import numpy
import os
import cv2
from scipy.stats import wasserstein_distance
from scipy.ndimage import imread
import numpy as np

outpath='C:/Users/Aniket/Desktop/Python/New folder/FINAL/scanned/'

def get_histogram(img):

  h, w = img.shape
  hist = [0.0] * 256
  for i in range(h):
    for j in range(w):
      hist[img[i, j]] += 1
  return np.array(hist) / (h * w)


mypath='C:/Users/Aniket/Desktop/Python/New folder/FINAL/vowels/ALL'
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
dists = []
x=0
min=0.1
for n in range(0,len(images)):
  a = imread('5.jpg')
  b = imread( join(mypath,onlyfiles[n]) )
  c = cv2.imread( join(mypath,onlyfiles[n]) )
  a_hist = get_histogram(a)
  b_hist = get_histogram(b)
  dist = wasserstein_distance(a_hist, b_hist)
  if(dist<0.0003 and dist<min):
    min=dist
    #dists.append(dist)
    save_fname = os.path.join(outpath, str(x)+'.jpg')
    cv2.imwrite(save_fname ,c )
    x+=1
print(len(images))
print(len(dists))
print x
