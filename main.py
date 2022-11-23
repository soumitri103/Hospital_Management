# This is a sample Python script.

import pandas as pd
# Add Different Hospital Details in New Sheet with different Begining from 0
sheet = int(input("Enter the sheet name based on name on the Board : "))
data = pd.read_excel(r'C:\Users\soumi\Downloads\Hospital Management.xlsx',sheet_name=sheet)
class Hospital:
    def doctor():
        df = pd.DataFrame(data, columns=['Doctor','Qualification','Specialization','Experience','Salary'])
        print(df)
    def Nurse():
        df = pd.DataFrame(data, columns=['Nurse','Qualification','Specialization','Experience','Salary'])
        print(df)
    def AsstNurse():
        df = pd.DataFrame(data, columns=['Asst.Nurse', 'Qualification', 'Specialization', 'Experience'])
        print(df)
    def Patient():
        df = pd.DataFrame(data, columns=['Patient','Issue','Gender','Age'])
        print(df)


#1=doctor,2=patient,3=worker,4=cowerker
print('Please Enter your choices Dear user  : [1,2,3,4] ')
casevalue=int(input())
if(casevalue==1):
  Hospital.doctor()
elif(casevalue==2):
  Hospital.Patient()
elif(casevalue==3):
  Hospital.Nurse()
elif(casevalue==4):
    Hospital.AsstNurse()
else:
  print('run the existed code one more time and enter a valid choice')
print("Thank you ")