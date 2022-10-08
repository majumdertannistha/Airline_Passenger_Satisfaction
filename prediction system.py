import numpy as np
import pickle
import sklearn
## loading the saved model
loaded_model = pickle.load(open('C:\PROJECT\Pg project\trained_model.sav','rb'))

input_data = (77,821,0,5,1,4,5,4,4,5,4,4,2,4,4,3,1,1,0,0,1)
input_data_as_numpy_Array = np.array(input_data)
input_data_reshaped = input_data_as_numpy_Array.reshape(1,-1)
prediction = loaded_model.predict(input_data_reshaped)
print(prediction[0])
if (prediction[0] == 0) :
    print('The person is not satisfied')
else :
    print('The Person is satisfied')

