from music21 import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import copy
import fnmatch
from collections import Counter

environment.set('autoDownload', 'allow')

eps=np.finfo(float).eps 

#humdrum kern files:
    #http://kern.humdrum.org/search?s=t&keyword=bach+wtc&type=Text

#WTC 1 fugue files:

C_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f01.krn&f=kern')
c_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f02.krn&f=kern')
Csh_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f03.krn&f=kern')
csh_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f04.krn&f=kern')
D_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f05.krn&f=kern')
d_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f06.krn&f=kern')
Efl_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f07.krn&f=kern')
dsh_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f08.krn&f=kern')
E_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f09.krn&f=kern')
e_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f10.krn&f=kern')
F_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f11.krn&f=kern')
f_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f12.krn&f=kern')
Fsh_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f13.krn&f=kern')
fsh_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f14.krn&f=kern')
G_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f15.krn&f=kern')
g_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f16.krn&f=kern')
Afl_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f17.krn&f=kern')
gsh_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f18.krn&f=kern')
A_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f19.krn&f=kern')
a_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f20.krn&f=kern')
Bfl_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f21.krn&f=kern')
bfl_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f22.krn&f=kern')
B_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f23.krn&f=kern')
b_1=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f24.krn&f=kern')


if len(a_1.parts)==5:
    a_1.remove(a_1.parts[0])

#WTC 2 fugue files:

C_2 =converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f01.krn&f=kern')
c_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f02.krn&f=kern')
Csh_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f03.krn&f=kern')
csh_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f04.krn&f=kern')
D_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f05.krn&f=kern')
d_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f06.krn&f=kern')
Efl_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f07.krn&f=kern')
dsh_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f08.krn&f=kern')
E_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f09.krn&f=kern')
e_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f10.krn&f=kern')
F_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f11.krn&f=kern')
f_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f12.krn&f=kern')
Fsh_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f13.krn&f=kern')
fsh_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f14.krn&f=kern')
G_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f15.krn&f=kern')
g_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f16.krn&f=kern')
Afl_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f17.krn&f=kern')
gsh_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f18.krn&f=kern')
A_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f19.krn&f=kern')
a_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f20.krn&f=kern')
Bfl_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f21.krn&f=kern')
bfl_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f22.krn&f=kern')
B_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f23.krn&f=kern')
b_2=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-2&file=wtc2f24.krn&f=kern')

wtc_1=[C_1,c_1,Csh_1,csh_1,D_1,d_1,Efl_1,dsh_1,E_1,e_1,F_1,f_1,Fsh_1,fsh_1,G_1,g_1,Afl_1,gsh_1,A_1,a_1,Bfl_1,bfl_1,B_1,b_1]
wtc_1_names=['C_1','c_1','Csh_1','csh_1','D_1','d_1','Efl_1','dsh_1','E_1','e_1','F_1','f_1','Fsh_1','fsh_1','G_1','g_1','Afl_1','gsh_1','A_1','a_1','Bfl_1','bfl_1','B_1','b_1']

wtc_2=[C_2,c_2,Csh_2,csh_2,D_2,d_2,Efl_2,dsh_2,E_2,e_2,F_2,f_2,Fsh_2,fsh_2,G_2,g_2,Afl_2,gsh_2,A_2,a_2,Bfl_2,bfl_2,B_2,b_2]
wtc_2_names=['C_2','c_2','Csh_2','csh_2','D_2','d_2','Efl_2','dsh_2','E_2','e_2','F_2','f_2','Fsh_2','fsh_2','G_2','g_2','Afl_2','gsh_2','A_2','a_2','Bfl_2','bfl_2','B_2','b_2']

wtc_1_M=wtc_1[0::2]
wtc_1_M_names=wtc_1_names[0::2]

wtc_1_m=wtc_1[1::2]
wtc_1_m_names=wtc_1_names[1::2]

wtc_1_m_pure=[e_1,a_1,d_1]
wtc_1_m_pythag=[f_1,bfl_1,dsh_1]

wtc_1_minor=[c_1,csh_1,d_1,dsh_1,e_1,f_1,fsh_1,g_1,gsh_1,a_1,bfl_1,b_1]
wtc_1_major=[C_1,Csh_1,D_1,Efl_1,E_1,F_1,Fsh_1,G_1,Afl_1,A_1,Bfl_1,B_1]

m_titles=['c','c#','d','d#','e','f','f#','g','g#','a','b-','b']
M_titles=['C','C#','D','E-','E','F','F#','G','A-','A','B-','B']

m2_cents=[90,96,102,108]
M2_cents=[192,198,204]
m3_cents=[294,300,306,312]
M3_cents=[390,396,402,408]
P4_cents=[498,504]
TT_cents=[588,594,600,606,612]
P5_cents=[696,702]
m6_cents=[792,798,804,810]
M6_cents=[888,894,900,906]
m7_cents=[996,1002,1008]
M7_cents=[1092,1098,1104,1110]

#WTC I preludes - xml files, cannot view score via show(), but show('midi') is functioning, and dataframe objects should be accurate

# C_1_p=converter.parse('./wtc_1_preludes/wtc1p01.mxl')
# c_1_p=converter.parse('./wtc_1_preludes/wtc1p02.mxl')
# Csh_1_p=converter.parse('./wtc_1_preludes/wtc1p03.mxl')
# csh_1_p=converter.parse('./wtc_1_preludes/wtc1p04.mxl')
# D_1_p=converter.parse('./wtc_1_preludes/wtc1p05.mxl')
# d_1_p=converter.parse('./wtc_1_preludes/wtc1p06.mxl')
# Efl_1_p=converter.parse('./wtc_1_preludes/wtc1p07.mxl')
# efl_1_p=converter.parse('./wtc_1_preludes/wtc1p08.mxl')
# E_1_p=converter.parse('./wtc_1_preludes/wtc1p09.mxl')
# e_1_p=converter.parse('./wtc_1_preludes/wtc1p10.mxl')
# F_1_p=converter.parse('./wtc_1_preludes/wtc1p11.mxl')
# f_1_p=converter.parse('./wtc_1_preludes/wtc1p12.mxl')
# Fsh_1_p=converter.parse('./wtc_1_preludes/wtc1p13.mxl')
# fsh_1_p=converter.parse('./wtc_1_preludes/wtc1p14.mxl')
# G_1_p=converter.parse('./wtc_1_preludes/wtc1p15.mxl')
# g_1_p=converter.parse('./wtc_1_preludes/wtc1p16.mxl')
# Afl_1_p=converter.parse('./wtc_1_preludes/wtc1p17.mxl')
# gsh_1_p=converter.parse('./wtc_1_preludes/wtc1p18.mxl')
# A_1_p=converter.parse('./wtc_1_preludes/wtc1p19.mxl')
# a_1_p=converter.parse('./wtc_1_preludes/wtc1p20.mxl')
# Bfl_1_p=converter.parse('./wtc_1_preludes/wtc1p21.mxl')
# bfl_1_p=converter.parse('./wtc_1_preludes/wtc1p22.mxl')
# B_1_p=converter.parse('./wtc_1_preludes/wtc1p23.mxl')
# b_1_p=converter.parse('./wtc_1_preludes/wtc1p24.mxl')

# wtc_1_p=[C_1_p,c_1_p,Csh_1_p,csh_1_p,D_1_p,d_1_p,Efl_1_p,efl_1_p,E_1_p,e_1_p,F_1_p,f_1_p,Fsh_1_p,fsh_1_p,G_1_p,g_1_p,Afl_1_p,gsh_1_p,A_1_p,a_1_p,Bfl_1_p,bfl_1_p,B_1_p,b_1_p]
# wtc_1_names_p=['C_1_p','c_1_p','Csh_1_p','csh_1_p','D_1_p','d_1_p','Efl_1_p','efl_1_p','E_1_p','e_1_p','F_1_p','f_1_p','Fsh_1_p','fsh_1_p','G_1_p','g_1_p','Afl_1_p','gsh_1_p','A_1_p','a_1_p','Bfl_1_p','bfl_1_p','B_1_p','b_1_p']

# wtc_1_M_p=wtc_1_p[0::2]
# wtc_1_m_p=wtc_1_p[1::2]
# wtc_1_M_names_p=wtc_1_names_p[0::2]
# wtc_1_m_names_p=wtc_1_names_p[1::2]

# wtc_1_m_pure_p=[e_1_p,a_1_p,d_1_p]
# wtc_1_m_pythag_p=[f_1_p,bfl_1_p,efl_1_p]

# m_titles_p=['c','c#','d','e-','e','f','f#','g','g#','a','b-','b']
# M_titles_p=['C','C#','D','E-','E','F','F#','G','A-','A','B-','B']


#functions
def md(s):
    ss=copy.deepcopy(s)
    st=stream.Stream()
    st.append(note.Rest())
    st.append(ss)
    pl=st.show('midi')
    
    return pl

def trans_title(title_list,new_key_string):
    t_title=[f'{title_list[i]} to {new_key_string}' for i in range(len(title_list))]
    return t_title

def file_name(file):
    if file in wtc_1:
        d=wtc_1_names[wtc_1.index(file)]
    elif file in wtc_2:
        d=wtc_2_names[wtc_2.index(file)]
    elif file in wtc_1_p:
        d=wtc_1_names_p[wtc_1_p.index(file)]
    else:
        d=print('sorry rodent')
    return d

def circle_sort(df):
    order=[5,10,3,8,1,6,11,4,9,2,7,0]
    circle_df=[df[i] for i in order]
    return circle_df

def change_width(ax, new_value) :
    for patch in ax.patches :
        current_width = patch.get_width()
        diff = current_width - new_value

        #change the bar width
        patch.set_width(new_value)

        #recenter the bar
        patch.set_x(patch.get_x() + diff * .5)

def cents_from_just(n1,n2): 
    
    JI=np.array([0,112,204,316,386,498,590,702,814,884,996,1088])
    JIF=pd.DataFrame(JI)
    diff=round(abs(interval.Interval(n1,n2).cents))%1200-JIF.loc[round(abs(interval.Interval(n1,n2).semitones))%12][0]
    
    return diff

def bound_trans(value,max_new=1,min_new=.2,max_old=22,min_old=0):
    
    alpha=(((max_new-min_new)/(max_old-min_old))*(value-max_old))+max_new
    return alpha

def flat_sharp(n):
    if n<0:
        fs='flat'
    elif n==0:
        fs='pure'
    elif n>0:
        fs='sharp'
    
    return fs

def flatten_list(ls, flattened_list=[]):
    for elem in ls:
        if not isinstance(elem, list): 
            flattened_list.append(elem)
        else:
            flatten_list(elem, flattened_list)
    return flattened_list

#get chromatic scale degrees, for ky from dataframe provide str(n_df.iloc[0]["key"].split()[0])
#for solfege option
# sc = scale.MajorScale('f#')
# sc.solfeg('a')
def sc_degree(ky,p):
    sc = scale.ChromaticScale(ky)
    sc_d=sc.getScaleDegreeFromPitch(p,comparisonAttribute='pitchClass')-1
    
    return sc_d
#code to run to obtain scale degrees for df
# for n_df in m_hz:
#     for i in range(len(n_df)):
#         n_df.loc[n_df.index[i], 'sc degree']=sc_degree(str(n_df.iloc[0]["key"].split()[0]),str(n_df['n1 name'].iloc[i]))

def get_spine(n):

    sp=[]
    sp.append([(i.site.id) for i in n.contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])
    sp=flatten_list(sp,[])
    if len(sp)>0:
        sp=list(set(sp))[0]
        sp=int(sp.split('_')[1])
    else:
        sp=-9

    return sp

def get_spine_v(n):
    try:
        sp=int(n.split('_')[1])
    except:
        sp=-9
    
    return sp

def get_tie(n):
    try:
        ttype=n.tie.type
    except AttributeError:
        ttype='none'
    
    return ttype

def get_subjects(file):
    
    if file==C_1:
        f=C_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[1][0:10])
        searchlist[0].duration=search.WildcardDuration()     

        searchlist2=[note.Note(i) for i in ['E','F#','G','G','A','G','F#','D','G'] ]

        C_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notes)
            C_subjectpartlist_separate.append(individualpartlist)

        #get missing bass subject entry at m.20
        C_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.filterNotes=True
            ss2.algorithms.append(search.StreamSearcher.noteNameAlgorithm)
            subjects2=ss2.run()
            individualpartlist2=[]
            for results in subjects2:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                individualpartlist2.append(partstream2.recurse().notes)
            C_subjectpartlist_separate2.append(individualpartlist2)

        for i in range(len(C_subjectpartlist_separate2)):
            for j in range(len(C_subjectpartlist_separate2[i])):
                C_subjectpartlist_separate[i].append(C_subjectpartlist_separate2[i][j])

        C_subjects=C_subjectpartlist_separate
        thesubjects=C_subjects
        
    elif file==c_1:
        f=c_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[1][0:20])
        searchlist[-1].duration=search.WildcardDuration() 

        c_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notes)
            c_subjectpartlist_separate.append(individualpartlist)

        c_subjects=c_subjectpartlist_separate 
        thesubjects=c_subjects
        
    elif file==Csh_1:
        f=Csh_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[0][0:17])
        searchlist[0].duration=search.WildcardDuration()
        searchlist[-1].duration=search.WildcardDuration()

        Csh_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notes)
            Csh_subjectpartlist_separate.append(individualpartlist)

        searchlist2=copy.deepcopy(partList[0][0:11])
        searchlist2[0].duration=search.WildcardDuration()
        searchlist2[-1].duration=search.WildcardDuration()

        Csh_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.filterNotes=True
            ss2.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss2.run()

            individualpartlist2=[]
            for results in subjects:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                individualpartlist2.append(partstream2.recurse().notes)
            Csh_subjectpartlist_separate2.append(individualpartlist2)

        Csh_subjectpartlist_separate[0].append(Csh_subjectpartlist_separate2[0][2])
        Csh_subjectpartlist_separate[0].append(Csh_subjectpartlist_separate2[0][3])
        Csh_subjectpartlist_separate[0].append(Csh_subjectpartlist_separate2[0][5])
        Csh_subjectpartlist_separate[0].append(Csh_subjectpartlist_separate2[0][6])
        Csh_subjectpartlist_separate[0].append(Csh_subjectpartlist_separate2[0][7])
        Csh_subjectpartlist_separate[2].append(Csh_subjectpartlist_separate2[2][-4])
        Csh_subjectpartlist_separate[2].append(Csh_subjectpartlist_separate2[2][-3])
        Csh_subjectpartlist_separate[2].append(Csh_subjectpartlist_separate2[2][-2])

        Csh_subjects=Csh_subjectpartlist_separate 
        thesubjects=Csh_subjects
        
    elif file==csh_1:
        f=csh_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[4][0:5])
        searchlist[0].duration=search.WildcardDuration()
        searchlist[-1].duration=search.WildcardDuration()
        searchlist[-2].duration=search.WildcardDuration()

        csh_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                if partstream1[0].pitch.ps>partstream1[1].pitch.ps and partstream1[2].pitch.ps>partstream1[0].pitch.ps and partstream1[2].pitch.ps>=partstream1[3].pitch.ps and partstream1[3].pitch.ps>=partstream1[0].pitch.ps:
                    individualpartlist.append(partstream1)
            csh_subjectpartlist_separate.append(individualpartlist)

        csh_subjectpartlist_separate[2].pop(-2)
        csh_subjectpartlist_separate[2].pop(1)
        csh_subjectpartlist_separate[1].pop(3)
        csh_subjectpartlist_separate[1].pop(2)
        csh_subjectpartlist_separate[1].pop(1)
        csh_subjectpartlist_separate[0].pop(2)

        csh_subjectpartlist_separate[0][3].pop(-1) #possible no pop
        csh_subjectpartlist_separate[0][6].pop(-1)
        csh_subjectpartlist_separate[0][7].pop(-1)
        csh_subjectpartlist_separate[1][3].pop(-1)
        csh_subjectpartlist_separate[3][6].pop(-1)

        searchlist2=copy.deepcopy(partList[3][105:113])
        searchlist2[-1].duration=search.WildcardDuration()
        searchlist2[-2].duration=search.WildcardDuration()
        #searchlist[3].duration=search.WildcardDuration()

        csh_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.filterNotes=True
            ss2.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss2.run()

            individualpartlist2=[]
            for results in subjects:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                if partstream2[1]==partstream2[2] and partstream2[2]==partstream2[3] and partstream2[1]==partstream2[3]:
                    individualpartlist2.append(partstream2)
            csh_subjectpartlist_separate2.append(individualpartlist2)

        csh_subjectpartlist_separate2[1][6].pop(-1) 
        csh_subjectpartlist_separate2[2][1].pop(-1)
        csh_subjectpartlist_separate2[2][4].pop(-1)
        csh_subjectpartlist_separate2[2][6].pop(-1)
        csh_subjectpartlist_separate2[3][3].pop(-1)
        csh_subjectpartlist_separate2[4][2].pop(-1)
        csh_subjectpartlist_separate2[4][5].pop(-1)

        for i in range(len(csh_subjectpartlist_separate2)):
            for j in range(len(csh_subjectpartlist_separate2[i])):
                csh_subjectpartlist_separate[i].append(csh_subjectpartlist_separate2[i][j])

        searchlist3=copy.deepcopy(partList[2][279:])

        csh_subjectpartlist_separate3=[]

        for part in partList:
            ss3=search.StreamSearcher(part,searchlist3)
            ss3.recurse=True
            ss3.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss3.run()

            individualpartlist3=[]
            for results in subjects:
                partstream3=stream.Stream()
                partstream3.append(list(results.els))
                individualpartlist3.append(partstream3)

            csh_subjectpartlist_separate3.append(individualpartlist3)

        csh_subjectpartlist_separate[2].append(csh_subjectpartlist_separate2[2][0])

        csh_subjects=csh_subjectpartlist_separate 
        thesubjects=csh_subjects
        
    elif file==D_1:
        f=D_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[3][0:13])
        searchlist[0].duration=search.WildcardDuration()
        searchlist[-1].duration=search.WildcardDuration()

        D_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notes)
            D_subjectpartlist_separate.append(individualpartlist)

        D_subjectpartlist_separate[3].pop(-1)
        D_subjectpartlist_separate[3].pop(-2)
        D_subjectpartlist_separate[0].pop(-1)
        D_subjectpartlist_separate[0].pop(-1)

        D_subjects=D_subjectpartlist_separate  
        thesubjects=D_subjects
        
    elif file==d_1:
        f=d_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[0][0:12])
        searchlist[0].duration=search.WildcardDuration()
        searchlist[-1].duration=search.WildcardDuration()

        d_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notes)
            d_subjectpartlist_separate.append(individualpartlist)

        #for bass entry at m.34

        searchlist2=[note.Note(i) for i in ['D','E','F#','G','E','F#','D','C#','D','B-','A','G','B-','A']]

        d_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.filterNotes=True
            ss2.algorithms.append(search.StreamSearcher.noteNameAlgorithm)
            subjects2=ss2.run()
            individualpartlist2=[]
            for results in subjects2:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                individualpartlist2.append(partstream2.recurse().notes)
            d_subjectpartlist_separate2.append(individualpartlist2)

        d_subjectpartlist_separate[2].append(d_subjectpartlist_separate2[2][0])

        d_subjects=d_subjectpartlist_separate    
        thesubjects=d_subjects
        
    elif file==Efl_1:
        f=Efl_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[0][0:16])
        searchlist[-1].duration=search.WildcardDuration()

        Efl_subjectpartlist=[]
        Efl_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notes)
            Efl_subjectpartlist_separate.append(individualpartlist)

        Efl_subjects=Efl_subjectpartlist_separate    
        thesubjects=Efl_subjects
    
    elif file==dsh_1:
        f=dsh_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notesAndRests)

        searchlist=copy.deepcopy(partList[1][0:14])
        searchlist[0].duration=search.WildcardDuration()

        nums=list(range(7,14))
        for i in nums:
            searchlist[i].duration=search.WildcardDuration()

        searchlist2=copy.deepcopy(partList[0][3:17])
        searchlist2[0].duration=search.WildcardDuration()

        nums=list(range(7,14))
        for i in nums:
            searchlist2[i].duration=search.WildcardDuration()    

        dsh_subjectpartlist_separate=[]

        for part in partList:
            ss1=search.StreamSearcher(part,searchlist)
            ss1.recurse=True
            ss1.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss1.run()

            individualpartlist1=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                if interval.Interval(partstream1[0],partstream1[1]).name=='P4' or interval.Interval(partstream1[0],partstream1[1]).name=='P5':
                    individualpartlist1.append(partstream1.recurse().notesAndRests)
            dsh_subjectpartlist_separate.append(individualpartlist1)

        #second search to get subject with quarter note - eighth note tie    

        dsh_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss2.run()

            individualpartlist2=[]
            for results in subjects:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                if interval.Interval(partstream2[0],partstream2[1]).name=='P4' or interval.Interval(partstream2[0],partstream2[1]).name=='P5':
                    if partstream2[1].isNote and partstream2[2].isNote:
                        if partstream2[1].nameWithOctave==partstream2[2].nameWithOctave:
                            individualpartlist2.append(partstream2.recurse().notesAndRests)

            dsh_subjectpartlist_separate2.append(individualpartlist2)

        for i in range(len(dsh_subjectpartlist_separate2)):
            for j in range(len(dsh_subjectpartlist_separate2[i])):
                dsh_subjectpartlist_separate[i].append(dsh_subjectpartlist_separate2[i][j])

        #third and fourth search for augmented subjects

        searchlist3=copy.deepcopy(partList[1][0:14])

        nums=list(range(0,8))
        for i in nums:
            searchlist3[i].duration=searchlist3[i].duration.augmentOrDiminish(2) 
        nums=list(range(8,14))
        for i in nums:
            searchlist3[i].duration=search.WildcardDuration()

        searchlist4=copy.deepcopy(partList[0][3:17])

        nums=list(range(0,8))
        for i in nums:
            searchlist4[i].duration=searchlist4[i].duration.augmentOrDiminish(2)  
        nums=list(range(8,14))
        for i in nums:
            searchlist4[i].duration=search.WildcardDuration() 

        dsh_subjectpartlist_separate3=[]    
        dsh_subjectpartlist_separate4=[]

        for part in partList:
            ss3=search.StreamSearcher(part,searchlist3)
            ss3.recurse=True
            ss3.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss3.run()

            individualpartlist3=[]
            for results in subjects:
                partstream3=stream.Stream()
                partstream3.append(list(results.els))
                if interval.Interval(partstream3[0],partstream3[1]).name=='P4' or interval.Interval(partstream3[0],partstream3[1]).name=='P5':
                    individualpartlist3.append(partstream3.recurse().notesAndRests)

            dsh_subjectpartlist_separate3.append(individualpartlist3)

        for part in partList:
            ss4=search.StreamSearcher(part,searchlist4)
            ss4.recurse=True
            ss4.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss4.run()

            individualpartlist4=[]
            for results in subjects:
                partstream4=stream.Stream()
                partstream4.append(list(results.els))
                if interval.Interval(partstream4[0],partstream4[1]).name=='P4' or interval.Interval(partstream4[0],partstream4[1]).name=='P5':
                    if partstream4[1].isNote and partstream4[2].isNote:
                        if partstream4[1].nameWithOctave==partstream4[2].nameWithOctave:
                            individualpartlist4.append(partstream4.recurse().notesAndRests)

            dsh_subjectpartlist_separate4.append(individualpartlist4)


        dsh_subjectpartlist_separate[0].append(dsh_subjectpartlist_separate3[0][0])
        dsh_subjectpartlist_separate[1].append(dsh_subjectpartlist_separate3[1][0])
        dsh_subjectpartlist_separate[2].append(dsh_subjectpartlist_separate4[2][0])

        dsh_subjectpartlist_separate[0].pop(-2)
        dsh_subjectpartlist_separate[0].pop(5)
        dsh_subjectpartlist_separate[1].pop(-4)

        #for dotted subjects

        searchlist5=[note.Note(quarterLength=i) for i in [1,1.5,.5,1.5,.5,1.5,.5,1,1,2,1]]
        searchlist5[0].duration=search.WildcardDuration()

        nums=list(range(7,11))
        for i in nums:
            searchlist5[i].duration=search.WildcardDuration()

        dsh_subjectpartlist_separate5=[]

        for part in partList:
            ss5=search.StreamSearcher(part,searchlist5)
            ss5.recurse=True
            ss5.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss5.run()

            individualpartlist5=[]
            for results in subjects:
                partstream5=stream.Stream()
                partstream5.append(list(results.els))
                individualpartlist5.append(partstream5.recurse().notesAndRests)
            dsh_subjectpartlist_separate5.append(individualpartlist5)

        for i in range(len(dsh_subjectpartlist_separate5)):
            for j in range(len(dsh_subjectpartlist_separate5[i])):
                dsh_subjectpartlist_separate[i].append(dsh_subjectpartlist_separate5[i][j])

        # for tenor m.39 (sixteenth notes) subject

        searchlist6=[note.Note(quarterLength=i) for i in [.25,.25,.25,1,.5,.5,.5,.5,.5,.5,1,1,1,.5,.5,1,.5]]
        dsh_subjectpartlist_separate6=[]

        for part in partList:
            ss6=search.StreamSearcher(part,searchlist6)
            ss6.recurse=True
            ss6.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss6.run()

            individualpartlist6=[]
            for results in subjects:
                partstream6=stream.Stream()
                partstream6.append(list(results.els))
                individualpartlist6.append(partstream6.recurse().notesAndRests)
            dsh_subjectpartlist_separate6.append(individualpartlist6)

        dsh_subjectpartlist_separate[2].append(dsh_subjectpartlist_separate6[2][0])

        dsh_subjectpartlist_separate[0].pop(1)
        dsh_subjects=dsh_subjectpartlist_separate    
        thesubjects=dsh_subjects
    
    elif file==E_1:
        f=E_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[1][0:13])

        E_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notes)
            E_subjectpartlist_separate.append(individualpartlist)

        E_subjects=E_subjectpartlist_separate
        thesubjects=E_subjects
    
    elif file==e_1:
        f=e_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[0][0:26])

        e_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notes)
            e_subjectpartlist_separate.append(individualpartlist)

        e_subjectpartlist_separate[1].pop()

        #for partial subject statement at m.39
        searchlist2=copy.deepcopy(partList[0][0:13])
        e_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.filterNotes=True
            ss2.algorithms.append(search.StreamSearcher.noteNameAlgorithm)
            subjects=ss2.run()

            individualpartlist2=[]
            for results in subjects:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                individualpartlist2.append(partstream2.recurse().notes)
            e_subjectpartlist_separate2.append(individualpartlist2)

        e_subjectpartlist_separate[0].append(e_subjectpartlist_separate2[0][2])

        e_subjects=e_subjectpartlist_separate    
        thesubjects=e_subjects
    
    elif file==F_1:
        f=F_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[2][0:11])
        searchlist[0].duration=search.WildcardDuration()
        searchlist[-1].duration=search.WildcardDuration()

        F_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notes)
            F_subjectpartlist_separate.append(individualpartlist)

        #canon entrances (3)
        searchlist2=[note.Note(i) for i in ['D','E-','D','C','D','F#','G','A','B-','C','B-','D','C','B-','A','B-']]
        F_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.filterNotes=True
            ss2.algorithms.append(search.StreamSearcher.noteNameAlgorithm)
            subjects=ss2.run()

            individualpartlist2=[]
            for results in subjects:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                individualpartlist2.append(partstream2.recurse().notes)
            F_subjectpartlist_separate2.append(individualpartlist2)

        for i in range(len(F_subjectpartlist_separate2)):
            for j in range(len(F_subjectpartlist_separate2[i])):
                F_subjectpartlist_separate[i].append(F_subjectpartlist_separate2[i][j])

        F_subjects=F_subjectpartlist_separate 
        thesubjects=F_subjects
    
    elif file==f_1:
        f=f_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[2][0:11])
        searchlist[0].duration=search.WildcardDuration()
        searchlist[-1].duration=search.WildcardDuration()

        f_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notes)
            f_subjectpartlist_separate.append(individualpartlist)

        f_subjects=f_subjectpartlist_separate   
        thesubjects=f_subjects

    elif file==Fsh_1:
        f=Fsh_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[0][0:16])
        searchlist[0].duration=search.WildcardDuration()
        searchlist[-1].duration=search.WildcardDuration()

        Fsh_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notes)
            Fsh_subjectpartlist_separate.append(individualpartlist)

        # subject entry in soprano m.11 
        searchlist2=[note.Note(i) for i in ['C#','F#','E#','F#','E#','D#','C#','D#','C#','B','A#','G#','C#','A#']]
        Fsh_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.filterNotes=True
            ss2.algorithms.append(search.StreamSearcher.noteNameAlgorithm)
            subjects=ss2.run()

            individualpartlist2=[]
            for results in subjects:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                individualpartlist2.append(partstream2.recurse().notes)
            Fsh_subjectpartlist_separate2.append(individualpartlist2)

        Fsh_subjectpartlist_separate[0].append(Fsh_subjectpartlist_separate2[0][0])

        Fsh_subjects=Fsh_subjectpartlist_separate  
        thesubjects=Fsh_subjects
    
    elif file==fsh_1:
        f=fsh_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[2][0:20])
        searchlist[0].duration=search.WildcardDuration()
        searchlist[1].duration=search.WildcardDuration()
        searchlist[-1].duration=search.WildcardDuration()

        fsh_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notes)
            fsh_subjectpartlist_separate.append(individualpartlist)

        fsh_subjects=fsh_subjectpartlist_separate  
        thesubjects=fsh_subjects
    
    elif file==G_1:
        f=G_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[0][0:31])
        searchlist[0].duration=search.WildcardDuration()
        nums=list(range(15,31))
        for i in nums:
            searchlist[i].duration=search.WildcardDuration() 

        G_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1) #did not apply recursive iterator
            G_subjectpartlist_separate.append(individualpartlist)

        #tailoring ends of partial subject statements
        for _ in range(5):
            G_subjectpartlist_separate[0][3].pop(-1)
        for _ in range(10):
            G_subjectpartlist_separate[0][4].pop(-1)

        for _ in range(5):
            G_subjectpartlist_separate[1][3].pop(-1)
        for _ in range(2):
            G_subjectpartlist_separate[1][4].pop(-1)

        for _ in range(11):
            G_subjectpartlist_separate[2][1].pop(-1)
        for _ in range(16):
            G_subjectpartlist_separate[2][2].pop(-1)
        for _ in range(6):
            G_subjectpartlist_separate[2][3].pop(-1)  

        # subject entry in soprano m.61
        searchlist2=[note.Note(i) for i in ['D','E','D','C#','D','E','F#','E','D','E','F#','G','F#','E','D','C#','B','B','A']]
        G_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.filterNotes=True
            ss2.algorithms.append(search.StreamSearcher.noteNameAlgorithm)
            subjects=ss2.run()

            individualpartlist2=[]
            for results in subjects:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                individualpartlist2.append(partstream2)
            G_subjectpartlist_separate2.append(individualpartlist2)

        G_subjectpartlist_separate[0].append(G_subjectpartlist_separate2[0][0])

        G_subjects=G_subjectpartlist_separate   
        thesubjects=G_subjects
    
    elif file==g_1:
        #g DONE without recursive iterator, but might want counter subjects
        f=g_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notesAndRests)

        searchlist=copy.deepcopy(partList[1][0:13])
        searchlist[0].duration=search.WildcardDuration()
        searchlist[1].duration=search.WildcardDuration()
        searchlist[-1].duration=search.WildcardDuration()

        g_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1)
            g_subjectpartlist_separate.append(individualpartlist)

        g_subjectpartlist_separate[1].pop(4)

        for _ in range(6):
            g_subjectpartlist_separate[3][-1].pop(-1) 

        for p in g_subjectpartlist_separate:
            for i in p:
                i.pop(0)  

        g_subjects=g_subjectpartlist_separate
        thesubjects=g_subjects
    
    elif file==Afl_1:
        f=Afl_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notesAndRests)

        searchlist=copy.deepcopy(partList[2][0:8])
        searchlist[-1].duration=search.WildcardDuration()

        Afl_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1)

            Afl_subjectpartlist_separate.append(individualpartlist)

        Afl_subjectpartlist_separate[1].pop()
        Afl_subjectpartlist_separate[1].pop()
        Afl_subjectpartlist_separate[1].pop()
        Afl_subjectpartlist_separate[1].pop()
        Afl_subjectpartlist_separate[2].pop(4)
        Afl_subjectpartlist_separate[3].pop(1)

        #second search to get subjects without quarter rest in the beginning

        searchlist2=copy.deepcopy(partList[2][0:8])
        searchlist2[0].duration=search.WildcardDuration()

        Afl_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss2.run()

            individualpartlist2=[]
            for results in subjects:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                individualpartlist2.append(partstream2)

            Afl_subjectpartlist_separate2.append(individualpartlist2)

        Afl_subjectpartlist_separate[0].append(Afl_subjectpartlist_separate2[0][1])
        Afl_subjectpartlist_separate[1].append(Afl_subjectpartlist_separate2[1][3])
        Afl_subjectpartlist_separate[1].append(Afl_subjectpartlist_separate2[1][4])

        for p in Afl_subjectpartlist_separate:
            for i in p:
                i.pop(0)

        #third search to get last subject entry in soprano voice

        searchlist3=copy.deepcopy(partList[2][1:8])
        searchlist3[-1].duration=search.WildcardDuration()

        Afl_subjectpartlist_separate3=[]

        for part in partList:
            ss3=search.StreamSearcher(part,searchlist3)
            ss3.recurse=True
            ss3.algorithms.append(search.StreamSearcher.noteNameAlgorithm)
            subjects=ss3.run()

            individualpartlist3=[]
            for results in subjects:
                partstream3=stream.Stream()
                partstream3.append(list(results.els))
                individualpartlist3.append(partstream3)

            Afl_subjectpartlist_separate3.append(individualpartlist3)

        Afl_subjectpartlist_separate[0].append(Afl_subjectpartlist_separate3[0][-1])

        Afl_subjects=Afl_subjectpartlist_separate
        thesubjects=Afl_subjects
    
    elif file==gsh_1:
        f=gsh_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[2][0:15])
        searchlist[0].duration=search.WildcardDuration()
        searchlist[-1].duration=search.WildcardDuration()

        gsh_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notes)
            gsh_subjectpartlist_separate.append(individualpartlist)

        gsh_subjectpartlist_separate[1].pop()
        gsh_subjects=gsh_subjectpartlist_separate    
        thesubjects=gsh_subjects
    
    elif file==A_1:
        f=A_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notesAndRests)

        searchlist=copy.deepcopy(partList[0][0:17])
        nums=list(range(4,17))
        for i in nums:
            searchlist[i].duration=search.WildcardDuration()

        A_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                if partstream1[0].isNote and partstream1[1].isRest and partstream1[2].isRest and partstream1[3].isRest and partstream1[4].isNote:
                    individualpartlist.append(partstream1.recurse().notesAndRests)
            A_subjectpartlist_separate.append(individualpartlist)


        A_subjectpartlist_separate[0].pop()
        A_subjectpartlist_separate[1].pop(1) #mistake in original score, need to concatenate two voices
        A_subjectpartlist_separate[2].pop(-2)

        #score error - partial subject retrieved at m.25
        #n1=note.Note('E')
        #n2=note.Rest()
        #n3=[note.Note(i) for i in ['C#','F#','E','A','F#','B','G#','C#','A','D','C#','F#','D#']]
        searchlist2=[note.Note(i) for i in ['C#','F#','E','A','F#','B','G#','C#','A','D','C#','F#','D#']]

        A_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.filterNotes=True
            ss2.algorithms.append(search.StreamSearcher.noteNameAlgorithm)
            subjects=ss2.run()

            individualpartlist2=[]
            for results in subjects:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                individualpartlist2.append(partstream2.recurse().notesAndRests)
            A_subjectpartlist_separate2.append(individualpartlist2)

        A_subjectpartlist_separate[1].append(A_subjectpartlist_separate2[1][0])

        #score error - partial subject retrieved at m.31
        searchlist3=[note.Note(i) for i in ['C#','F#','D','G','E','A','F#','B','A','D','G','G','F#']]

        A_subjectpartlist_separate3=[]

        for part in partList:
            ss3=search.StreamSearcher(part,searchlist3)
            ss3.recurse=True
            ss3.filterNotes=True
            ss3.algorithms.append(search.StreamSearcher.noteNameAlgorithm)
            subjects=ss3.run()

            individualpartlist3=[]
            for results in subjects:
                partstream3=stream.Stream()
                partstream3.append(list(results.els))
                individualpartlist3.append(partstream3.recurse().notesAndRests)
            A_subjectpartlist_separate3.append(individualpartlist3)

        A_subjectpartlist_separate[1].append(A_subjectpartlist_separate3[1][0])

        n1=note.Note('E')
        n2=note.Rest()
        n3=[note.Note(i) for i in ['C#','F#','E','A','F#','B','G#','C#','A','D','F#','G#','E','G#','A']]
        searchlist4=flatten_list([n1,n2,n2,n3],[])

        A_subjectpartlist_separate4=[]

        for part in partList:
            ss4=search.StreamSearcher(part,searchlist4)
            ss4.recurse=True
            ss4.filterNotes=True
            ss4.algorithms.append(search.StreamSearcher.noteNameAlgorithm)
            subjects=ss4.run()

            individualpartlist4=[]
            for results in subjects:
                partstream4=stream.Stream()
                partstream4.append(list(results.els))
                individualpartlist4.append(partstream4.recurse().notesAndRests)
            A_subjectpartlist_separate4.append(individualpartlist4)

        A_subjectpartlist_separate[2].append(A_subjectpartlist_separate4[2][0])

        A_subjects=A_subjectpartlist_separate   
        thesubjects=A_subjects
    
    elif file==a_1:
        f=a_1

        if len(f.parts)==4:
            f=converter.parse('http://kern.humdrum.org/cgi-bin/ksdata?l=osu/classical/bach/wtc-1&file=wtc1f20.krn&f=kern')
        
        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notesAndRests)

        searchlist=copy.deepcopy(partList[2][1:33])

        nums=list(range(19,32))
        for i in nums:
            searchlist[i].duration=search.WildcardDuration()

        a_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notesAndRests)
            a_subjectpartlist_separate.append(individualpartlist)

        searchlist2=[note.Note(i) for i in ['A','G','A','B','C#','C#','B','C#','D','E','D','C#','D','E','F','G','E']]
        a_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.filterNotes=True
            ss2.algorithms.append(search.StreamSearcher.noteNameAlgorithm)
            subjects=ss2.run()

            individualpartlist2=[]
            for results in subjects:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                individualpartlist2.append(partstream2.recurse().notesAndRests)
            a_subjectpartlist_separate2.append(individualpartlist2)

        a_subjectpartlist_separate[2].append(a_subjectpartlist_separate2[2][0])

        a_subjects=a_subjectpartlist_separate 
        thesubjects=a_subjects
    
    elif file==Bfl_1:
        f=Bfl_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)


        searchlist=copy.deepcopy(partList[0][0:38])
        searchlist[-1].duration=search.WildcardDuration()

        Bfl_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notes)
            Bfl_subjectpartlist_separate.append(individualpartlist)

        searchlist2=[note.Note(i) for i in ['C','E-','C','G','B-','A-','D','C','E-','D','C','B-','F','A-','G']]
        Bfl_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.filterNotes=True
            ss2.algorithms.append(search.StreamSearcher.noteNameAlgorithm)
            subjects=ss2.run()

            individualpartlist2=[]
            for results in subjects:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                individualpartlist2.append(partstream2.recurse().notes)
            Bfl_subjectpartlist_separate2.append(individualpartlist2)

        Bfl_subjectpartlist_separate[1].append(Bfl_subjectpartlist_separate2[1][0])

        Bfl_subjects=Bfl_subjectpartlist_separate    
        thesubjects=Bfl_subjects
    
    elif file==bfl_1:
        f=bfl_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notesAndRests)

        searchlist=copy.deepcopy(partList[0][0:11])

        nums=list(range(6,11))
        for i in nums:
            searchlist[i].duration=search.WildcardDuration()  

        bfl_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                if partstream1[2].isRest:
                    individualpartlist.append(partstream1.recurse().notesAndRests)
            bfl_subjectpartlist_separate.append(individualpartlist)       

        #second search to get single alto subject entry at m.46

        searchlist2=copy.deepcopy(partList[1][2:9])
        searchlist2index=range(len(partList[1][2:9]))
        searchlist2[1].duration.type='quarter'
        searchlist2[-1]=search.Wildcard()

        bfl_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            ss2.algorithms.append(search.StreamSearcher.noteNameAlgorithm)
            subjects=ss2.run()

            individualpartlist2=[]
            for results in subjects:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                individualpartlist2.append(partstream2.recurse().notesAndRests)            
            bfl_subjectpartlist_separate2.append(individualpartlist2)

        bfl_subjectpartlist_separate[2].append(bfl_subjectpartlist_separate2[2][0])

        bfl_subjects=bfl_subjectpartlist_separate    
        thesubjects=bfl_subjects
    
    elif file==B_1:
        f=B_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[2][0:14])
        searchlist[-2].duration=search.WildcardDuration()
        searchlist[-1].duration=search.WildcardDuration()

        B_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1.recurse().notes)
            B_subjectpartlist_separate.append(individualpartlist)

        B_subjects=B_subjectpartlist_separate  
        thesubjects=B_subjects
    
    elif file==b_1:
        f=b_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[1][0:20])

        b_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                individualpartlist.append(partstream1)
            b_subjectpartlist_separate.append(individualpartlist)

        b_subjectpartlist_separate[2].pop()

        searchlist2=copy.deepcopy(partList[1][0:10])
        searchlist2[-1].duration=search.WildcardDuration()

        b_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.filterNotes=True
            ss2.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss2.run()

            individualpartlist2=[]
            for results in subjects:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                if interval.Interval(partstream2[0],partstream2[1]).directedName=='M-3' and interval.Interval(partstream2[1],partstream2[2]).directedName=='m-3' and interval.Interval(partstream2[3],partstream2[4]).directedName=='m-2' and interval.Interval(partstream2[5],partstream2[6]).directedName=='m-2' and interval.Interval(partstream2[7],partstream2[8]).directedName=='m-2' and interval.Interval(partstream2[8],partstream2[9]).directedName!='d7':
                    individualpartlist2.append(partstream2)
                elif interval.Interval(partstream2[0],partstream2[1]).directedName=='m-3' and interval.Interval(partstream2[1],partstream2[2]).directedName=='M-3' and interval.Interval(partstream2[3],partstream2[4]).directedName=='M-2' and interval.Interval(partstream2[5],partstream2[6]).directedName=='m-2' and interval.Interval(partstream2[7],partstream2[8]).directedName=='m-2' and interval.Interval(partstream2[8],partstream2[9]).directedName!='d7':
                    individualpartlist2.append(partstream2)
            b_subjectpartlist_separate2.append(individualpartlist2)

        for p in b_subjectpartlist_separate2:
            for i in p:
                i.pop(-1)

        for i in range(len(b_subjectpartlist_separate2)):
            for j in range(len(b_subjectpartlist_separate2[i])):
                b_subjectpartlist_separate[i].append(b_subjectpartlist_separate2[i][j])

        b_subjects=b_subjectpartlist_separate    
        thesubjects=b_subjects
    
    else:
        thesubjects='subjects not available for particular fugue'

    return thesubjects

# get second subject for c sharp minor fugue      

def get_subjects_1(file):
    if file==csh_1:
        f=csh_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[4][0:5])
        searchlist[0].duration=search.WildcardDuration()
        searchlist[-1].duration=search.WildcardDuration()
        searchlist[-2].duration=search.WildcardDuration()

        csh_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                if partstream1[0].pitch.ps>partstream1[1].pitch.ps and partstream1[2].pitch.ps>partstream1[0].pitch.ps and partstream1[2].pitch.ps>=partstream1[3].pitch.ps and partstream1[3].pitch.ps>=partstream1[0].pitch.ps:
                    individualpartlist.append(partstream1)
            csh_subjectpartlist_separate.append(individualpartlist)

        csh_subjectpartlist_separate[2].pop(-2)
        csh_subjectpartlist_separate[2].pop(1)
        csh_subjectpartlist_separate[1].pop(3)
        csh_subjectpartlist_separate[1].pop(2)
        csh_subjectpartlist_separate[1].pop(1)
        csh_subjectpartlist_separate[0].pop(2)

        csh_subjectpartlist_separate[0][3].pop(-1) #possible no pop
        csh_subjectpartlist_separate[0][6].pop(-1)
        csh_subjectpartlist_separate[0][7].pop(-1)
        csh_subjectpartlist_separate[1][3].pop(-1)
        csh_subjectpartlist_separate[3][6].pop(-1)

        csh_subjects=csh_subjectpartlist_separate 
        thesubjects=csh_subjects
    
    else:
        thesubjects=[]

    return thesubjects

def get_subjects_2(file):
    if file==csh_1:
        f=csh_1

        partList=[]

        for num in range(len(f.parts)):
            partList.append(f.parts[num].recurse().notes)

        searchlist=copy.deepcopy(partList[3][105:113])
        searchlist[-1].duration=search.WildcardDuration()
        searchlist[-2].duration=search.WildcardDuration()
        #searchlist[3].duration=search.WildcardDuration()

        csh_subjectpartlist_separate=[]

        for part in partList:
            ss=search.StreamSearcher(part,searchlist)
            ss.recurse=True
            ss.filterNotes=True
            ss.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss.run()

            individualpartlist=[]
            for results in subjects:
                partstream1=stream.Stream()
                partstream1.append(list(results.els))
                if partstream1[1]==partstream1[2] and partstream1[2]==partstream1[3] and partstream1[1]==partstream1[3]:
                    individualpartlist.append(partstream1)
            csh_subjectpartlist_separate.append(individualpartlist)

        csh_subjectpartlist_separate[1][6].pop(-1) 
        csh_subjectpartlist_separate[2][1].pop(-1)
        csh_subjectpartlist_separate[2][4].pop(-1)
        csh_subjectpartlist_separate[2][6].pop(-1)
        csh_subjectpartlist_separate[3][3].pop(-1)
        csh_subjectpartlist_separate[4][2].pop(-1)
        csh_subjectpartlist_separate[4][5].pop(-1)

        searchlist2=copy.deepcopy(partList[2][279:])

        csh_subjectpartlist_separate2=[]

        for part in partList:
            ss2=search.StreamSearcher(part,searchlist2)
            ss2.recurse=True
            ss2.algorithms.append(search.StreamSearcher.rhythmAlgorithm)
            subjects=ss2.run()

            individualpartlist2=[]
            for results in subjects:
                partstream2=stream.Stream()
                partstream2.append(list(results.els))
                individualpartlist2.append(partstream2)

            csh_subjectpartlist_separate2.append(individualpartlist2)

        csh_subjectpartlist_separate[2].append(csh_subjectpartlist_separate2[2][0])

        csh_subjects=csh_subjectpartlist_separate 
        thesubjects=csh_subjects
    
    else:
        thesubjects=[]

    return thesubjects


#new code using get_subjects() function

def in_subject(file, p1, p2): 
    
    subject_list=get_subjects(file)              
    
    flist=flatten_list(subject_list, [])

    slisti=[]
    slisto=[]

    for n in flist:
        for j in range(len(n)):
            slisti.append([(i.site.id, i.offset[1]) for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])
            slisto.append([n[j].offset for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])

    slisti=flatten_list(slisti,[])
    slisto=flatten_list(slisto,[])

    ndf=pd.DataFrame([slisti]).T
    ndf.columns=['gv']
    ndf['lv']=slisto
    #ndf=ndf.apply(pd.to_numeric, errors='ignore')

    vals=[(i.site.id, i.offset[1]) for i in p1.contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')]
    vals1=[(i.site.id, i.offset[1]) for i in p2.contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')]
    
    insubject=any(ndf['gv']==vals[0]) and any(ndf['gv']==vals1[0])
    
    if insubject:
        soffset=ndf.loc[ndf['gv']==vals[0]].iloc[0]['lv']
    elif insubject==False:
        soffset=False
    
    return [insubject,soffset]

#shortened subject search to be used in conjunction to hz searches
def in_subject_s(ndf, p1, p2): 
    
    vals=[(i.site.id, i.offset[1]) for i in p1.contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')]
    vals1=[(i.site.id, i.offset[1]) for i in p2.contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')]
    
    insubject=any(ndf['gv']==vals[0]) and any(ndf['gv']==vals1[0])

    if insubject:
        soffset=ndf.loc[ndf['gv']==vals[0]].iloc[0]['lv']
    elif insubject==False:
        soffset=False
    
    return [insubject,soffset]

#shorted subject search for vertical files - searches for sinlge note in subject instead of two notes forming an interval
def in_subject_v(ndf, p1): 
    
    vals=[(i.site.id, i.offset[1]) for i in p1.contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')]

    try: 
        insubject=any(ndf['gv']==vals[0])
    except IndexError:
        insubject=False
    
    if insubject:
        soffset=ndf.loc[ndf['gv']==vals[0]].iloc[0]['lv']
    elif insubject==False:
        soffset=False
    
    return [insubject,soffset]

def hz_full(file): #with subjects

    f=copy.deepcopy(file)
    
    if file==a_1:
        if len(f.parts)==5:
            f.remove(f.parts[0])
    
    if file==Csh_1:
        keyname=str('C# major')
    else:
        keyname=f.analyze('key.krumhanslschmuckler').name
    
    t=scale.ScalaScale(str('werck3'))
    t.tune(f)

    #get subjects
    subject_list=get_subjects(file)                  
    flist=flatten_list(subject_list, [])
    slisti=[]
    slisto=[]

    for n in flist:
        for j in range(len(n)):
            slisti.append([(i.site.id, i.offset[1]) for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])
            slisto.append([n[j].offset for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])

    slisti=flatten_list(slisti,[])
    slisto=flatten_list(slisto,[])
    
    ndf=pd.DataFrame([slisti]).T
    ndf.columns=['gv']
    ndf['lv']=slisto
    #end get subjects

    partList=[]

    for num in range(len(f.parts)):
        partList.append(f.parts[num].recurse().notes)
    
    matlist=[]

    for p in partList:
        for i in range(len(p)-1):
            if type(p[i])==note.Note and type(p[i+1])==note.Note:
                count_mat=np.array([file_name(file), keyname, round(abs(interval.Interval(p[i],p[i+1]).cents))%1200,cents_from_just(p[i],p[i+1]),round(abs(interval.Interval(p[i],p[i+1]).semitones))%12,int(''.join(filter(str.isdigit, interval.Interval(p[i],p[i+1]).simpleName))),interval.Interval(p[i],p[i+1]).simpleName,interval.Interval(p[i],p[i+1]).name,interval.Interval(p[i],p[i+1]).directedName,str(interval.Interval(p[i],p[i+1]).direction==1),round(abs(interval.Interval(p[i],p[i+1]).semitones)),p[i].duration.quarterLength,p[i+1].duration.quarterLength,p[i].offset,p[i].beat,p[i].name,p[i+1].name,p[i].octave,p[i+1].octave,p[i].measureNumber,get_spine_v(p.id),str(in_subject_s(ndf,p[i],p[i+1])[0]),float(in_subject_s(ndf,p[i],p[i+1])[1]),p[i],p[i+1]]) 
                c_count_mat=np.column_stack(count_mat)
                
                matlist.append(c_count_mat)
    
    ctm=np.concatenate(matlist) #concatenate all matices into a large matrix
    df=pd.DataFrame(data=ctm,columns=['file','key','cents','cents from just','semitones','generic interval','simple name','name','directed name','direction','total semitones','n1 duration','n2 duration','offset','beat','n1 name','n2 name','n1 octave','n2 octave','measure','part','subject','subject offset','n1','n2']) #convert numpy array into pandas dataframe
    df=df.apply(pd.to_numeric, errors='ignore')

    
    return df


def hz_t(file,new_key): #THIS ONE FOR NOW
    
    f=copy.deepcopy(file)
    
    if file==a_1:
        if len(f.parts)==5:
            f.remove(f.parts[0])
    
    if file==Csh_1:
        old_key=str('C#')
        name=str('C# major')
    else:
        old_key=f.analyze('key.krumhanslschmuckler').name.partition(' ')[0]
        name=f.analyze('key.krumhanslschmuckler').name
    
    if file in wtc_1:
        if name=='E- minor':
            old_key='D#'
    
    trans_int=interval.Interval(note.Note(old_key),note.Note(new_key))
            
    if abs(trans_int.semitones)>6:
        c_trans_int=interval.subtract(['P8', trans_int.name])
        if trans_int.direction==1:
            c_trans_int=c_trans_int.reverse()
            trans_int=c_trans_int
        else:
            trans_int=c_trans_int
        
    tf=f.transpose(trans_int)
    
    if file==Csh_1:
        newname=str(f'{new_key} major')
    else:
        newname=tf.analyze('key.krumhanslschmuckler').name
    
    t=scale.ScalaScale(str('werck3'))
    t.tune(tf)

    #get subjects
    subject_list=get_subjects(file)                  
    flist=flatten_list(subject_list, [])
    slisti=[]
    slisto=[]

    for n in flist:
        for j in range(len(n)):
            slisti.append([(i.site.id, i.offset[1]) for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])
            slisto.append([n[j].offset for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])

    slisti=flatten_list(slisti,[])
    slisto=flatten_list(slisto,[])
    
    ndf=pd.DataFrame([slisti]).T
    ndf.columns=['gv']
    ndf['lv']=slisto
    #end get subjects   

    partList=[]

    for num in range(len(tf.parts)):
        partList.append(tf.parts[num].recurse().notes)
    
    matlist=[]

    for p in partList:
        for i in range(len(p)-1):
            if type(p[i])==note.Note and type(p[i+1])==note.Note:
                count_mat=np.array([file_name(file), name, newname, round(abs(interval.Interval(p[i],p[i+1]).cents))%1200,cents_from_just(p[i],p[i+1]),round(abs(interval.Interval(p[i],p[i+1]).semitones))%12,int(''.join(filter(str.isdigit, interval.Interval(p[i],p[i+1]).simpleName))),interval.Interval(p[i],p[i+1]).simpleName,interval.Interval(p[i],p[i+1]).name,interval.Interval(p[i],p[i+1]).directedName,str(interval.Interval(p[i],p[i+1]).direction==1),round(abs(interval.Interval(p[i],p[i+1]).semitones)),p[i].duration.quarterLength,p[i+1].duration.quarterLength,p[i].offset,p[i].beat,p[i].name,p[i+1].name,p[i].octave,p[i+1].octave,p[i].measureNumber,get_spine_v(p.id),str(in_subject_s(ndf,p[i],p[i+1])[0]),float(in_subject_s(ndf,p[i],p[i+1])[1]),p[i],p[i+1]]) 
                c_count_mat=np.column_stack(count_mat)
                
                matlist.append(c_count_mat)
    
    ctm=np.concatenate(matlist) #concatenate all matices into a large matrix
    df=pd.DataFrame(data=ctm,columns=['file','original key','key','cents','cents from just','semitones','generic interval','simple name','name','directed name','direction','total semitones','n1 duration','n2 duration','offset','beat','n1 name','n2 name','n1 octave','n2 octave','measure','part','subject','subject offset','n1','n2']) #convert numpy array into pandas dataframe
    df=df.apply(pd.to_numeric, errors='ignore')

    
    return df


#PANDAS W DIFF CENTS NO SUM WITH OTHER FIELDS NEW CODE !!!!! now with measure number and note names
#version with file name field and KEY
#WITH SPINES AND NAME and TIES
#with subject searches

def vert_full(file): #with old code

    f=copy.deepcopy(file)
    
    if file==a_1:
        if len(f.parts)==5:
            f.remove(f.parts[0])
        
    if file==Csh_1:
        keyname=str('C# major')
    else:
        keyname=f.analyze('key.krumhanslschmuckler').name
    
    t=scale.ScalaScale(str('werck3'))
    t.tune(f)
    
    #get subjects
    subject_list=get_subjects(file)                  
    flist=flatten_list(subject_list, [])
    slisti=[]
    slisto=[]

    for n in flist:
        for j in range(len(n)):
            slisti.append([(i.site.id, i.offset[1]) for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])
            slisto.append([n[j].offset for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])

    slisti=flatten_list(slisti,[])
    slisto=flatten_list(slisto,[])
    
    ndf=pd.DataFrame([slisti]).T
    ndf.columns=['gv']
    ndf['lv']=slisto
    #end get subjects
    
    partList=[]

    for num in range(len(f.parts)):
        partList.append(f.parts[num])

    matri=np.empty(shape=(len(partList),len(partList)),dtype=object)

    for i in range(len(partList)):
        for j in range(len(partList)):
            matri[i,j]=stream.Score()
            if i!=j:
                matri[i,j].insert(0,partList[i])
                matri[i,j].insert(0,partList[j])
    Imat=np.triu(matri)
    kat=matri[np.triu_indices(len(matri),1)]  

    for i in range(len(kat)):
        kat[i]=kat[i].chordify(removeRedundantPitches=False)
        kat[i]=kat[i].recurse().notesAndRests

    matlist=[]
    
    for part in kat:
        for ch in part:
            if not ch.isRest:
                cha=ch.sortAscending()
                mat=np.empty(shape=(len(ch),len(ch)),dtype=object)

                for i in range(len(ch)):
                    for j in range(len(ch)):
                        mat[i,j]=[file_name(file),keyname,round(abs(interval.Interval(cha[i],cha[j]).cents))%1200,cents_from_just(cha[i],cha[j]),round(abs(interval.Interval(cha[i],cha[j]).semitones))%12,int(''.join(filter(str.isdigit, interval.Interval(cha[i],cha[j]).simpleName))),interval.Interval(cha[i],cha[j]).simpleName,interval.Interval(cha[i],cha[j]).name,round(abs(interval.Interval(cha[i],cha[j]).semitones)),ch.duration.quarterLength,ch.offset,float(ch.beat),cha[i].name,cha[j].name,get_spine(cha[i]),get_spine(cha[j]),get_tie(cha[i]),get_tie(cha[j]),str(in_subject_v(ndf,cha[i])[0]),float(in_subject_v(ndf,cha[i])[1]),str(in_subject_v(ndf,cha[j])[0]),float(in_subject_v(ndf,cha[j])[1]),ch.measureNumber] 

                kmat=mat[np.triu_indices(len(mat),1)] #CHANGE INDENTATION HERE
                
                for i in range(len(kmat)):
                    kmat[i]=np.array(kmat[i])
                    
                if len(kmat)>0: #separate list into columns containing interval class and another containing cents
                    flattened=(np.hstack(kmat)) 
                    i_file=flattened[0::23]
                    i_key=flattened[1::23]
                    i_cents=flattened[2::23] 
                    i_centsfromjust=flattened[3::23]
                    i_semitones=flattened[4::23]
                    i_intclass=flattened[5::23]
                    i_simpname=flattened[6::23]
                    i_name=flattened[7::23]
                    i_semitonesnotsimp=flattened[8::23]
                    i_dur=flattened[9::23]
                    i_offset=flattened[10::23]
                    i_beat=flattened[11::23]
                    i_lower_note=flattened[12::23]
                    i_upper_note=flattened[13::23]
                    i_lower_spine=flattened[14::23]
                    i_upper_spine=flattened[15::23]
                    i_lower_tie=flattened[16::23]
                    i_upper_tie=flattened[17::23]
                    i_n1_subject=flattened[18::23]
                    i_n1_offset=flattened[19::23]
                    i_n2_subject=flattened[20::23]
                    i_n2_offset=flattened[21::23]
                    i_measure=flattened[22::23]
                elif len(kmat)==0:
                    i_file=kmat[0::23]
                    i_key=kmat[1::23]
                    i_cents=kmat[2::23] 
                    i_centsfromjust=kmat[3::23]
                    i_semitones=kmat[4::23]
                    i_intclass=kmat[5::23]
                    i_simpname=kmat[6::23]
                    i_name=kmat[7::23]
                    i_semitonesnotsimp=kmat[8::23]
                    i_dur=kmat[9::23]
                    i_offset=kmat[10::23]
                    i_beat=kmat[11::23]
                    i_lower_note=kmat[12::23]
                    i_upper_note=kmat[13::23]
                    i_lower_spine=kmat[14::23]
                    i_upper_spine=kmat[15::23]
                    i_lower_tie=kmat[16::23]
                    i_upper_tie=kmat[17::23]
                    i_n1_subject=kmat[18::23]
                    i_n1_offset=kmat[19::23]
                    i_n2_subject=kmat[20::23]
                    i_n2_offset=kmat[21::23]                    
                    i_measure=kmat[22::23]
                    
                count_mat=np.column_stack((i_file,i_key,i_cents,i_centsfromjust,i_semitones,i_intclass,i_simpname,i_name,i_semitonesnotsimp,i_dur,i_offset,i_beat,i_lower_note,i_upper_note,i_lower_spine,i_upper_spine,i_lower_tie,i_upper_tie,i_n1_subject,i_n1_offset,i_n2_subject,i_n2_offset,i_measure)) #put the lists into a matrix    

                matlist.append((count_mat)) #append matrix to list

    ctm=np.concatenate(matlist) #concatenate all matices into a large matrix
    df=pd.DataFrame(data=ctm,columns=['file','key','cents','cents from just','semitones','generic interval','simple name','name','total semitones','duration','offset','beat','lower note','upper note','lower part','upper part','lower tie','upper tie','lower subject','lower offset','upper subject','upper offset','measure']) #convert numpy array into pandas dataframe
    df=df.apply(pd.to_numeric, errors='ignore')
    #df=df.astype(dtype='float64')
    #df_sum=df.groupby(['cents','cents from just','semitones'],as_index=False)['duration'].sum()
    #df_sum=df.groupby(['cents','interval class','cents from just'],as_index=False)['duration'].sum() #sum up duration by cents group

    ncol=df['duration']/sum(df['duration'])
    df['norm duration'] = ncol
    df=df.apply(pd.to_numeric, errors='ignore')
    
    return df

#PANDAS W DIFF CENTS NO SUM WITH OTHER FIELDS NEW CODE !!!!! transposed with input parameter as NEW KEY CLOSE
#UPDATED KEY SEARCH WITH NEW AND OLD KEY FIELDS MOST UPDATED
#with spines and name 
def vert_t3(file,new_key): #with old code

    f=copy.deepcopy(file)
    
    if file==a_1:
        if len(f.parts)==5:
            f.remove(f.parts[0])
    
    if file==Csh_1:
        old_key=str('C#')
        name=str('C# major')
    else:
        old_key=f.analyze('key.krumhanslschmuckler').name.partition(' ')[0]
        name=f.analyze('key.krumhanslschmuckler').name
    
    if file in wtc_1:
        if name=='E- minor':
            old_key='D#'
    
    trans_int=interval.Interval(note.Note(old_key),note.Note(new_key))
    
    if abs(trans_int.semitones)>6:
        c_trans_int=interval.subtract(['P8', trans_int.name])
        if trans_int.direction==1:
            c_trans_int=c_trans_int.reverse()
            trans_int=c_trans_int
        else:
            trans_int=c_trans_int
        
    tf=f.transpose(trans_int)
    
    if file==Csh_1:
        newname=str(f'{new_key} major')
    else:
        newname=tf.analyze('key.krumhanslschmuckler').name
        
    t=scale.ScalaScale(str('werck3'))
    t.tune(tf)

    #get subjects
    subject_list=get_subjects(file)                  
    flist=flatten_list(subject_list, [])
    slisti=[]
    slisto=[]

    for n in flist:
        for j in range(len(n)):
            slisti.append([(i.site.id, i.offset[1]) for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])
            slisto.append([n[j].offset for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])

    slisti=flatten_list(slisti,[])
    slisto=flatten_list(slisto,[])
    
    ndf=pd.DataFrame([slisti]).T
    ndf.columns=['gv']
    ndf['lv']=slisto
    #end get subjects    

    partList=[]

    for num in range(len(tf.parts)):
        partList.append(tf.parts[num])

    matri=np.empty(shape=(len(partList),len(partList)),dtype=object)

    for i in range(len(partList)):
        for j in range(len(partList)):
            matri[i,j]=stream.Score()
            if i!=j:
                matri[i,j].insert(0,partList[i])
                matri[i,j].insert(0,partList[j])
    Imat=np.triu(matri)
    kat=matri[np.triu_indices(len(matri),1)]  

    for i in range(len(kat)):
        kat[i]=kat[i].chordify(removeRedundantPitches=False)
        kat[i]=kat[i].recurse().notesAndRests

    matlist=[]
    
    for part in kat:
        for ch in part:
            if not ch.isRest:
                cha=ch.sortAscending()
                mat=np.empty(shape=(len(ch),len(ch)),dtype=object)

                for i in range(len(ch)):
                    for j in range(len(ch)):
                        mat[i,j]=[file_name(file),name,newname,round(abs(interval.Interval(cha[i],cha[j]).cents))%1200,cents_from_just(cha[i],cha[j]),round(abs(interval.Interval(cha[i],cha[j]).semitones))%12,int(''.join(filter(str.isdigit, interval.Interval(cha[i],cha[j]).simpleName))),interval.Interval(cha[i],cha[j]).simpleName,interval.Interval(cha[i],cha[j]).name,round(abs(interval.Interval(cha[i],cha[j]).semitones)),ch.duration.quarterLength,ch.offset,float(ch.beat),cha[i].name,cha[j].name,get_spine(cha[i]),get_spine(cha[j]),get_tie(cha[i]),get_tie(cha[j]),str(in_subject_v(ndf,cha[i])[0]),float(in_subject_v(ndf,cha[i])[1]),str(in_subject_v(ndf,cha[j])[0]),float(in_subject_v(ndf,cha[j])[1]),ch.measureNumber] 

                kmat=mat[np.triu_indices(len(mat),1)] #CHANGE INDENTATION HERE
                
                for i in range(len(kmat)):
                    kmat[i]=np.array(kmat[i])
                    
                if len(kmat)>0: #separate list into columns containing interval class and another containing cents
                    flattened=(np.hstack(kmat)) 
                    i_file=flattened[0::24]
                    i_key=flattened[1::24]
                    i_newkey=flattened[2::24] 
                    i_cents=flattened[3::24]
                    i_centsfromjust=flattened[4::24]
                    i_semitones=flattened[5::24]
                    i_intclass=flattened[6::24]
                    i_simpname=flattened[7::24]
                    i_name=flattened[8::24]
                    i_semitonesnotsimp=flattened[9::24]
                    i_dur=flattened[10::24]
                    i_offset=flattened[11::24]
                    i_beat=flattened[12::24]
                    i_lower_note=flattened[13::24]
                    i_upper_note=flattened[14::24]
                    i_lower_spine=flattened[15::24]
                    i_upper_spine=flattened[16::24]
                    i_lower_tie=flattened[17::24]
                    i_upper_tie=flattened[18::24]
                    i_n1_subject=flattened[19::24]
                    i_n1_offset=flattened[20::24]
                    i_n2_subject=flattened[21::24]
                    i_n2_offset=flattened[22::24]                    
                    i_measure=flattened[23::24]
                elif len(kmat)==0:
                    i_file=kmat[0::24]
                    i_key=kmat[1::24]
                    i_newkey=kmat[2::24] 
                    i_cents=kmat[3::24]
                    i_centsfromjust=kmat[4::24]
                    i_semitones=kmat[5::24]
                    i_intclass=kmat[6::24]
                    i_simpname=kmat[7::24]
                    i_name=kmat[8::24]
                    i_semitonesnotsimp=kmat[9::24]
                    i_dur=kmat[10::24]
                    i_offset=kmat[11::24]
                    i_beat=kmat[12::24]
                    i_lower_note=kmat[13::24]
                    i_upper_note=kmat[14::24]
                    i_lower_spine=kmat[15::24]
                    i_upper_spine=kmat[16::24]
                    i_lower_tie=kmat[17::24]
                    i_upper_tie=kmat[18::24]
                    i_n1_subject=kmat[19::24]
                    i_n1_offset=kmat[20::24]
                    i_n2_subject=kmat[21::24]
                    i_n2_offset=kmat[22::24]                    
                    i_measure=kmat[23::24]
                    
                count_mat=np.column_stack((i_file,i_key,i_newkey,i_cents,i_centsfromjust,i_semitones,i_intclass,i_simpname,i_name,i_semitonesnotsimp,i_dur,i_offset,i_beat,i_lower_note,i_upper_note,i_lower_spine,i_upper_spine,i_lower_tie,i_upper_tie,i_n1_subject,i_n1_offset,i_n2_subject,i_n2_offset,i_measure)) #put the lists into a matrix    

                matlist.append((count_mat)) #append matrix to list

    ctm=np.concatenate(matlist) #concatenate all matices into a large matrix
    df=pd.DataFrame(data=ctm,columns=['file','original key','key','cents','cents from just','semitones','generic interval','simple name','name','total semitones','duration','offset','beat','lower note','upper note','lower part','upper part','lower tie','upper tie','lower subject','lower offset','upper subject','upper offset','measure']) #convert numpy array into pandas dataframe
    df=df.apply(pd.to_numeric, errors='ignore')
    #df=df.astype(dtype='float64')
    #df_sum=df.groupby(['cents','cents from just','semitones'],as_index=False)['duration'].sum()
    #df_sum=df.groupby(['cents','interval class','cents from just'],as_index=False)['duration'].sum() #sum up duration by cents group

    ncol=df['duration']/sum(df['duration'])
    df['norm duration'] = ncol
    df=df.apply(pd.to_numeric, errors='ignore')
    
    return df

#prelude vertical searches
def prelude_vert(file): #with old code

    f=copy.deepcopy(file)
    
    if file==Fsh_1_p:
        keyname=str('F# major')
    else:
        keyname=f.analyze('key.krumhanslschmuckler').name
    
    t=scale.ScalaScale(str('werck3'))
    t.tune(f)

    f_chords=f.chordify() #convert score into chords
    f_ch=f_chords.recurse().notesAndRests #select only notes and rests in recursive iterator
    
    matlist=[]
    
    for ch in f_ch: #ch = each chord in score of chords
        if not ch.isRest: #filter out rests
            cha=ch.sortAscending()
            mat=np.empty(shape=(len(ch),len(ch)),dtype=object)

            for i in range(len(ch)):
                for j in range(len(ch)):
                    mat[i,j]=[file_name(file),keyname,round(abs(interval.Interval(cha[i],cha[j]).cents))%1200,cents_from_just(cha[i],cha[j]),round(abs(interval.Interval(cha[i],cha[j]).semitones))%12,int(''.join(filter(str.isdigit, interval.Interval(cha[i],cha[j]).simpleName))),interval.Interval(cha[i],cha[j]).simpleName,interval.Interval(cha[i],cha[j]).name,round(abs(interval.Interval(cha[i],cha[j]).semitones)),float(ch.duration.quarterLength),ch.offset,float(ch.beat),cha[i].name,cha[j].name,get_tie(cha[i]),get_tie(cha[j]),ch.measureNumber] 

            kmat=mat[np.triu_indices(len(mat),1)] #CHANGE INDENTATION HERE

            for i in range(len(kmat)):
                kmat[i]=np.array(kmat[i])

            if len(kmat)>0: #separate list into columns containing interval class and another containing cents
                flattened=(np.hstack(kmat)) 
                i_file=flattened[0::17]
                i_key=flattened[1::17]
                i_cents=flattened[2::17] 
                i_centsfromjust=flattened[3::17]
                i_semitones=flattened[4::17]
                i_intclass=flattened[5::17]
                i_simpname=flattened[6::17]
                i_name=flattened[7::17]
                i_semitonesnotsimp=flattened[8::17]
                i_dur=flattened[9::17]
                i_offset=flattened[10::17]
                i_beat=flattened[11::17]
                i_lower_note=flattened[12::17]
                i_upper_note=flattened[13::17]
                i_lower_tie=flattened[14::17]
                i_upper_tie=flattened[15::17]
                i_measure=flattened[16::17]
            elif len(kmat)==0:
                i_file=kmat[0::17]
                i_key=kmat[1::17]
                i_cents=kmat[2::17] 
                i_centsfromjust=kmat[3::17]
                i_semitones=kmat[4::17]
                i_intclass=kmat[5::17]
                i_simpname=kmat[6::17]
                i_name=kmat[7::17]
                i_semitonesnotsimp=kmat[8::17]
                i_dur=kmat[9::17]
                i_offset=kmat[10::17]
                i_beat=kmat[11::17]
                i_lower_note=kmat[12::17]
                i_upper_note=kmat[13::17]
                i_lower_tie=kmat[14::17]
                i_upper_tie=kmat[15::17]                  
                i_measure=kmat[16::17]

            count_mat=np.column_stack((i_file,i_key,i_cents,i_centsfromjust,i_semitones,i_intclass,i_simpname,i_name,i_semitonesnotsimp,i_dur,i_offset,i_beat,i_lower_note,i_upper_note,i_lower_tie,i_upper_tie,i_measure)) #put the lists into a matrix    

            matlist.append((count_mat)) #append matrix to list

    ctm=np.concatenate(matlist) #concatenate all matices into a large matrix
    df=pd.DataFrame(data=ctm,columns=['file','key','cents','cents from just','semitones','generic interval','simple name','name','total semitones','duration','offset','beat','lower note','upper note','lower tie','upper tie','measure']) #convert numpy array into pandas dataframe
    df=df.apply(pd.to_numeric, errors='ignore')
    #df=df.astype(dtype='float64')
    #df_sum=df.groupby(['cents','cents from just','semitones'],as_index=False)['duration'].sum()
    #df_sum=df.groupby(['cents','interval class','cents from just'],as_index=False)['duration'].sum() #sum up duration by cents group

    ncol=df['duration']/sum(df['duration'])
    df['norm duration'] = ncol
    df=df.apply(pd.to_numeric, errors='ignore')
    
    return df

#PANDAS W DIFF CENTS NO SUM WITH OTHER FIELDS NEW CODE !!!!! transposed with input parameter as NEW KEY CLOSE
#UPDATED KEY SEARCH WITH NEW AND OLD KEY FIELDS MOST UPDATED
#with spines and name 

def prelude_vert_t(file,new_key): #with old code

    f=copy.deepcopy(file)
    
    if file==Fsh_1_p:
        old_key=str('F#')
        name=str('F# major')
    else:
        old_key=f.analyze('key.krumhanslschmuckler').name.partition(' ')[0]
        name=f.analyze('key.krumhanslschmuckler').name
    
    trans_int=interval.Interval(note.Note(old_key),note.Note(new_key))
    
    if abs(trans_int.semitones)>6:
        c_trans_int=interval.subtract(['P8', trans_int.name])
        if trans_int.direction==1:
            c_trans_int=c_trans_int.reverse()
            trans_int=c_trans_int
        else:
            trans_int=c_trans_int
        
    tf=f.transpose(trans_int)
    
    if file==Fsh_1_p:
        newname=str(f'{new_key} major')
    else:
        newname=tf.analyze('key.krumhanslschmuckler').name
        
    t=scale.ScalaScale(str('werck3'))
    t.tune(tf)

    f_chords=tf.chordify() #convert score into chords
    f_ch=f_chords.recurse().notesAndRests #select only notes and rests in recursive iterator
    
    matlist=[]
    
    for ch in f_ch: #ch = each chord in score of chords
        if not ch.isRest: #filter out rests
            cha=ch.sortAscending()
            mat=np.empty(shape=(len(ch),len(ch)),dtype=object)

            for i in range(len(ch)):
                for j in range(len(ch)):
                    mat[i,j]=[file_name(file),name,newname,round(abs(interval.Interval(cha[i],cha[j]).cents))%1200,cents_from_just(cha[i],cha[j]),round(abs(interval.Interval(cha[i],cha[j]).semitones))%12,int(''.join(filter(str.isdigit, interval.Interval(cha[i],cha[j]).simpleName))),interval.Interval(cha[i],cha[j]).simpleName,interval.Interval(cha[i],cha[j]).name,round(abs(interval.Interval(cha[i],cha[j]).semitones)),float(ch.duration.quarterLength),ch.offset,float(ch.beat),cha[i].name,cha[j].name,get_tie(cha[i]),get_tie(cha[j]),ch.measureNumber] 

            kmat=mat[np.triu_indices(len(mat),1)] #CHANGE INDENTATION HERE

            for i in range(len(kmat)):
                kmat[i]=np.array(kmat[i])

            if len(kmat)>0: #separate list into columns containing interval class and another containing cents
                flattened=(np.hstack(kmat)) 
                i_file=flattened[0::18]
                i_key=flattened[1::18]
                i_newkey=flattened[2::18]
                i_cents=flattened[3::18] 
                i_centsfromjust=flattened[4::18]
                i_semitones=flattened[5::18]
                i_intclass=flattened[6::18]
                i_simpname=flattened[7::18]
                i_name=flattened[8::18]
                i_semitonesnotsimp=flattened[9::18]
                i_dur=flattened[10::18]
                i_offset=flattened[11::18]
                i_beat=flattened[12::18]
                i_lower_note=flattened[13::18]
                i_upper_note=flattened[14::18]
                i_lower_tie=flattened[15::18]
                i_upper_tie=flattened[16::18]
                i_measure=flattened[17::18]
            elif len(kmat)==0:
                i_file=kmat[0::18]
                i_key=kmat[1::18]
                i_newkey=kmat[2::18]
                i_cents=kmat[3::18] 
                i_centsfromjust=kmat[4::18]
                i_semitones=kmat[5::18]
                i_intclass=kmat[6::18]
                i_simpname=kmat[7::18]
                i_name=kmat[8::18]
                i_semitonesnotsimp=kmat[9::18]
                i_dur=kmat[10::18]
                i_offset=kmat[11::18]
                i_beat=kmat[12::18]
                i_lower_note=kmat[13::18]
                i_upper_note=kmat[14::18]
                i_lower_tie=kmat[15::18]
                i_upper_tie=kmat[16::18]                  
                i_measure=kmat[17::18]

            count_mat=np.column_stack((i_file,i_key,i_newkey,i_cents,i_centsfromjust,i_semitones,i_intclass,i_simpname,i_name,i_semitonesnotsimp,i_dur,i_offset,i_beat,i_lower_note,i_upper_note,i_lower_tie,i_upper_tie,i_measure)) #put the lists into a matrix    

            matlist.append((count_mat)) #append matrix to list

    ctm=np.concatenate(matlist) #concatenate all matices into a large matrix
    df=pd.DataFrame(data=ctm,columns=['file','original key','key','cents','cents from just','semitones','generic interval','simple name','name','total semitones','duration','offset','beat','lower note','upper note','lower tie','upper tie','measure']) #convert numpy array into pandas dataframe
    df=df.apply(pd.to_numeric, errors='ignore')
    #df=df.astype(dtype='float64')
    #df_sum=df.groupby(['cents','cents from just','semitones'],as_index=False)['duration'].sum()
    #df_sum=df.groupby(['cents','interval class','cents from just'],as_index=False)['duration'].sum() #sum up duration by cents group

    ncol=df['duration']/sum(df['duration'])
    df['norm duration'] = ncol
    df=df.apply(pd.to_numeric, errors='ignore')
    
    return df



#CODE TO GRAB SUBJECT HEAD UPDATED E MINOR ACCOUNTED FOR

def subject_head_0(df):
    flop=df.sort_values(['measure','beat'])
   
    if df.iloc[0]['file']=='e_1':
        start=92
    else:
        start=0
        while int(flop.iloc[start].name) in range(int(flop.iloc[start+1].name)-50,int(flop.iloc[start+1].name)+50):
            start+=1     
        
    end=flop.iloc[start].name
    first=flop.iloc[0].name
    head=flop.loc[first:end]
    
    return head

#for horizontal searches only, filters score by metrical hierarchy
def m_hier(df, b):
    
    n_df=copy.deepcopy(df[df['beat']%b==0])
    
    for i in range(len(n_df)-1):
        if n_df['part'].iloc[i]==n_df['part'].iloc[i+1]:
            n_df.loc[n_df.index[i], 'cents']=round(abs(interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).cents))%1200
            n_df.loc[n_df.index[i], 'cents from just']=cents_from_just(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1])
            n_df.loc[n_df.index[i], 'semitones']=round(abs(interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).semitones))%12
            n_df.loc[n_df.index[i], 'generic interval']=int(''.join(filter(str.isdigit, interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).simpleName)))
            n_df.loc[n_df.index[i], 'name']=interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).name
            n_df.loc[n_df.index[i], 'simple name']=interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).simpleName
            n_df.loc[n_df.index[i], 'directed name']=interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).directedName
            n_df.loc[n_df.index[i], 'direction']=str(interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).direction==1)
            n_df.loc[n_df.index[i], 'total semitones']=round(abs(interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).semitones))
            n_df.loc[n_df.index[i], 'n2 duration']=n_df['n1'].iloc[i+1].duration.quarterLength
            n_df.loc[n_df.index[i], 'n2 name']=n_df['n1'].iloc[i+1].name
            n_df.loc[n_df.index[i], 'n2 octave']=n_df['n1'].iloc[i+1].octave
            n_df.loc[n_df.index[i], 'n2']=n_df['n1'].iloc[i+1]
           
    #n_df=n_df[['file','key','cents','cents from just','semitones','generic interval','name','directed name','direction','total semitones','n1 duration','n2 duration','offset','beat','n1 name','n2 name','octave','measure','part','subject','subject offset','n1']]
    
    return n_df

def roman_from_key(file,newkey):
    
    f=copy.deepcopy(file)

    if f==Csh_1:
        tonickey=str('C# major')
    else:
        tonickey=f.analyze('key.krumhanslschmuckler').name

    Tnm=tonickey.split()[0]
    Tmode=f.analyze('key.krumhanslschmuckler').mode

    if Tmode=='major':  
        Tnm=Tnm.upper()
    elif Tmode=='minor':  
        Tnm=Tnm.lower()

    Tky=key.Key(Tnm)
    
    Nnm=newkey.split()[0]
    Nmode=newkey.split()[1]

    if Nmode=='major':
        sc = scale.MajorScale(Nnm)
    elif Nmode=='minor':
        sc = scale.MinorScale(Nnm)

    ptches=[str(p) for p in sc.pitchesFromScaleDegrees([1,3,5])]
    t_chord=chord.Chord(ptches)
    
    res=roman.romanNumeralFromChord(t_chord, Tky).figure
    
    if res=='bVII':
        res="VII"
    
    if res=='bbvi':
        res='v'
    
    if res=='bvii':
        res='vii'
    
    return res

def win_key(file,n,cgrid=False): #with corrected enharmonics
    #from collections import Counter
    s=copy.deepcopy(file)
    p=analysis.discrete.KeyWeightKeyAnalysis()
    wa=analysis.windowed.WindowedAnalysis(s, p)
    wa_len=len(wa._windowedStream)
    num=wa_len/2**n
    a, b = wa.analyze(int(num))

    cola=[(i[0],i[1]) for i in a]
    seta=set([(i[0],i[1]) for i in a])

    #[[x,cola.count(x)] for x in set(cola)]
    rlist=Counter(cola)
    rlist_keys=list(rlist.keys())
    rlist_vals=np.array(list(rlist.values()))
    modkeys=[rlist_keys[i][0].name for i in range(len(rlist_keys))]
    
    if '#' in s.analyze('key.krumhanslschmuckler').name:
        for k in range(len(modkeys)):
            if '-' in modkeys[k]:
                modkeys[k]=pitch.Pitch(modkeys[k]).getAllCommonEnharmonics(alterLimit=1)[0].name
    elif '-' in f.analyze('key.krumhanslschmuckler').name:
        for k in range(len(modkeys)):
            if '#' in modkeys[k]:
                modkeys[k]=pitch.Pitch(modkeys[k]).getAllCommonEnharmonics(alterLimit=1)[0].name
    
    keynames=np.array([f'{modkeys[i]} {rlist_keys[i][1]}' for i in range(len(rlist_keys))])
    tdata=np.column_stack([keynames,rlist_vals])
    tdataf=pd.DataFrame(data=tdata,columns=['key','count'])
    for i in range(len(tdataf)):
        tdataf.loc[tdataf.index[i], 'roman']=roman_from_key(file,tdataf['key'].iloc[i])

    tdataf['file']=file_name(file)

    tdataf=tdataf.apply(pd.to_numeric, errors='ignore')

    tdataf=tdataf[['file','key','roman','count']]
    tdataf['norm count']=tdataf['count']/sum(tdataf['count'])
    
    if cgrid:
        graph.plot.WindowedKey(s).run()
        g = graph.primitives.GraphColorGridLegend()
        data = analysis.discrete.KrumhanslSchmuckler().solutionLegend()
        g.data = data
        g.process()
    
    return tdataf

# m_titles=['c','c#','d','d#','e','f','f#','g','g#','a','b-','b']
# M_titles=['C','C#','D','E-','E','F','F#','G','A-','A','B-','B']

# m_circle_titles=circle_sort(m_titles)
# M_circle_titles=circle_sort(M_titles)

# def hz_b(file,b=0.03125): #with subjects

#     f=copy.deepcopy(file)
    
#     if file==a_1:
#         f.remove(f.parts[0])
    
#     keyname=f.analyze('key.krumhanslschmuckler').name
    
#     t=scale.ScalaScale(str('werck3'))
#     t.tune(f)

#     partList=[]

#     for num in range(len(f.parts)):
#         partList.append(f.parts[num].recurse().notes)
    
#     matlist=[]

#     for p in partList:
#         for i in range(len(p)):
#             if type(p[i])==note.Note:
#                 count_mat=np.array([file_name(file),keyname,p[i].measureNumber,p.id,p[i],p[i].name,p[i].beat,p[i].offset,p[i].duration.quarterLength,p[i].octave]) 
#                 c_count_mat=np.column_stack(count_mat)

#                 matlist.append(c_count_mat)
    
#     ctm=np.concatenate(matlist) #concatenate all matices into a large matrix
#     df=pd.DataFrame(data=ctm,columns=['file','key','measure','part','n1','n1 name','beat','offset','n1 duration','octave'])
#     df=df.apply(pd.to_numeric, errors='ignore')

#     n_df=copy.deepcopy(df[df['beat']%b==0])
    
#     for i in range(len(n_df)-1):
#         if n_df['part'].iloc[i]==n_df['part'].iloc[i+1]:
#             n_df.loc[n_df.index[i], 'cents']=round(abs(interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).cents))%1200
#             n_df.loc[n_df.index[i], 'cents from just']=cents_from_just(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1])
#             n_df.loc[n_df.index[i], 'semitones']=round(abs(interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).semitones))%12
#             n_df.loc[n_df.index[i], 'generic interval']=int(''.join(filter(str.isdigit, interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).simpleName)))
#             n_df.loc[n_df.index[i], 'name']=interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).name
#             n_df.loc[n_df.index[i], 'simple name']=interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).simpleName
#             n_df.loc[n_df.index[i], 'directed name']=interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).directedName
#             n_df.loc[n_df.index[i], 'direction']=str(interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).direction==1)
#             n_df.loc[n_df.index[i], 'total semitones']=round(abs(interval.Interval(n_df['n1'].iloc[i],n_df['n1'].iloc[i+1]).semitones))
#             n_df.loc[n_df.index[i], 'n2 duration']=n_df['n1'].iloc[i+1].duration.quarterLength
#             n_df.loc[n_df.index[i], 'n2 name']=n_df['n1'].iloc[i+1].name
#             n_df.loc[n_df.index[i], 'subject']=str(in_subject(file,n_df['n1'].iloc[i],n_df['n1'].iloc[i+1])[0])
#             n_df.loc[n_df.index[i], 'subject offset']=float(in_subject(file,n_df['n1'].iloc[i],n_df['n1'].iloc[i+1])[1])
    
#     n_df=n_df[['file','key','cents','cents from just','semitones','generic interval','name','directed name','direction','total semitones','n1 duration','n2 duration','offset','beat','n1 name','n2 name','octave','measure','part','subject','subject offset','n1']]
#     n_df.drop(n_df.index[-1])
    
#     return n_df

# for c-sharp minor fugues double subjects

def hz_full_csh(file): #with subjects

    f=copy.deepcopy(file)
    
    if file==a_1:
        if len(f.parts)==5:
            f.remove(f.parts[0])
    
    if file==Csh_1:
        keyname=str('C# major')
    else:
        keyname=f.analyze('key.krumhanslschmuckler').name
    
    t=scale.ScalaScale(str('werck3'))
    t.tune(f)

    #get subjects
    subject_list=get_subjects(file)                  
    flist=flatten_list(subject_list, [])
    slisti=[]
    slisto=[]

    for n in flist:
        for j in range(len(n)):
            slisti.append([(i.site.id, i.offset[1]) for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])
            slisto.append([n[j].offset for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])

    slisti=flatten_list(slisti,[])
    slisto=flatten_list(slisto,[])
    
    ndf=pd.DataFrame([slisti]).T
    ndf.columns=['gv']
    ndf['lv']=slisto
    
    #subject 1
    subject_list1=get_subjects_1(file)                  
    flist=flatten_list(subject_list1, [])
    slisti=[]
    slisto=[]

    for n in flist:
        for j in range(len(n)):
            slisti.append([(i.site.id, i.offset[1]) for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])
            slisto.append([n[j].offset for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])

    slisti=flatten_list(slisti,[])
    slisto=flatten_list(slisto,[])
    
    ndf1=pd.DataFrame([slisti]).T
    ndf1.columns=['gv']
    ndf1['lv']=slisto
    
    #subject 2
    subject_list2=get_subjects_2(file)                  
    flist=flatten_list(subject_list2, [])
    slisti=[]
    slisto=[]

    for n in flist:
        for j in range(len(n)):
            slisti.append([(i.site.id, i.offset[1]) for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])
            slisto.append([n[j].offset for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])

    slisti=flatten_list(slisti,[])
    slisto=flatten_list(slisto,[])
    
    ndf2=pd.DataFrame([slisti]).T
    ndf2.columns=['gv']
    ndf2['lv']=slisto
    
    #end get subjects

    partList=[]

    for num in range(len(f.parts)):
        partList.append(f.parts[num].recurse().notes)
    
    matlist=[]

    for p in partList:
        for i in range(len(p)-1):
            if type(p[i])==note.Note and type(p[i+1])==note.Note:
                count_mat=np.array([file_name(file), keyname, round(abs(interval.Interval(p[i],p[i+1]).cents))%1200,cents_from_just(p[i],p[i+1]),round(abs(interval.Interval(p[i],p[i+1]).semitones))%12,int(''.join(filter(str.isdigit, interval.Interval(p[i],p[i+1]).simpleName))),interval.Interval(p[i],p[i+1]).simpleName,interval.Interval(p[i],p[i+1]).name,interval.Interval(p[i],p[i+1]).directedName,str(interval.Interval(p[i],p[i+1]).direction==1),round(abs(interval.Interval(p[i],p[i+1]).semitones)),p[i].duration.quarterLength,p[i+1].duration.quarterLength,p[i].offset,p[i].beat,p[i].name,p[i+1].name,p[i].octave,p[i+1].octave,p[i].measureNumber,get_spine_v(p.id),str(in_subject_s(ndf,p[i],p[i+1])[0]),float(in_subject_s(ndf,p[i],p[i+1])[1]),str(in_subject_s(ndf1,p[i],p[i+1])[0]),float(in_subject_s(ndf1,p[i],p[i+1])[1]),str(in_subject_s(ndf2,p[i],p[i+1])[0]),float(in_subject_s(ndf2,p[i],p[i+1])[1])]) 
                c_count_mat=np.column_stack(count_mat)
                
                matlist.append(c_count_mat)
    
    ctm=np.concatenate(matlist) #concatenate all matices into a large matrix
    df=pd.DataFrame(data=ctm,columns=['file','key','cents','cents from just','semitones','generic interval','simple name','name','directed name','direction','total semitones','n1 duration','n2 duration','offset','beat','n1 name','n2 name','n1 octave','n2 octave','measure','part','subject','subject offset','subject 1','subject 1 offset','subject 2','subject 2 offset']) #convert numpy array into pandas dataframe
    df=df.apply(pd.to_numeric, errors='ignore')

    
    return df

def hz_t_csh(file,new_key): #THIS ONE FOR NOW
    
    f=copy.deepcopy(file)
    
    if file==a_1:
        if len(f.parts)==5:
            f.remove(f.parts[0])
    
    if file==Csh_1:
        old_key=str('C#')
        name=str('C# major')
    else:
        old_key=f.analyze('key.krumhanslschmuckler').name.partition(' ')[0]
        name=f.analyze('key.krumhanslschmuckler').name
    
    if file in wtc_1:
        if name=='E- minor':
            old_key='D#'
    
    trans_int=interval.Interval(note.Note(old_key),note.Note(new_key))
            
    if abs(trans_int.semitones)>6:
        c_trans_int=interval.subtract(['P8', trans_int.name])
        if trans_int.direction==1:
            c_trans_int=c_trans_int.reverse()
            trans_int=c_trans_int
        else:
            trans_int=c_trans_int
        
    tf=f.transpose(trans_int)
    
    if file==Csh_1:
        newname=str(f'{new_key} major')
    else:
        newname=tf.analyze('key.krumhanslschmuckler').name
    
    t=scale.ScalaScale(str('werck3'))
    t.tune(tf)

    #get subjects
    subject_list=get_subjects(file)                  
    flist=flatten_list(subject_list, [])
    slisti=[]
    slisto=[]

    for n in flist:
        for j in range(len(n)):
            slisti.append([(i.site.id, i.offset[1]) for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])
            slisto.append([n[j].offset for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])

    slisti=flatten_list(slisti,[])
    slisto=flatten_list(slisto,[])
    
    ndf=pd.DataFrame([slisti]).T
    ndf.columns=['gv']
    ndf['lv']=slisto
    
    #subject 1
    subject_list1=get_subjects_1(file)                  
    flist=flatten_list(subject_list1, [])
    slisti=[]
    slisto=[]

    for n in flist:
        for j in range(len(n)):
            slisti.append([(i.site.id, i.offset[1]) for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])
            slisto.append([n[j].offset for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])

    slisti=flatten_list(slisti,[])
    slisto=flatten_list(slisto,[])
    
    ndf1=pd.DataFrame([slisti]).T
    ndf1.columns=['gv']
    ndf1['lv']=slisto
    
    #subject 2
    subject_list2=get_subjects_2(file)                  
    flist=flatten_list(subject_list2, [])
    slisti=[]
    slisto=[]

    for n in flist:
        for j in range(len(n)):
            slisti.append([(i.site.id, i.offset[1]) for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])
            slisto.append([n[j].offset for i in n[j].contextSites(returnSortTuples=True) if fnmatch.fnmatch(str(i.site.id),'spine_?')])

    slisti=flatten_list(slisti,[])
    slisto=flatten_list(slisto,[])
    
    ndf2=pd.DataFrame([slisti]).T
    ndf2.columns=['gv']
    ndf2['lv']=slisto
    
    #end get subjects

    partList=[]

    for num in range(len(tf.parts)):
        partList.append(tf.parts[num].recurse().notes)
    
    matlist=[]

    for p in partList:
        for i in range(len(p)-1):
            if type(p[i])==note.Note and type(p[i+1])==note.Note:
                count_mat=np.array([file_name(file), name, newname, round(abs(interval.Interval(p[i],p[i+1]).cents))%1200,cents_from_just(p[i],p[i+1]),round(abs(interval.Interval(p[i],p[i+1]).semitones))%12,int(''.join(filter(str.isdigit, interval.Interval(p[i],p[i+1]).simpleName))),interval.Interval(p[i],p[i+1]).simpleName,interval.Interval(p[i],p[i+1]).name,interval.Interval(p[i],p[i+1]).directedName,str(interval.Interval(p[i],p[i+1]).direction==1),round(abs(interval.Interval(p[i],p[i+1]).semitones)),p[i].duration.quarterLength,p[i+1].duration.quarterLength,p[i].offset,p[i].beat,p[i].name,p[i+1].name,p[i].octave,p[i+1].octave,p[i].measureNumber,get_spine_v(p.id),str(in_subject_s(ndf,p[i],p[i+1])[0]),float(in_subject_s(ndf,p[i],p[i+1])[1]),str(in_subject_s(ndf1,p[i],p[i+1])[0]),float(in_subject_s(ndf1,p[i],p[i+1])[1]),str(in_subject_s(ndf2,p[i],p[i+1])[0]),float(in_subject_s(ndf2,p[i],p[i+1])[1])]) 
                c_count_mat=np.column_stack(count_mat)
                
                matlist.append(c_count_mat)
    
    ctm=np.concatenate(matlist) #concatenate all matices into a large matrix
    df=pd.DataFrame(data=ctm,columns=['file','original key','key','cents','cents from just','semitones','generic interval','simple name','name','directed name','direction','total semitones','n1 duration','n2 duration','offset','beat','n1 name','n2 name','n1 octave','n2 octave','measure','part','subject','subject offset','subject 1','subject 1 offset','subject 2','subject 2 offset']) #convert numpy array into pandas dataframe
    df=df.apply(pd.to_numeric, errors='ignore')

    
    return df
