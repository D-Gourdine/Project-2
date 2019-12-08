#CDTs Daniel Echeveste and Gourdine D'Angelo 
#The goal of this program is to be a basic data science suite that allows
#a user to fit and comapre general linear models and execute and evaluate
#principle component analysis.


#import sklearn
#import matplot.lib 
#from sklearn.decomposition import PCA
#from sklearn import linear_model,datasets 
#from sklearn.svm import LinearSVC
#from sklearn.feature_selection import SelectFromModel
#from sklearn.datasets import load_boston
#import matplotlib.pyplot as plt
#import numpy as np

import tkinter as tk
from tkinter import ttk

# MATTPLOTLIB USED FOR GRAPHS
import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure


LARGE_FONT = ("Stencil", 24)


dataSet = []


class math(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, "Data Analyzer")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)  # sets size and priority(weight)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (
            StartPage,
            PageOne,
            PageTwo,
        ):  # https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # streches to size of window

        self.show_frame(StartPage)  # Sets the initial screen/frame

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()  # raise the frame to the front (so that it is visible)

    def get_page(self, page_class):
        return self.frames[page_class]
    

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        tk.Frame.__init__(self, parent)

        self.label = ttk.Label(self, text="Data Analysis Helper", font=LARGE_FONT)
        self.label.pack()

        
        print(type(self.label))
        self.options = ttk.Combobox(
            self, values=["a", "b", "c","d"], width=25, justify="center"
        )  # eventually change these values to correspond to the datasets
        self.options.pack(anchor="c")
        self.options.set("Please select a data set")

        f1 = tk.Frame(width=200, height=200, background="grey")
        f1.pack(fill="both", expand=True, padx=20, pady=20)
        #page2 = self.controller.get_page(PageTwo)
        button2 = ttk.Button(
            self,
            text="Execute",
            command=lambda: [
                dataSet.append(self.options.get()),
                controller.show_frame(PageOne),
                print(dataSet[0]),
            ],
        )  # Can use the lambda to store the value of the dropdown box with the value selected to use later
        button2.pack(anchor="center")
        #PageOne_ref = self.controller.get_page(PageOne)
        
        


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        self.controller=controller
        def get_data_info(file_name):
            name=str()
            number=str()
            categories=str()
            if file_name=="a":
                name="Boston House Prices"
                number= "506"
                categories= "Crime RaTE, Prop. of Land Zoned, Prop. of Non-retial business land, NO2 Concentration, Average # of Rooms, Prop. Owner Occupied Units, Distance to Employment Centers, Accessibility to HWY, Property Tax Rate, Student teacher ratio, Proportion of African Americans, % Lower Status of Pop., Median Value of Home"
            elif file_name=="b":
                name="Diabetes"
                number="442"
                categories="Age, Sex, BMI, Average Blood Pressure, S1, S2, S3, S4, S5, S6"
            elif file_name=="d":
                name="Breast Cancer"
                number="569"
                categories="See scikit-learn Toy Data sets section"
            elif file_name=="c":
                name="Wine Recognition"
                number="178"
                categories="Alcohol, Malic Acid, Ash, Alcalinity of Ash, Magnesium, Total Phenols, Flavanoids, NonFlavanoid Phenols, Proanthocyanins, Color Intensity, Hue, OD280/OD315, Proline" 
            return name,number,categories
        tk.Frame.__init__(self, parent)
        self.Label = tk.StringVar()
        tk.Label(self, textvariable=self.Label, font = LARGE_FONT).grid(row=0, column=1)
        self.Label.set("Data Set Snapshot of: ")

        # label = tk.Label(self, text="Data Set Snapshot of: ", font=LARGE_FONT)
        # label.grid(row=0, column=1)

        button1 = ttk.Button(
            self, text="Back", command=lambda: controller.show_frame(StartPage)
        )
        button1.grid()
        button2 = ttk.Button(
            self, text="Next", command=lambda: controller.show_frame(PageTwo)
        )
        
        format_width = 80
        print(lambda: [dataSet])
        dat_var=get_data_info("a")
        text_description = "The {} data set consist of {} observations".format(dat_var[0], dat_var[1])
        text_description2= "The data has the following categories in order:"
        lis=dat_var[2].split(",")
        for i in lis:
            text_description2+="\n {}".format(i)
        Label1 = tk.Label(
            self,
            text=text_description,
            bd=25,
            bg="grey",
            width=format_width,
            wraplengt=500,
        ).grid(row=1, column=0)
        label_space = tk.Label(self, width=format_width, bg="black", bd=25).grid()
        Label2 = tk.Label(
            self, text=text_description2, bd=25, bg="grey", width=format_width
        ).grid()
        Label3 = tk.Label(
            self, text="", bd=25, bg="grey", width=format_width
        ).grid()

        Label4 = tk.Label(
            self,
            text="How would you like to proceed?",
            bd=25,
            bg="grey",
            width=format_width,
        ).grid(row=1, column=2)

        var_pca = tk.IntVar()  # 0 or 1 corresponds to whether or not this is engaged
        check_PCA = tk.Checkbutton(
            self, text="PCA", font=("Stencil", 18), variable=var_pca
        ).grid(row=2, column=2, sticky="w")

        var_lsm = tk.IntVar()  # 0 or 1 corresponds to whether or not this is engaged
        check_PCA = tk.Checkbutton(
            self, text="Lasso Model Selection", font=("Stencil", 18), variable=var_lsm
        ).grid(row=3, column=2, sticky="w")

        var_glm = tk.IntVar()  # 0 or 1 corresponds to whether or not this is engaged
        check_PCA = tk.Checkbutton(
            self, text="General Linear Model", font=("Stencil", 18), variable=var_glm
        ).grid(row=4, column=2, sticky="w")

        formatlabel_1 = tk.Label(self, bd=25, width=format_width).grid(
            row=8, column=0, padx=20
        )
        formatlabel_2 = tk.Label(self, bd=25, width=format_width).grid(
            row=8, column=1
        )
        formatlabel_3 = tk.Label(self, bd=25, width=format_width).grid(
            row=8, column=2, padx=20, pady=10
        )
        formatlabel_4 = tk.Label(self, bd=25, width=format_width).grid(
            row=9, columnspan=3, pady=10, padx=20, sticky="ew"
        )
        formatlabel_5 = tk.Label(self, bd=25, width=format_width).grid(
            row=10, columnspan=3, pady=10, padx=20, sticky="ew"
        )
        formatlabel_6 = tk.Label(self, bd=25, width=format_width).grid(
            row=11, columnspan=3, pady=10, padx=20, sticky="ew"
        )
        button2.grid(row=13, column=2, padx=20, sticky="se")
        page1 = self.controller.get_page(StartPage)
        #page1.options.set("Hello, world")
        button3 = ttk.Button(
            self, text="Back", command=lambda: [print(page1.options.get())])

        button3.grid(column =2, row = 14,  padx=20, sticky="se")

        
        
    
        

    


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        self.controller=controller
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self, text="Home Page", command=lambda: controller.show_frame(StartPage)
        )
        button1.pack(side="right", anchor="s", pady=10, padx=10)
        button2 = ttk.Button(
            self, text="Back", command=lambda: controller.show_frame(PageOne)
        )
        button2.pack(side="left", anchor="s", pady=10, padx=10)
        #page2 = self.controller.get_page(PageTwo)


app = math()
app.state("zoomed")  # Makes the application windowed fullscreen
app.mainloop()


#The code for the buttons was found under Tkinter in the python
#documentation. The code for tkinter and, specifically opening a file, 
#was gathered from python-courses.edu (https://www.python-course.eu/tkinter_dialogs.php). 
#This website was found via the readings on Tkinter for IT383 
#(http://www-internal.eecs.usma.edu/courses/it383/lessons.html). 


#function: get_data
#retrieves data from list of avaliable data sets. A single character 
#from a to g represents the data sets 
#char-->array,char
def get_data(file_name):
    '''takes a char and returns the associated data set and the character
    '''
    if file_name==a:
        data=datasets.load_boston
    elif file_name==b:
        data=datasets.load_diabetes
    elif file_name==b:
        data=datasets.load_wine
    elif file_name==d:
        data=datasets.load_breast_cancer 
    return data,file_name 

    
#function: create_test_set
#takes as input data and a float representing how much of the data
#to use for fitting 
#an array and a percentage. two new arrays 
#list,float-->list1,list2
def create_test_set(data,size_train):
    '''takes a data set and a percentage representing the number of rows to use in the 
        training set. Returns the training set and test sets in that order as nested lists
    '''
    sizeT=int(data.data[:].shape[1]*size_train)
    train_dat=data.data[:sizeT]
    test_dat=data.data[sizeT:]
    train_targ=data.target[:sizeT]
    test_targ=data.target[sizeT:]
    return train_dat,test_dat,train_targ,test_targ

#function: conduct_PCA
#takes a nested list of data and a number of components to keep
#then returns the PCA object from sklearn's PCA
#list,integer--> PCA_object
def conduct_PCA(data,n_components):
    '''takes a nested list of data and the number of components to use for the PCA.
        Then returns a PCA object from sklearn.
    '''
    pca=PCA(n_components=n_components)
    transformed_data=pca.fit(data.data).transform(data.data)
    return transformed_data
#https://scikit-learn.org/stable/auto_examples/decomposition/plot_pca_vs_lda.html#sphx-glr-auto-examples-decomposition-plot-pca-vs-lda-py


#function: fit_GLM
#takes a nested list of data and the columns to use as factors.
#The columns should be represented by a list of integers. Returns a GLM object
#List,list--> GLM_object 
def fit_GLM(data_GLM,components,test_size):
    '''takes a nested list of data and the columns to use as factors.
        The columns should be represented by a list of integers. Returns a GLM object.
        Also prints the GLM parameters and performance score. 
    '''
    GLM_dat=create_test_set(data_GLM,test_size)
    lm=linear_model.LinearRegression()
    if len(components)==1:
        train_d=GLM_dat[0][:,np.newaxis,components]
        train_t=GLM_dat[2][:,np.newaxis,components]
        test_d=GLM_dat[1][:,np.newaxis,components]
        test_t=GLM_dat[3][:,np.newaxis,components]
    elif components==None:
        train_d=GLM_dat[0][:]
        train_t=GLM_dat[2][:]
        test_d=GLM_dat[1][:]
        test_t=GLM_dat[3][:]
    else:
        train_d=GLM_dat[0][:,components]
        train_t=GLM_dat[2][:,components]
        test_d=GLM_dat[1][:,components]
        test_t=GLM_dat[3][:,components]
    lm.fit(train_d,train_t)
    preicted_target=lm.predict(test_d)
    return predicted_target,lm
#https://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html#sphx-glr-auto-examples-linear-model-plot-ols-py

#procedure: compare_GLMs
#takes as input a nested list of data and a list of the total 
#columns to include in the compared model. Prints what combination is optimal.
#list,list-->N/A
def SVC_Model_selection(data,c_value):
    '''Takes as an input a nested list of data and a list of factors to use. 
        Recursive feature elimination
        will then be used to compare different feature combinations. The best 
        feature combination will
        then be printed for the user to take note of. 
    '''
    lsvc=LinearSVC(C=c_value,penalty="L1",dual=False).fit(data.data)
    model=SelectFromModel(lsvc,prefit=True)
    transformed_data=model.transform(data.data)
    return transformed_data 
#https://scikit-learn.org/stable/modules/feature_selection.html#l1-feature-selection

   

#The Scikit-learn documentation (https://scikit-learn.org/stable/modules/decomposition.html#pca) 
#was used to inform the creation of the stubs and the general modules to import.
#The creation of the stubs was informed by seeing what info was required and 
#made avaliable by the various scikit functions (e.g. PCA and GLM). 
#Additionally, the plots and methods for comparing various GLM's was influenced 
#by the information within the Scikit documentation. 
























