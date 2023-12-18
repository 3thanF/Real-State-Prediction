import numpy as np

def UploadData(): # Here we divide the data in x training set and y test set.
    data = np.loadtxt("./HousesData.txt", delimiter=',')
    X = data[:,:4]
    y = data[:,4]
    return X,y    

dlc = dict(dlblue = '#0096ff', dlorange = '#FF9300', dldarkred='#C00000', dlmagenta='#FF40FF', dlpurple='#7030A0')