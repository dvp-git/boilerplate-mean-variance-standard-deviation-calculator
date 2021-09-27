import numpy as np

def calculate(list):
    # Failure of condition:
  if len(list) < 9:
    raise ValueError('List must contain nine numbers.')
  npa = np.array(list).reshape(3,3)
  calculations = {
    'mean':[ npa.mean(axis=0).tolist() , npa.mean(axis=1).tolist(), npa.mean()],
    'variance':[npa.var(axis=0).tolist() , npa.var(axis=1).tolist(), npa.var()],
    'standard deviation':[npa.std(axis=0).tolist() , npa.std(axis=1).tolist(), npa.std()],
    'max':[npa.max(axis=0).tolist() , npa.max(axis=1).tolist(), npa.max()],
    'min':[npa.min(axis=0).tolist() , npa.min(axis=1).tolist(), npa.min()],
    'sum':[npa.sum(axis=0).tolist() , npa.sum(axis=1).tolist(), npa.sum()]}
  return calculations

