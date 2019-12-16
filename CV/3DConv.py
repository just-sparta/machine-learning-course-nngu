import numpy as np

def ThreeDimConvolution():

  input_ = np.ones((3,3)).astype(np.int32)
  kernel_ = np.array([ [[1, 1], [1, 1]], 
                       [[1, 1], [1, 1]] ], np.int32)
  result = np.zeros(shape=[len(kernel_),len(kernel_[0]),len(kernel_[0][0])], 
                    dtype=np.uint8)
  amount = 0

  nX = 0
  nY = 0

  dX = 1
  dY = 1

  for i in range(0, len(input_)-len(kernel_)+1, dX):
    for j in range(0, len(input_[0])-len(kernel_[0])+1, dY):
      amount = 0
      for x in range(len(kernel_)):
        for y in range(len(kernel_[0])):
          for z in range(len(kernel_[0][0])):
            amount = amount + input_[x+i, y+j]*kernel_[x, y]         
      result[nX, nY] = amount
      nY = nY + 1
    nX = nX + 1
    nY=0
  return result