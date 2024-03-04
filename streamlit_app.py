import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics 

import streamlit as st

df_orig = pd.read_csv(r "//Dataset file path goes here//")
df = df_orig.copy()
df.dropna(axis = 1, inplace = True)

level_map = {'Not Interested':0, 'Poor':1,'Beginner':2,'Average':3,
             'Slightly Interested':4,'Moderately Interested':5,'Highly Interested':6, }

role_map = {'IT':0,'CSE/IT':1,'AI&DS':2,'CSE':3,'B.Arch':4,'B.A. , B.A.(Hons)':5,'Cyber Security / IT':6,
            'Aero space':7,'Aeronautics':8}

pred_role_map = {0: 'IT', 1: 'CSE/IT', 2: 'AI&DS', 3: 'CSE', 4: 'B.Arch', 5: 'B.A.', 6: 'Cyber Security / IT', 7: 'Aero space', 8: 'Aeronautics'}

exp_level = ('Not Interested', 'Poor', 'Beginner', 'Average', 'Slightly Interested', 'Moderately Interested', 'Highly Interested')


df.replace(level_map, inplace = True)
df.replace(role_map, inplace = True)

## Train Test Split
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,:-1],df.iloc[:,-1],test_size = 0.2,random_state=42)

clf = DecisionTreeClassifier()
clf = clf.fit(X_train,y_train)


def selectbox(subject):
    return st.selectbox(str(subject), exp_level)

st.set_page_config(
        page_title="Team Matrix",
)
st.title("Career Guidance !")
st.sidebar.success("Get to know yourselves 🚀")
st.header("Wondering which domain to choose ? Use our recommender",divider='rainbow')
st.sidebar.success("Aptitude tests!")

wbdev = selectbox('Web Development')
appdev = selectbox('App Development')
coding = selectbox('Coding')
ai = selectbox('Artificial Intelligence')
cloud = selectbox('Cloud Computing')
arch = selectbox('Architecture')
busadm = selectbox('Business Administration')
fullstack = selectbox('Full Stack Development')
ethack = selectbox('Ethical Hacking')
space = selectbox('Space')
aircraft = selectbox('Aircrafts')
swengg = selectbox('Software Engineering')
graphics = selectbox('Graphics Designing')

values= [level_map[wbdev], level_map[appdev], level_map[coding],
        level_map[ai], level_map[cloud], level_map[arch],
        level_map[busadm], level_map[fullstack], level_map[ethack],
        level_map[space], level_map[aircraft], level_map[swengg],
        level_map[graphics]]

dummy_df = pd.DataFrame(columns = df.columns[:-1])
dummy_df.loc[0] = values

pred = clf.predict(dummy_df)

st.write('Recommended Domain :', pred_role_map[pred[0]])
