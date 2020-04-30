from music21 import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import copy
import fnmatch

from bach import *

myfonts = ['Liberation Sans', 'Arial']
#try:
#    import statsmodels
#except ImportError as e:
#    print ("You need to install statsmodels")

#ALL VERTICAL SEARCH DF
c_1_vt=pd.read_pickle("./bach_pickle_df/c_1_minor_vt.pkl")
csh_1_vt=pd.read_pickle("./bach_pickle_df/csh_1_minor_vt.pkl")
d_1_vt=pd.read_pickle("./bach_pickle_df/d_1_minor_vt.pkl")
dsh_1_vt=pd.read_pickle("./bach_pickle_df/dsh_1_minor_vt.pkl")
e_1_vt=pd.read_pickle("./bach_pickle_df/e_1_minor_vt.pkl")
f_1_vt=pd.read_pickle("./bach_pickle_df/f_1_minor_vt.pkl")
fsh_1_vt=pd.read_pickle("./bach_pickle_df/fsh_1_minor_vt.pkl")
g_1_vt=pd.read_pickle("./bach_pickle_df/g_1_minor_vt.pkl")
gsh_1_vt=pd.read_pickle("./bach_pickle_df/gsh_1_minor_vt.pkl")
a_1_vt=pd.read_pickle("./bach_pickle_df/a_1_minor_vt.pkl")
bfl_1_vt=pd.read_pickle("./bach_pickle_df/bfl_1_minor_vt.pkl")
b_1_vt=pd.read_pickle("./bach_pickle_df/b_1_minor_vt.pkl")



C_1_vt=pd.read_pickle("./bach_pickle_df/C_1_Major_vt.pkl")
Csh_1_vt=pd.read_pickle("./bach_pickle_df/Csh_1_Major_vt.pkl")
D_1_vt=pd.read_pickle("./bach_pickle_df/D_1_Major_vt.pkl")
Efl_1_vt=pd.read_pickle("./bach_pickle_df/Efl_1_Major_vt.pkl")
E_1_vt=pd.read_pickle("./bach_pickle_df/E_1_Major_vt.pkl")
F_1_vt=pd.read_pickle("./bach_pickle_df/F_1_Major_vt.pkl")
Fsh_1_vt=pd.read_pickle("./bach_pickle_df/Fsh_1_Major_vt.pkl")
G_1_vt=pd.read_pickle("./bach_pickle_df/G_1_Major_vt.pkl")
Afl_1_vt=pd.read_pickle("./bach_pickle_df/Afl_1_Major_vt.pkl")
A_1_vt=pd.read_pickle("./bach_pickle_df/A_1_Major_vt.pkl")
Bfl_1_vt=pd.read_pickle("./bach_pickle_df/Bfl_1_Major_vt.pkl")
B_1_vt=pd.read_pickle("./bach_pickle_df/B_1_Major_vt.pkl")

m_vt=[c_1_vt,csh_1_vt,d_1_vt,dsh_1_vt,e_1_vt,f_1_vt,fsh_1_vt,g_1_vt,gsh_1_vt,a_1_vt,bfl_1_vt,b_1_vt]
M_vt=[C_1_vt,Csh_1_vt,D_1_vt,Efl_1_vt,E_1_vt,F_1_vt,Fsh_1_vt,G_1_vt,Afl_1_vt,A_1_vt,Bfl_1_vt,B_1_vt]

m_vt_circle=circle_sort(m_vt)
M_vt_circle=circle_sort(M_vt)

#without keys
m_vt_concat=pd.concat(m_vt)
M_vt_concat=pd.concat(M_vt)

all_vt_concat=pd.concat([M_vt_concat,m_vt_concat])

#with keys
m_vt_concat_wk=pd.concat(m_vt,keys=wtc_1_m_names)
M_vt_concat_wk=pd.concat(M_vt,keys=wtc_1_M_names)

all_vt_concat=pd.concat([M_vt_concat_wk,m_vt_concat_wk])


#VERTICAL TRANSPOSED SEARCHES DF
# rodent=np.array([i.split('_')[0] for i in wtc_1_m_names])
# rodent2=np.array(m_titles)
# crodent=np.column_stack((np.array([i.split('_')[0] for i in wtc_1_m_names]),np.array(m_titles)))

#TRANSPOSITIONS
#name all transposed fugues
#organize and create lists by fugue
#example of fugue variable: b_1_to_dsh_vt
#example of list: c_1_vt_T , list of c_1 fugue transposed to all 12 keys
for fg in wtc_1_m_names:
	exec(f"{fg}_vt_T" + '=[]')
	for ky in np.column_stack((np.array([i.split('_')[0] for i in wtc_1_m_names]),np.array(m_titles))):
		pklfile=pd.read_pickle(f'./bach_pickle_df/{fg}_minor_to_{ky[1]}_vt.pkl')
		exec(f"{fg}_to_{ky[0]}_vt" + ' = pklfile')
		exec(f"{fg}_vt_T" + '.append(pklfile)')
	exec(f"{fg}_vt_T_concat" + f'= pd.concat({fg}_vt_T)')

for fg in wtc_1_M_names:
	exec(f"{fg}_vt_T" + '=[]')
	for ky in np.column_stack((np.array([i.split('_')[0] for i in wtc_1_M_names]),np.array(M_titles))):
		pklfile=pd.read_pickle(f'./bach_pickle_df/{fg}_Major_to_{ky[1]}_vt.pkl')
		exec(f"{fg}_to_{ky[0]}_vt" + ' = pklfile')
		exec(f"{fg}_vt_T" + '.append(pklfile)')
	exec(f"{fg}_vt_T_concat" + f'= pd.concat({fg}_vt_T)')

#organize and create list by key
#example of list: fg_1_to_c_vt , list of all 12 fugues transposed to the key of c minor

av_m_vt=[]
av_m_vt_nc=[]
for ky in np.column_stack((np.array([i.split('_')[0] for i in wtc_1_m_names]),np.array(m_titles))):
    exec(f"fg_1_to_{ky[0]}_vt" + '=[]')
    for fg in wtc_1_m_names:
        pklfile=pd.read_pickle(f'./bach_pickle_df/{fg}_minor_to_{ky[1]}_vt.pkl')
        exec(f"fg_1_to_{ky[0]}_vt" + '.append(pklfile)')
    exec(f"fg_1_to_{ky[0]}_vt_concat" + f'= pd.concat(fg_1_to_{ky[0]}_vt)')
    exec(f"fg_1_to_{ky[0]}_vt_concat['N norm duration']" + f'= fg_1_to_{ky[0]}_vt_concat["norm duration"]/sum(fg_1_to_{ky[0]}_vt_concat["norm duration"])') #
    exec("av_m_vt" + f'.append(fg_1_to_{ky[0]}_vt_concat)')
    exec("av_m_vt_nc" + f'.append(fg_1_to_{ky[0]}_vt)')

av_M_vt=[]
av_M_vt_nc=[]
for ky in np.column_stack((np.array([i.split('_')[0] for i in wtc_1_M_names]),np.array(M_titles))):
    exec(f"fg_1_to_{ky[0]}_vt" + '=[]')
    for fg in wtc_1_M_names:
        pklfile=pd.read_pickle(f'./bach_pickle_df/{fg}_Major_to_{ky[1]}_vt.pkl')
        exec(f"fg_1_to_{ky[0]}_vt" + '.append(pklfile)')
    exec(f"fg_1_to_{ky[0]}_vt_concat" + f'= pd.concat(fg_1_to_{ky[0]}_vt)')
    exec(f"fg_1_to_{ky[0]}_vt_concat['N norm duration']" + f'= fg_1_to_{ky[0]}_vt_concat["norm duration"]/sum(fg_1_to_{ky[0]}_vt_concat["norm duration"])') #
    exec("av_M_vt" + f'.append(fg_1_to_{ky[0]}_vt_concat)')
    exec("av_M_vt_nc" + f'.append(fg_1_to_{ky[0]}_vt)')


#ALL HORIZONTAL SEARCH DF
c_1_hz=pd.read_pickle("./bach_pickle_df/c_1_minor_hz.pkl")
csh_1_hz=pd.read_pickle("./bach_pickle_df/csh_1_minor_hz.pkl")
d_1_hz=pd.read_pickle("./bach_pickle_df/d_1_minor_hz.pkl")
dsh_1_hz=pd.read_pickle("./bach_pickle_df/dsh_1_minor_hz.pkl")
e_1_hz=pd.read_pickle("./bach_pickle_df/e_1_minor_hz.pkl")
f_1_hz=pd.read_pickle("./bach_pickle_df/f_1_minor_hz.pkl")
fsh_1_hz=pd.read_pickle("./bach_pickle_df/fsh_1_minor_hz.pkl")
g_1_hz=pd.read_pickle("./bach_pickle_df/g_1_minor_hz.pkl")
gsh_1_hz=pd.read_pickle("./bach_pickle_df/gsh_1_minor_hz.pkl")
a_1_hz=pd.read_pickle("./bach_pickle_df/a_1_minor_hz.pkl")
bfl_1_hz=pd.read_pickle("./bach_pickle_df/bfl_1_minor_hz.pkl")
b_1_hz=pd.read_pickle("./bach_pickle_df/b_1_minor_hz.pkl")

C_1_hz=pd.read_pickle("./bach_pickle_df/C_1_Major_hz.pkl")
Csh_1_hz=pd.read_pickle("./bach_pickle_df/Csh_1_Major_hz.pkl")
D_1_hz=pd.read_pickle("./bach_pickle_df/D_1_Major_hz.pkl")
Efl_1_hz=pd.read_pickle("./bach_pickle_df/Efl_1_Major_hz.pkl")
E_1_hz=pd.read_pickle("./bach_pickle_df/E_1_Major_hz.pkl")
F_1_hz=pd.read_pickle("./bach_pickle_df/F_1_Major_hz.pkl")
Fsh_1_hz=pd.read_pickle("./bach_pickle_df/Fsh_1_Major_hz.pkl")
G_1_hz=pd.read_pickle("./bach_pickle_df/G_1_Major_hz.pkl")
Afl_1_hz=pd.read_pickle("./bach_pickle_df/Afl_1_Major_hz.pkl")
A_1_hz=pd.read_pickle("./bach_pickle_df/A_1_Major_hz.pkl")
Bfl_1_hz=pd.read_pickle("./bach_pickle_df/Bfl_1_Major_hz.pkl")
B_1_hz=pd.read_pickle("./bach_pickle_df/B_1_Major_hz.pkl")

m_hz=[c_1_hz,csh_1_hz,d_1_hz,dsh_1_hz,e_1_hz,f_1_hz,fsh_1_hz,g_1_hz,gsh_1_hz,a_1_hz,bfl_1_hz,b_1_hz]
M_hz=[C_1_hz,Csh_1_hz,D_1_hz,Efl_1_hz,E_1_hz,F_1_hz,Fsh_1_hz,G_1_hz,Afl_1_hz,A_1_hz,Bfl_1_hz,B_1_hz]

m_hz_circle=circle_sort(m_hz)
M_hz_circle=circle_sort(M_hz)

#without keys
m_hz_concat=pd.concat(m_hz)
M_hz_concat=pd.concat(M_hz)

all_hz_concat=pd.concat([M_hz_concat,m_hz_concat])

#with keys
m_hz_concat_wk=pd.concat(m_hz,keys=wtc_1_m_names)
M_hz_concat_wk=pd.concat(M_hz,keys=wtc_1_M_names)

all_hz_concat_wk=pd.concat([M_hz_concat_wk,m_hz_concat_wk])


#HORIZONTAL TRANSPOSED SEARCHES DF
# rodent=np.array([i.split('_')[0] for i in wtc_1_m_names])
# rodent2=np.array(m_titles)
# crodent=np.column_stack((np.array([i.split('_')[0] for i in wtc_1_m_names]),np.array(m_titles)))


#example of fugue variable: b_1_to_dsh_hz
#example of list: c_1_hz_T , list of c_1 fugue transposed to all 12 keys
for fg in wtc_1_m_names:
	exec(f"{fg}_hz_T" + '=[]')
	for ky in np.column_stack((np.array([i.split('_')[0] for i in wtc_1_m_names]),np.array(m_titles))):
		pklfile=pd.read_pickle(f'./bach_pickle_df/{fg}_minor_to_{ky[1]}_hz.pkl')
		exec(f"{fg}_to_{ky[0]}_hz" + ' = pklfile')
		exec(f"{fg}_hz_T" + '.append(pklfile)')
	exec(f"{fg}_hz_T_concat" + f'= pd.concat({fg}_hz_T)')

for fg in wtc_1_M_names:
	exec(f"{fg}_hz_T" + '=[]')
	for ky in np.column_stack((np.array([i.split('_')[0] for i in wtc_1_M_names]),np.array(M_titles))):
		pklfile=pd.read_pickle(f'./bach_pickle_df/{fg}_Major_to_{ky[1]}_hz.pkl')
		exec(f"{fg}_to_{ky[0]}_hz" + ' = pklfile')
		exec(f"{fg}_hz_T" + '.append(pklfile)')
	exec(f"{fg}_hz_T_concat" + f'= pd.concat({fg}_hz_T)')
		

#organize and create list by key
#example of list: fg_1_to_c_hz , list of all 12 fugues transposed to the key of c minor

av_m_hz=[]
av_m_hz_nc=[]
for ky in np.column_stack((np.array([i.split('_')[0] for i in wtc_1_m_names]),np.array(m_titles))):
    exec(f"fg_1_to_{ky[0]}_hz" + '=[]')
    for fg in wtc_1_m_names:
        pklfile=pd.read_pickle(f'./bach_pickle_df/{fg}_minor_to_{ky[1]}_hz.pkl')
        exec(f"fg_1_to_{ky[0]}_hz" + '.append(pklfile)')
    exec(f"fg_1_to_{ky[0]}_hz_concat" + f'= pd.concat(fg_1_to_{ky[0]}_hz)')
    exec(f"fg_1_to_{ky[0]}_hz_concat['N av dur norm']" + f'= fg_1_to_{ky[0]}_hz_concat["av dur norm"]/sum(fg_1_to_{ky[0]}_hz_concat["av dur norm"])') #
    exec("av_m_hz" + f'.append(fg_1_to_{ky[0]}_hz_concat)')
    exec("av_m_hz_nc" + f'.append(fg_1_to_{ky[0]}_hz)')

av_M_hz=[]
av_M_hz_nc=[]
for ky in np.column_stack((np.array([i.split('_')[0] for i in wtc_1_M_names]),np.array(M_titles))):
    exec(f"fg_1_to_{ky[0]}_hz" + '=[]')
    for fg in wtc_1_M_names:
        pklfile=pd.read_pickle(f'./bach_pickle_df/{fg}_Major_to_{ky[1]}_hz.pkl')
        exec(f"fg_1_to_{ky[0]}_hz" + '.append(pklfile)')
    exec(f"fg_1_to_{ky[0]}_hz_concat" + f'= pd.concat(fg_1_to_{ky[0]}_hz)')
    exec(f"fg_1_to_{ky[0]}_hz_concat['N av dur norm']" + f'= fg_1_to_{ky[0]}_hz_concat["av dur norm"]/sum(fg_1_to_{ky[0]}_hz_concat["av dur norm"])') #
    exec("av_M_hz" + f'.append(fg_1_to_{ky[0]}_hz_concat)')
    exec("av_M_hz_nc" + f'.append(fg_1_to_{ky[0]}_hz)')

# m_vt_circle=[f_1_vt,bfl_1_vt,dsh_1_vt,gsh_1_vt,csh_1_vt,fsh_1_vt,b_1_vt,e_1_vt,a_1_vt,d_1_vt,g_1_vt,c_1_vt]
# M_vt_circle=[F_1_vt,Bfl_1_vt,Efl_1_vt,Afl_1_vt,Csh_1_vt,Fsh_1_vt,B_1_vt,E_1_vt,A_1_vt,D_1_vt,G_1_vt,C_1_vt]

m_circle_names=circle_sort(wtc_1_m_names)
M_circle_names=circle_sort(wtc_1_M_names) 

m_circle_titles=circle_sort(m_titles)
M_circle_titles=circle_sort(M_titles)

pd.options.display.max_columns = None



#ALL VERTICAL SEARCH DF FOR PRELUDES BOOK 1
# m_vt_p=[]
# for fg in wtc_1_m_names_p:
#     pklfile=pd.read_pickle(f'./bach_pickle_df_p/{fg}_minor_vt.pkl')
#     exec(f"{fg}_vt" + ' = pklfile')
#     m_vt_p.append(pklfile)

# m_vt_circle_p=circle_sort(m_vt_p)
# m_vt_concat_p=pd.concat(m_vt_p)

# M_vt_p=[]
# for fg in wtc_1_M_names_p:
#     pklfile=pd.read_pickle(f'./bach_pickle_df_p/{fg}_Major_vt.pkl')
#     exec(f"{fg}_vt" + ' = pklfile')
#     M_vt_p.append(pklfile)

# M_vt_circle_p=circle_sort(M_vt_p)
# M_vt_concat_p=pd.concat(M_vt_p)

# #VERTICAL TRANSPOSED SEARCHES DF

# for fg in wtc_1_m_names_p:
# 	exec(f"{fg}_vt_T" + '=[]')
# 	for ky in np.column_stack((np.array([i.split('_')[0] for i in wtc_1_m_names_p]),np.array(m_titles_p))):
# 		pklfile=pd.read_pickle(f'./bach_pickle_df_p/{fg}_minor_to_{ky[1]}_vt.pkl')
# 		exec(f"{fg}_to_{ky[0]}_vt" + ' = pklfile')
# 		exec(f"{fg}_vt_T" + '.append(pklfile)')
# 	exec(f"{fg}_vt_T_concat" + f'= pd.concat({fg}_vt_T)')

# for fg in wtc_1_M_names_p:
# 	exec(f"{fg}_vt_T" + '=[]')
# 	for ky in np.column_stack((np.array([i.split('_')[0] for i in wtc_1_M_names_p]),np.array(M_titles_p))):
# 		pklfile=pd.read_pickle(f'./bach_pickle_df_p/{fg}_Major_to_{ky[1]}_vt.pkl')
# 		exec(f"{fg}_to_{ky[0]}_vt" + ' = pklfile')
# 		exec(f"{fg}_vt_T" + '.append(pklfile)')
# 	exec(f"{fg}_vt_T_concat" + f'= pd.concat({fg}_vt_T)')

# #organize and create list by key
# #example of list: fg_1_to_c_vt , list of all 12 fugues transposed to the key of c minor

# av_m_vt_p=[]
# for ky in np.column_stack((np.array([i.split('_')[0] for i in wtc_1_m_names_p]),np.array(m_titles_p))):
#     exec(f"fg_1_to_{ky[0]}_vt_p" + '=[]')
#     for fg in wtc_1_m_names_p:
#         pklfile=pd.read_pickle(f'./bach_pickle_df_p/{fg}_minor_to_{ky[1]}_vt.pkl')
#         exec(f"fg_1_to_{ky[0]}_vt_p" + '.append(pklfile)')
#     exec(f"fg_1_to_{ky[0]}_vt_p_concat" + f'= pd.concat(fg_1_to_{ky[0]}_vt_p)')
#     exec("av_m_vt_p" + f'.append(fg_1_to_{ky[0]}_vt_p_concat)')

# av_M_vt_p=[]
# for ky in np.column_stack((np.array([i.split('_')[0] for i in wtc_1_M_names_p]),np.array(M_titles_p))):
#     exec(f"fg_1_to_{ky[0]}_vt_p" + '=[]')
#     for fg in wtc_1_M_names_p:
#         pklfile=pd.read_pickle(f'./bach_pickle_df_p/{fg}_Major_to_{ky[1]}_vt.pkl')
#         exec(f"fg_1_to_{ky[0]}_vt_p" + '.append(pklfile)')
#     exec(f"fg_1_to_{ky[0]}_vt_p_concat" + f'= pd.concat(fg_1_to_{ky[0]}_vt_p)')
#     exec("av_M_vt_p" + f'.append(fg_1_to_{ky[0]}_vt_p_concat)')

# m_circle_names_p=circle_sort(wtc_1_m_names_p)
# M_circle_names_p=circle_sort(wtc_1_M_names_p) 

# m_circle_titles_p=circle_sort(m_titles_p)
# M_circle_titles_p=circle_sort(M_titles_p)

