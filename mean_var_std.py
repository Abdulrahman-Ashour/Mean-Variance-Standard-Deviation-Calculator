import numpy as np

def calculate(list):
  if len(list)!=9:
    raise ValueError('List must contain nine numbers.')
  else:
    cal_mat=np.array(list).reshape(3,3)
  
  mean=[(cal_mat.mean(axis=0).tolist()), (cal_mat.mean(axis=1).tolist()),cal_mat.flatten().mean()]

  variance = [(cal_mat.var(axis=0).tolist()), (cal_mat.var(axis=1).tolist()), (cal_mat.flatten().var())]

  std = [(cal_mat.std(axis=0).tolist()), (cal_mat.std(axis=1).tolist()), (cal_mat.flatten().std())]

  max = [(cal_mat.max(axis=0).tolist()), (cal_mat.max(axis=1).tolist()), (cal_mat.flatten().max())]

  min = [(cal_mat.min(axis=0).tolist()), (cal_mat.min(axis=1).tolist()), (cal_mat.flatten().min())]

  sum = [(cal_mat.sum(axis=0).tolist()), (cal_mat.sum(axis=1).tolist()), (cal_mat.flatten().sum())]

  calculations = {
        "mean": mean,
        "variance": variance,
        "standard deviation": std,
        "max": max,
        "min": min,
        "sum": sum,
  }

  return calculations