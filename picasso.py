import pickle 
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
from MyUtils import *

with open('/home/victor/Documentos/GitHub/nasdaq/2_weeks_training/2W_43_score.pickle', 'rb') as handle:
    random_score_2W_43 = pickle.load(handle)
with open('/home/victor/Documentos/GitHub/nasdaq/2_weeks_training/2W_74_score.pickle', 'rb') as handle:
    random_score_2W_74 = pickle.load(handle)
with open('/home/victor/Documentos/GitHub/nasdaq/2_weeks_training/2W_59_score.pickle', 'rb') as handle:
    random_score_2W_59 = pickle.load(handle)

with open('/home/victor/Documentos/GitHub/nasdaq/3_weeks_training/3W_43_score.pickle', 'rb') as handle:
    random_score_3W_43 = pickle.load(handle)
with open('/home/victor/Documentos/GitHub/nasdaq/3_weeks_training/3W_74_score.pickle', 'rb') as handle:
    random_score_3W_74 = pickle.load(handle)
with open('/home/victor/Documentos/GitHub/nasdaq/3_weeks_training/3W_59_score.pickle', 'rb') as handle:
    random_score_3W_59 = pickle.load(handle)

with open('/home/victor/Documentos/GitHub/nasdaq/4_weeks_training/4W_43_score.pickle', 'rb') as handle:
    random_score_4W_43 = pickle.load(handle)
with open('/home/victor/Documentos/GitHub/nasdaq/4_weeks_training/4W_74_score.pickle', 'rb') as handle:
    random_score_4W_74 = pickle.load(handle)
with open('/home/victor/Documentos/GitHub/nasdaq/4_weeks_training/4W_59_score.pickle', 'rb') as handle:
    random_score_4W_59 = pickle.load(handle)


with open('/home/victor/Documentos/GitHub/nasdaq/2_weeks_unsup/2W_43_random.pickle', 'rb') as handle:
    optimal_score_2W_43 = pickle.load(handle)
with open('/home/victor/Documentos/GitHub/nasdaq/2_weeks_unsup/2W_74_random.pickle', 'rb') as handle:
    optimal_score_2W_74 = pickle.load(handle)
with open('/home/victor/Documentos/GitHub/nasdaq/2_weeks_unsup/2W_59_random.pickle', 'rb') as handle:
    optimal_score_2W_59 = pickle.load(handle)

with open('/home/victor/Documentos/GitHub/nasdaq/3_weeks_unsup/3W_43_random.pickle', 'rb') as handle:
    optimal_score_3W_43 = pickle.load(handle)
with open('/home/victor/Documentos/GitHub/nasdaq/3_weeks_unsup/3W_74_random.pickle', 'rb') as handle:
    optimal_score_3W_74 = pickle.load(handle)
with open('/home/victor/Documentos/GitHub/nasdaq/3_weeks_unsup/3W_59_random.pickle', 'rb') as handle:
    optimal_score_3W_59 = pickle.load(handle)

with open('/home/victor/Documentos/GitHub/nasdaq/4_weeks_unsup/4W_43_random.pickle', 'rb') as handle:
    optimal_score_4W_43 = pickle.load(handle)
with open('/home/victor/Documentos/GitHub/nasdaq/4_weeks_unsup/4W_74_random.pickle', 'rb') as handle:
    optimal_score_4W_74 = pickle.load(handle)
with open('/home/victor/Documentos/GitHub/nasdaq/4_weeks_unsup/4W_59_random.pickle', 'rb') as handle:
    optimal_score_4W_59 = pickle.load(handle)



#print(random_score_2W_43)
#print(optimal_score_2W_43)
#print(random_score_3W_43)
ff,aa = plt.subplots(3,3, sharex=True, sharey=True, figsize=(8,12))
aa[0][0].set_title("2 weeks, 43 instruments")
MyUtils.make_histo_sup_vs_unsup(random_score_2W_43, optimal_score_2W_43, aa[0][0])
#

aa[0][1].set_title("2 weeks, 59 instruments")
MyUtils.make_histo_sup_vs_unsup(random_score_2W_59, optimal_score_2W_59, aa[0][1])
#ff.tight_layout()

aa[0][2].set_title("2 weeks, 74 instruments")
MyUtils.make_histo_sup_vs_unsup(random_score_2W_74, optimal_score_2W_74, aa[0][2])
#ff.tight_layout()

aa[1][0].set_title("3 weeks, 43 instruments")
MyUtils.make_histo_sup_vs_unsup(random_score_3W_43,optimal_score_3W_43, aa[1][0])
#ff.tight_layout()
aa[1][1].set_title("3 weeks, 59 instruments")
MyUtils.make_histo_sup_vs_unsup(random_score_3W_59, optimal_score_3W_59, aa[1][1])
#ff.tight_layout()
aa[1][2].set_title("3 weeks, 74 instruments")
MyUtils.make_histo_sup_vs_unsup(random_score_3W_74, optimal_score_3W_74, aa[1][2])

aa[2][0].set_title("4 weeks, 43 instruments")
MyUtils.make_histo_sup_vs_unsup(random_score_4W_43, optimal_score_4W_43, aa[2][0])
#ff.tight_layout()
aa[2][1].set_title("4 weeks, 59 instruments")
MyUtils.make_histo_sup_vs_unsup(random_score_4W_59, optimal_score_4W_59, aa[2][1])
#ff.tight_layout()
aa[2][2].set_title("4 weeks, 74 instruments")
MyUtils.make_histo_sup_vs_unsup(random_score_4W_74, optimal_score_4W_74, aa[2][2])
#ff.tight_layout()

ff.tight_layout()

plt.show()


plt.savefig('/home/victor/Documentos/GitHub/nasdaq/sup_vs_unsup_nasdaq.png')