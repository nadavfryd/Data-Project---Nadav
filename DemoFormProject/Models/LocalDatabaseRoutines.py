"""
Used structures and classes
"""
from os import path
import json
import pandas as pd

def create_LocalDatabaseServiceRoutines():
    return LocalDatabaseServiceRoutines()

class LocalDatabaseServiceRoutines(object):
    def __init__(self):
        self.name = 'Data base service routines'
        self.index = {}
        self.UsersDataFile = path.join(path.dirname(__file__), '..\\static\\Data\\users.csv')
        self.ContactDataFile = path.join(path.dirname(__file__), '..\\static\\Data\\contact.csv')

# -------------------------------------------------------
# Read users data into a dataframe
# -------------------------------------------------------
    def ReadCSVUsersDB(self):
        df = pd.read_csv(self.UsersDataFile)
        return df

# -------------------------------------------------------
# Saves the DataFrame (input parameter) into the users csv
# -------------------------------------------------------
    def WriteCSVToFile_users(self, df):
        df.to_csv(self.UsersDataFile, index=False)

# -------------------------------------------------------
# Check if username is in the data file
# -------------------------------------------------------
    def IsUserExist(self, UserName):
        # Load the database of users
        df = self.ReadCSVUsersDB()
        df = df.set_index('username')
        return (UserName in df.index.values)

# -------------------------------------------------------
# return boolean if username/password pair is in the DB
# -------------------------------------------------------
    def IsLoginGood(self, UserName, Password):
        # Load the database of users
        df = self.ReadCSVUsersDB()
        df=df.reset_index()
        selection = [UserName]
        df = df[pd.DataFrame(df.username.tolist()).isin(selection).any(1)]

        df = df.set_index('password')
        return (Password in df.index.values)
     
# -------------------------------------------------------
# Add a new user to the DB
# -------------------------------------------------------
    def AddNewUser(self, User):
        # Load the database of users
        df = self.ReadCSVUsersDB()
        dfNew = pd.DataFrame([[User.FirstName.data, User.LastName.data, User.PhoneNum.data, User.EmailAddr.data, User.username.data, User.password.data]], columns=['FirstName', 'LastName', 'PhoneNum', 'EmailAddr',  'username', 'password'])
        dfComplete = df.append(dfNew, ignore_index=True)
        self.WriteCSVToFile_users(dfComplete)

 # -------------------------------------------------------
 # Contact
 # -------------------------------------------------------

    def ReadCSVContactDB(self):
        df = pd.read_csv(self.ContactDataFile)
        return df

    def WriteCSVToFile_contact(self, df):
        df.to_csv(self.ContactDataFile, index=False)

    def AddContact(self, Contact):
        # Load the database of contact
        df = self.ReadCSVContactDB()
        dfNew = pd.DataFrame([[Contact.FirstName.data, Contact.LastName.data, Contact.PhoneNumber.data, Contact.EMail.data, Contact.Message.data]], columns=['FirstName', 'LastName', 'PhoneNumber', 'E-Mail', 'Message'])
        dfComplete = df.append(dfNew, ignore_index=True)
        self.WriteCSVToFile_contact(dfComplete)

