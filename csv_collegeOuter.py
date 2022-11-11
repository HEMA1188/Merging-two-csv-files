import pandas as pd
import matplotlib.pyplot as plt
#merge those two csv files (after getting as dataframes, get them as a single dataframe)
df1=pd.read_csv("D:/Pandas Task4/college_1.csv")
df2=pd.read_csv("D:/Pandas Task4/college_2.csv")

Outcome1=pd.merge(df1,df2, how='outer')
print(Outcome1)


'''
#Take each csv file , split that csv file into multiple categories (example csv files are added in the repo)
data1 = pd.read_csv("D:/Machine Learning/college_1.csv")
 
# no of csv files with row size

k = 2
size = 5
 
for i in range(k):
    df = data1[size*i:size*(i+1)]
    df.to_csv(f'college_1_{i+1}.csv', index=False)
 
df_1 = pd.read_csv("college_1_1.csv")
print(df_1)
 
df_2 = pd.read_csv("college_1_2.csv")
print(df_2)
#Split into Column wise
for (department), group in data.groupby(['Department']):
     group.to_csv(f'{department}.csv', index=False)
 
#print(pd.read_csv("Computer Science and Engineering.csv"))
#print(pd.read_csv("Electronics and Communication Engineering.csv"))
com=pd.read_csv("Computer Science and Engineering.csv")
print(com)
ele=pd.read_csv("Electronics and Communication Engineering.csv")
print(ele)

#consider if the codekata score exceeds 15000 points(present week) then make a csv on those observations as Exceeded expectations.csv
#if 10000<codekata score<15000 (Reached_expectations.csv)
#if 7000<codekata score<10000 (Needs_Improvement.csv)
#if codekate score < 7000 (Unsatisfactory.csv)

Exedata2=data2.loc[data2["CodeKata Score"]<15000 and data2["CodeKata Score"]>10000]
print(Exedata2)
'''
'''
data2['Excedeed'] = data2['CodeKata Score'].apply(lambda x: 'Excedeed Expectation' if x > 15000 else 'Nan')
data2["Reached Expect"]=data2['CodeKata Score'].apply(lambda x1:"Reached_Expectation " if x1<= 15000 and x1> 10000 else 'Nan')
data2['Needs Improve']=data2['CodeKata Score'].apply(lambda x2:"Needs_Improvement" if x2<=10000 and x2> 7000 else 'Nan')
data2['Unsatisfactory']=data2['CodeKata Score'].apply(lambda x3:"Unsatisfactory" if x3<=7000 else 'Nan')
print(data2)
'''
'''
for (Excede), group in data2.groupby(['Excedeed']):
     group.to_csv(f'{Excede}.csv', index=False)
     
     
ExeExpect=pd.read_csv("Exceeded Expectation.csv")

print(ExeExpect)
'''
'''

for (Reached), group in data2.groupby(['Reached Expect']):
     group.to_csv(f'{Reached}.csv', index=False)
     
     
Reach=pd.read_csv("Reached_Expectation.csv")

print(Reach)


'''
'''
for (Needs), group in data2.groupby(['Needs Improve']):
     group.to_csv(f'{Needs}.csv', index=False)
     
     
NeedImprove=pd.read_csv("Needs_improvement.csv")

print(NeedImprove)
'''

'''
for (unsatis), group in data2.groupby(['Unsatisfactory']):
     group.to_csv(f'{unsatis}.csv', index=False)
     
     
UnsatisF=pd.read_csv("Unsatisfactory.csv")

print(UnsatisF)
'''
#Average of previous week geekions vs this week geekions (i.e Previous Geekions vs CodeKata Score)
'''
Outcome1['Avg']=Outcome1[['Previous Geekions', 'CodeKata Score']].mean(axis=1)
print(Outcome1)


#No of students participated
No_of_Stud_Participate=len(Outcome1.axes[0])
print(No_of_Stud_Participate)

#Average completion of python course or my_sql or python english or computational thinking

Outcome1['Avg_of_Complection']=Outcome1[['python'or'mysql'or'python_en'or'computational_thinking']].mean(axis=1)
print(Outcome1)

'''
'''
#rising star of the week (top 3 candidate who performed well in that particular week)

Top3=Outcome1.nlargest(3,['Rising'])
print(Top3)
'''

#Shining stars of the week (top 3 candidates who has highest geekions)


Top3Geekcoin=Outcome1.nlargest(3,['Previous Geekions'])
print(Top3Geekcoin)

#Department wise codekata performence (pie chart)
'''
#Department wise codekata performence (pie chart)
fig = plt.figure(figsize =(30, 20))
plt.pie(Outcome1['CodeKata Score'], labels = Outcome1['Department'])
plt.show()
'''
'''
sums = Outcome1.groupby(Outcome1["Department"])["CodeKata Score"].sum()

plt.pie(sums, labels=sums.index);
plt.show()
'''

#Department wise toppers (horizantal bar graph or any visual representations of your choice)

'''
X=Outcome1['Department']
Y=Outcome1['Avg']
plt.bar(X,Y)
plt.xlabel('Department')
plt.ylabel('Topper')
plt.title('Vertical Graph')
plt.show()
'''