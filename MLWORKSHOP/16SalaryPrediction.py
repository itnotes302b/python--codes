import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def welcome():
    print("Welcome to sylary Prediction using ML")
    print("Press any key to comtinue")
    input()

def checkcsv():
    csv_files=[]
#    cur_dir=os.getcwd()
    content_list=os.listdir(os.getcwd())
    for x in content_list:
        if x.split('.')[-1]=='csv':   # We know the split function bit [-1] will give the name/data after . eg abc.csv [-1] will give csv
            csv_files.append(x)

    if len(csv_files)==0:
        return "NO CSV FILE FOUND IN DIRECTORY"
    else:
        return csv_files

# selecting CSV FILE
def select_csv(csv_files):
    i=0
    for fname in csv_files :
        print(i ,"------" ,fname)
        i+=1
        # input and int user se input lega ie 0,1,2,3 and that also become the index of csv_files hence file will return
    return csv_files[int(input("SELECT FILE TO CREATE ML MODEL "))]

#def graph(X_train ,Y_train,X_test ,Y_test ,Y_predict):

def graph(X_train ,Y_train,regressionObject,X_test ,Y_test ,Y_predict):
    plt.scatter(X_train,Y_train,color='red',label='Tranning Data')
    plt.plot(X_train,regressionObject.predict(X_train),color='blue',label='Best Fit')
#    plt.plot(X_train,Y_predict,color='blue',label='Best Fit')
    plt.scatter(X_test,Y_test,color='green',label='Test Data')
    plt.scatter(X_test,Y_predict,color='black',label='Predicted test data')
    plt.title('Salary vs Experience ')
    plt.xlabel('Years of Experience')
    plt.ylabel('Salary')
    plt.legend()
    plt.show()



if __name__ == '__main__':
#    def main():
        welcome()
        try:
            csv_files = checkcsv()
            if csv_files == "NO CSV FILE FOUND IN DIRECTORY":
                raise FileNotFoundError('NO CSV FILE FOUND IN DIRECTORY')
            csv_file = select_csv(csv_files)
            print(csv_file, " is selected ")
            print("Reading CSV file ...... ")
            print('Creating data set ......')
            dataset = pd.read_csv(csv_file)
            print("DATA SET created ")
            # optaining X and Y
            X = dataset.iloc[:, :-1].values
            # : / colen select all rows and :-1 select all column from starting except last one because -1 is excluded in sclicing
            Y = dataset.iloc[:, -1].values
            # : / colen select all rows and -1 directly select last column using sclicing
            s = float(input("enter test data range between 0 to 1"))
            X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=s)
            # train_test_split(X,Y,test_size=s) will return 4 values
            # If s=test data =20
            # X and Y are two columns , jitne X hai utne hai Y hai
            # If 20 % data 0become test data & 80% data become tranning data
            # ie 80 % X ka 80 % Y ka = tarnning data
            # ie 20% X ka 20 % Y ka = testing data
            # hence 4 value will return and we store 4value in new varibales
            print("Model Creation  in process")
            regressionObject = LinearRegression()  # Object will created
            regressionObject.fit(X_train, Y_train)  # in this line regression line will created using tranning data
            print(" Model is created ")
            print("press enter key to predict data ")
            input()
            Y_predict=regressionObject.predict(X_test)
#            Y_predict = regressionObject.predict(X_test)

            print("X_test,'......',Y_test,'......',Y_predict")
            i = 0

            while i < len(Y_predict):
                print(X_test[i], '....', Y_test[i], '....', Y_predict[i])
                i += 1

            print("Press any key to see above information in graphical format")
            input()
            graph(X_train, Y_train, regressionObject, X_test, Y_test, Y_predict)
#            graph(X_train, Y_train,  X_test, Y_test, Y_predict)

            r2 = r2_score(Y_test, Y_predict)
            print('our model is %2.2f%% accurate ' % (r2 * 100))

            print("NOW you can predict salary of employeess using our model ")

            print("Enter experience of candidate , seperated by comma ")
            exp = [float(e) for e in input().split(',')]
            ex = []
            for x in exp:
                ex.append([x])

            experience = np.array(ex)
            salaries = regressionObject.predict(experience)

            plt.scatter(experience, salaries, color='black')

            plt.xlabel('Years of Experience ')
            plt.ylabel('Salaries ')
            plt.show()

            d = pd.DataFrame({'Experience': exp, 'salaries': salaries})
            print(d)


        except FileNotFoundError:
            print('NO CSV FILE FOUND IN DIRECTORY')
            print("plese enter to exit()")
            input()
            exit()
#   main()
#    input()
