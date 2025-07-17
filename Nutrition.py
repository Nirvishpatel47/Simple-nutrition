import json        
import os
import time
import pandas as pd
import matplotlib.pyplot as  plt
import seaborn as sns
import datetime
from datetime import datetime,timedelta


#To create and open the data and also to make it dataframe
try:
    time.sleep(0.1)
    with open(r"D:\HTML tutorial\alltext\Data.txt","r") as file:
        uk = file.readline()
        wk = file.readline()
        hk = file.readline()
        ak = file.readline()
    user_name = uk
    weight = int(wk)
    height = int(hk)
    age = int(ak)
    time.sleep(1)
    with open(r"D:\HTML tutorial\Python\Nutrition.json",'r') as file:
        content = json.load(file)
        df_uncleaned = pd.DataFrame(content)
        df = df_uncleaned.drop_duplicates()
except Exception as e:
    print("Some error occured please try again.")
    time.sleep(0.1)
    print(f"Error is {e}")

    
#For the user info!
def user():
    try:
        print("Hello User")
        time.sleep(0.1)
        print("Please Enter your Name: ")
        user_name = input()
        time.sleep(0.1)
        print(f"So {user_name}!, Please entr your Weight,Age and Height: ")
        time.sleep(0.1)
        weight = int(input("Enter your weight (In KG): "))
        time.sleep(0.1)
        height = int(input("Enter your Height (In CM): "))
        time.sleep(0.1)
        age = int(input("Enter your age: "))
        time.sleep(0.1)
        print("------------------------------")
        time.sleep(0.1)
        print("1.Add the data")
        time.sleep(0.1)
        print("2.New user")
        i = int(input())
        if i == 1:
            with open(r"D:\HTML tutorial\Data.txt","w") as file:
                file.write(str(user_name + "\n"))
                file.write(str(weight) + "\n")
                file.write(str(height) + "\n")
                file.write(str(age) + "\n")
            print("Data added sucessfully")
        elif i == 2:
            user()
    except Exception as e:
        print("Some error is occurred!")
        time.sleep(0.1)
        print(f"Error is {e}")


#For BMR
def BMR():
    print("To calculate BMR: ")
    time.sleep(0.1)
    print("1.For Men")
    time.sleep(0.1)
    print("2.For women")
    g = int(input())
    if g == 1:
        global men_bmr
        men_bmr = 10 * weight + 6.25 * height - 5 * age + 5
    elif g == 2:
        global women_bmr
        women_bmr = men_bmr = 10 * weight + 6.25 * height - 5 * age - 161


#How much nutrition a person needs?
def report():
    try:
        BMR()
        print("You need: ")
        time.sleep(0.1)
        print(f"{round(1.2 * int(weight))}-{round(2.2 * int(weight))}Protein")
        time.sleep(0.1)
        print("30-38g of Fiber")
        time.sleep(0.1)
        print("900mg Vit A")
        time.sleep(0.1)
        print("90mg Vit C")
        time.sleep(0.1)
        print("15mcg Vit D")
        time.sleep(0.1)
        print("15mg Vit E")
        time.sleep(0.1)
        print("120mcg Vit K")
        time.sleep(0.1)
        print("2.4 mcg Vit B12")
        time.sleep(0.1)
        print("1000mg Calcium")
        time.sleep(0.1)
        print("8mg Iron")
        time.sleep(0.1)
        print("400-420mg Magnesium")
        time.sleep(0.1)
        print("3400mg Potassium")
        time.sleep(0.1)
        print("1.6g Omega 3")
    except Exception as e:
        print("Some error occured! Please try again")
        time.sleep(0.1)
        print(f"Error is {e}")


#for adding food to the yesterday
def yesterday():
    try:
        while True:
            time.sleep(0.1)
            key = input("Enter the food you eat:  ").lower()
            while True:
                if  key == "tmt":
                    yesterday() 
                elif type(key) == str:
                    break 
                else:
                    print("This is an invalid statement please try again...")
            row = df[df["food"].str.lower()==key]
            #To check that key is present in row or not
            if row.empty:
                suggestion(key[:2])
            else:
                break
        new_row = row.copy()
        var = {row["per"].iloc[0]}
        time.sleep(0.1)
        print(f"In {var}")
        time.sleep(0.1)
        while True:
            how_much = float(input("How much(Kindly use common sense): "))
            if type(how_much) == float:
                break
            else:
                time.sleep(0.1)
                print("Invalid Input please Try again...")
                time.sleep(0.1)
                print("------------------------------")
            
        new_row.loc[:,new_row.dtypes != 'object'] *= how_much
        append_row(new_row,0)
            
    except Exception as e:
        time.sleep(0.1)
        print("Some error occured pease try again...")
        time.sleep(0.1)
        print(f"Error is {e}")


#For retriving value from the user:
def value_retrive(tms):
    try:
        if tms == 1:
            while True:
                while True:
                    time.sleep(0.1)
                    key = input("Enter the food you eat (or Enter Exit):  ").lower()
                    while True: 
                        if key == "exit":
                            return 0
                        elif key == None:
                            break
                        elif type(key) == str:
                            break 
                        else:
                            print("This is an invalid statement please try again...")
                    row = df[df["food"].str.lower()==key]
                    #To check that key is present in row or not
                    if row.empty:
                        suggestion(key[:2])
                    else:
                        break
                new_row = row.copy()
                var = {row["per"].iloc[0]}
                time.sleep(0.1)
                print(f"In {var}")
                time.sleep(0.1)
                while True:
                    how_much = float(input("How much(Kindly use common sense): "))
                    if type(how_much) == float:
                        break
                    else:
                        time.sleep(0.1)
                        print("Invalid Input please Try again...")
                        time.sleep(0.1)
                        print("------------------------------")
                    
                new_row.loc[:,new_row.dtypes != 'object'] *= how_much
                append_row(new_row,1)
        else:
            while True:
                time.sleep(0.1)
                key = input("Enter the food you eat:  ").lower()
                while True: 
                    if key == "exit":
                        return 0
                    elif key == None:
                        break
                    elif type(key) == str:
                        break 
                    else:
                        print("This is an invalid statement please try again...")
                row = df[df["food"].str.lower()==key]
                #To check that key is present in row or not
                if row.empty:
                    suggestion(key[:2])
                else:
                    break
                new_row = row.copy()
                var = {row["per"].iloc[0]}
                time.sleep(0.1)
                print(f"In {var}")
                time.sleep(0.1)
                while True:
                    how_much = float(input("How much(Kindly use common sense): "))
                    if type(how_much) == float:
                        break
                    else:
                        time.sleep(0.1)
                        print("Invalid Input please Try again...")
                        time.sleep(0.1)
                        print("------------------------------")
                    
                new_row.loc[:,new_row.dtypes != 'object'] *= how_much
                append_row(new_row,1)
            
    except Exception as e:
        time.sleep(0.1)
        print("Some error occured pease try again...")
        time.sleep(0.1)
        print(f"Error is {e}")


#For appending rows:
def append_row(new_row,eda):
    try:
        file_path = r"D:\HTML tutorial\Python\Nutri.xlsx"
        df_exesting = pd.read_excel(file_path)
        if eda == 1:
            date = datetime.today().strftime("%d-%m-%y")
        elif eda == 0:
            date_uf = datetime.now() - timedelta(days=1)
            date = date_uf.strftime("%d-%m-%y")
        else:
            print("Error!")
        new_row["Date"] = date
        df_updated1 = pd.DataFrame(new_row)   
        df_updated = pd.concat([df_exesting,df_updated1],ignore_index=True)
        df_updated.to_excel(file_path,index=False)
        time.sleep(0.1)
        print("---------------------------")
        time.sleep(0.1)
        print("Row append sucessfully!")
    except Exception as e:
        time.sleep(0.1)
        print("Some errpr occured please try again...")
        time.sleep(0.1)
        print(f"Error is {e}")


#To read a file
def read():
    try:
        print("1.Read whole File")
        time.sleep(0.1)
        print("2.See the Data for specific Date")
        time.sleep(0.1)
        print("3.See the Data of Today")
        time.sleep(0.1)
        print("4.To see How much Nutrition you need")
        ept = int(input())
        if ept == 1:
            file_path = r"D:\HTML tutorial\Python\Nutri.xlsx"
            reading_file = pd.read_excel(file_path)
            print(reading_file)
        elif ept == 2:
            while True:
                file_path = r"D:\HTML tutorial\Python\Nutri.xlsx"
                kd = pd.read_excel(file_path)
                date = input("Enter the 'DATE' in (dd-mm-yy): ")
                selected_data = kd[kd["Date"] == date]
                if selected_data.empty:
                    print("Invalid Date or Date not Exists Please Try Again.")
                else:
                    break
            print("------------------------------")
            time.sleep(0.1)
            print(selected_data)
            time.sleep(0.1)
            print("------------------------------")
        elif ept == 3:
            file_path = r"D:\HTML tutorial\Python\Nutri.xlsx"
            kd = pd.read_excel(file_path)
            date = datetime.today().strftime("%d-%m-%y")
            selected_data = kd[kd["Date"] == date]
            print("------------------------------")
            time.sleep(0.1)
            print(selected_data)
            time.sleep(0.1)
            print("------------------------------")
        elif ept == 4:
            if os.path.getsize("Data.txt") == 0:
                d = 2
            else:
                d = 1
            if d == 1:
                report()
            elif d == 2:
                print("So please Register yourself First!")
                time.sleep(0.1)
            else:
                print("Invalid Statement. Please try again.")
        else:
            print("Invalid Statement. Please try again")
    except Exception as e:
        time.sleep(0.1)
        print("Some error occured please try again.")
        time.sleep(0.1)
        print(f"Error is {e}")

def file_location():
    try:
        time.sleep(0.1)
        print("Data: ")
        time.sleep(0.1)
        print("From chat gpt")
        time.sleep(0.1)
        print("Source: ")
        time.sleep(0.1)
        print("The libraries used in this program is:")
        time.sleep(0.1)
        print("Json")
        time.sleep(0.1)
        print("Pandas")
        time.sleep(0.1)
        print("OS")
        time.sleep(0.1)
        print("Time")
        time.sleep(0.1)
        print("Seaborn")
        time.sleep(0.1)
        print("metplotlib.pyplot")
        time.sleep(0.1)
        print(f"The data is taken from: {os.path.abspath('Nutrition.json')}")
        time.sleep(0.1)
        print("Stored: ")
        time.sleep(0.1)
        print(f"The data stored in : {os.path.abspath('Nutri.xlsx')}")
    except Exception as e:
        print("Some error occured please try again.")
        time.sleep(0.1)
        print("Error is {e}")


#Just to read entire file for better vision
def sml_read():
    file_path = r"D:\HTML tutorial\Python\Nutri.xlsx"
    reading_file = pd.read_excel(file_path)
    print(reading_file)


#To remove the rows
def remove_rows():
    try:
        time.sleep(0.1)
        print("1.Remove last row")
        time.sleep(0.1)
        print("2.Remove specific row")
        time.sleep(0.1)
        print("3.Remove multiple rows")
        kt = input()
        if kt == "1":
            sml_read()
            print("------------------------------")
            time.sleep(0.1)
            print("This will remove the last row from the excel sheet...")
            file_path = r"D:\HTML tutorial\Python\Nutri.xlsx"
            reading_file = pd.read_excel(file_path)
            print("------------------------------")
            print(reading_file)
            print("------------------------------")
            updated_file = reading_file.iloc[:-1]
            with pd.ExcelWriter(file_path,mode="w") as writer:
                updated_file.to_excel(writer,index=False)
            time.sleep(0.1)
            print("Rows deleted sucessfully!")
        elif kt == "2":
            sml_read()
            time.sleep(0.1)
            c = int(input("Enter the index you want to remove: "))
            kd = pd.read_excel(r"D:\HTML tutorial\Python\Nutri.xlsx")
            kd = kd.drop(c)
            with pd.ExcelWriter(r"D:\HTML tutorial\Python\Nutri.xlsx",mode="w") as writer:
                kd.to_excel(writer,index=False)
            time.sleep(0.1)
            print("Rows deleted sucessfully!")
        elif kt.lower() == "3":
            sml_read()
            print("------------------------------")
            time.sleep(0.1)
            print("WARNING. Values (0,0) can delete all the data in the file")
            time.sleep(0.1)
            print("------------------------------")
            start_row = int(input("Enter the row you want to start deleting from: "))
            time.sleep(0.1)
            end_row = int(input("Enter the number of last low you want to delete: "))
            file_path = r"D:\HTML tutorial\Python\Nutri.xlsx"
            reading_file = pd.read_excel(file_path)
            print(reading_file)
            updated_file = reading_file.iloc[start_row:end_row]
            with pd.ExcelWriter(file_path,mode="w") as writer:
                updated_file.to_excel(writer,index=False)
            time.sleep(0.1)
            print("Rows deleted sucessfully!")
    except Exception as e:
        print("Some error occured please try again.")
        time.sleep(0.1)
        print("Error is {e}")

                
#Food suggestion
def suggestion(prefix):
    try:
        prefix = prefix.lower()
        suggestion = df[df["food"].str.lower().str.startswith(prefix)]["food"].tolist()
        if suggestion:
            time.sleep(0.1)
            for i,food in enumerate(suggestion,1):
                print(f"{i}. {food}")
        
        else:
            time.sleep(0.1)
            print("No match Found please try again")
    except Exception as e:
        print("Some error occured please try again.")
        time.sleep(0.1)
        print(f"Error is {e}")


#To See the nutritional info of a food
def data_food():
    try:
        while True:
            print("1.To see data of food")
            time.sleep(0.1)
            print("2.Exit")
            k = int(input())
            if k == 1:
                key = input("Enter the food you wnat to see the details: ")
                while True:
                    if type(key) == str:
                        break
                    else:
                        print("Invalid Statement. Please try again.")
                row = df[df["food"].str.lower()==key]
                if row.empty:
                    suggestion(key[:-2])
                else:
                    pass
                print(row)
            elif k == 2:
                break
            else:
                print("Invalid Output")

            
    except Exception as e:
        print("Some error occured please te=ry again.")
        time.sleep(0.1)
        print(f"Error is {e}")


#To sum up all the columns
def numeric_sum():
    try:
        kd = pd.read_excel(r"D:\HTML tutorial\Python\Nutri.xlsx")
        time.sleep(0.1)
        print("------------------------------")
        time.sleep(0.1)
        print("1.Add to data")
        time.sleep(0.1)
        print("2.see the data")
        idk = int(input())

        #For External use only
        def Dat():
            while True:
                date = input("Enter the 'DATE' in (dd-mm-yy): ")
                selected_data = kd[kd["Date"] == date]
                if selected_data.empty:
                    print("Invalid Date or Date not Exists Please Try Again.")
                else:
                    break
            numeric_sum = selected_data.select_dtypes(include='number').sum(axis=0)
        if idk == 1:
            Dat()
            location = "data.xlsx"
            dk = pd.DataFrame(numeric_sum)
            dk.to_excel(location,index=False) 
            time.sleep(0.1)
            print("Added sucessfully...")
        elif idk == 2:  
            print("1.See the Data for Today only.")
            time.sleep(0.1)
            print("2.See the Data for specific Date.")
            edt = int(input())
            if edt == 1:
                while True:
                    date = datetime.today().strftime("%d-%m-%y")
                    selected_data = kd[kd["Date"] == date]
                    if selected_data.empty:
                        print("Invalid Date or Date not Exists Please Try Again.")
                    else:
                        break
                numeric_sum = selected_data.select_dtypes(include='number').sum(axis=0)
                print(numeric_sum)
            elif edt == 2:
                while True:
                    date = input("Enter the 'DATE' in (dd-mm-yy): ")
                    selected_data = kd[kd["Date"] == date]
                    if selected_data.empty:
                        print("Invalid Date or Date not Exists Please Try Again.")
                    else:
                        break
                numeric_sum = selected_data.select_dtypes(include='number').sum(axis=0)
                print(numeric_sum)

        else:
            time.sleep(0.1)
            print("Invalid input please try again...")
    except Exception as e:
        print("Some error occured please try again.")
        time.sleep(0.1)
        print("Error is {e}")


#To get meaningful insights from the data
def insights():
    try:
        file_location = r"D:\HTML tutorial\Python\Nutri.xlsx"
        kd = pd.read_excel(file_location)
        column_name = kd.columns.to_list()
        column = ', '.join([str(col) for col in column_name])
        print(f"From This names select the axis Boss.")
        print(column)
        #df = sns.load_dataset(file_location)
        time.sleep(0.1)
        print("Enter the chart you want to make insights.")
        time.sleep(0.1)
        print("1.Scatter plot")
        time.sleep(0.1)
        print("2.Scatter plot with third variable")
        time.sleep(0.1)
        print("3.Bar plot")
        time.sleep(0.1)
        print("4.Box plot")
        time.sleep(0.1)
        print("5.Line plot")
        time.sleep(0.1)
        p = int(input())
        print("------------------------------")
        time.sleep(0.3)
        print("Processing...")
        

        #For values
        def val():
            k = input("Enter for 'X' Axis: ")
            time.sleep(0.1)
            d = input("Enter for 'Y' Axis: ")
            return k,d
        if p == 1:
            k,d = val()
            sns.scatterplot(x=k,y=d,data=kd)
            plt.show()
        elif p == 2:
            k,d = val()
            h = input("Enter the Third variable")
            sns.scatterplot(x=k,y=d,hue=h,data=kd)
            plt.show()
        elif p == 3:
            k,d = val()
            sns.barplot(x=k,y=d,data=kd)
            plt.show()
        elif p == 4:
            k,d = val()
            sns.boxplot(x=k,y=d,data=kd)
            plt.show()
        elif p == 5:
            k,d = val()
            sns.lineplot(x=k,y=d,data=kd)
            plt.show()
        else:
            print("Invalid output")
    except Exception as e:
        print("Some error occured,Please try again.")
        time.sleep(0.1)
        print(f"Error is {e}")

    
#To provide a Structure
def menu():
    try:
        while True:
            print("------------------------------")
            print("Here is the Menu Boss!")
            time.sleep(0.1)
            print("1. Add food")
            time.sleep(0.1)
            print("2. Add multiple food")
            time.sleep(0.1)
            print("3.Add food to yesterday")
            time.sleep(0.1)
            print("4.See the data")
            time.sleep(0.1)
            print("5.See Files locations and info about programs")
            time.sleep(0.1)
            print("6.Remove Rows")
            time.sleep(0.1)
            print("7.Nutritional Info of Food")
            time.sleep(0.1)
            print("8.Get the data...")
            time.sleep(0.1)
            print("9.Get the graph")
            time.sleep(0.1)
            print("10.User Entry")
            time.sleep(0.1)
            print("11.Exit")
            time.sleep(0.1)
            print("------------------------------")
            k = int(input())
            if k == 1:
                value_retrive(0)
            elif k == 2:
                value_retrive(1)
            elif k == 4:
                read() 
            elif k == 5:
                file_location()
            elif k == 6:
                remove_rows()
            elif k == 7:
                data_food()
            elif k == 8:
                numeric_sum()
            elif k == 9:
                insights()
            elif k == 10:
                user()
            elif k == 3:
                yesterday()
            elif k == 11:
                return
            else:
                time.sleep(0.1)
                print("Invalid option. Please try Again")
    except Exception as e:
        time.sleep(0.1)
        print("Some error occured please try again...")
        time.sleep(0.1)
        print(f"Error is {e}")

if __name__ == "__main__":
    menu()