import numpy as np
import pickle 

with open('/home/victor/Documentos/GitHub/nasdaq/4_weeks_training/4W_74_random.pickle', 'rb') as file:
    loaded_variable = pickle.load(file)

print(loaded_variable)
print(np.mean(list(loaded_variable.values())))
with open('/home/victor/Documentos/GitHub/nasdaq/4_weeks_training/4W_74_score.pickle', 'rb') as file:
    loaded_variable_2 = pickle.load(file)
print(loaded_variable_2)