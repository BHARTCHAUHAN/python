import numpy as np
ar1=array([1,2,3,4,5,6,7,8,9])
ar2=ar1.array(ar1)
print(ar2)





#1
print(np.__version__)

#2
arr=np.array([1,2,3,4,5])
print(arr.sum())

#3
print(arr.mean())

#4
print(arr.max())

#5
print(arr.min());

#6
print(arr.std());

#7
print(arr.var());

#8
print(arr.shape);

#9
arr=np.array([[1,2,3],[4,5,6]])
print(arr.flatten());

#10
print(arr.reshape(6,1));

#11
arr=np.array([1,2,3,4,5])
print(np.concatenate((arr,arr),axis=0));

#12
print(arr[1:5]);

#13
print(arr[:3]);


#14
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr[1:,1:]);

#15
print(arr[1:,1:3]);

#16
print(arr[:-1, :-1]);

#17
print(arr[[True,False,True], [True,True,False]]);
