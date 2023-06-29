while True:
    print(f"Choose an option below"
        "\n1-Show Dataset"
        "\n2-Question about the Database"                  #Gives the user 3 options to choose from
        "\n3-Leave")
    user_input= input("\n:")
    
    if user_input=='3': 
        print(f"\nGoodbye")   #tell the user that they have exited
        break
    elif user_input=='1':
        import pandas as pd
        data = pd.read_csv("billionaires.csv")        #loads the data from the CSV
        print(data)

        break
    elif user_input=='2':
        print(f"\nChoose any of the question below:"
              
              "\n1-Whats the chances of a billionaires' wealth being inherited?"
              "\n2-What are the different genders of the billionaires?"                                 #Gives the user 3 options to choose from about the insights of the dataset
              "\n3-Whats is the different ages compared to the billionaires industry")
        user_inputa= input("\n:")
    while True:
         import pandas as pd 
         import matplotlib.pyplot as plt
         df=pd.read_csv('billionaires.csv')  
         df

         subSet = df[['Rank','Name', 'Demographics Gender', 'Year', 'Company Name', 'Company Sector', 'Wealth How Inherited' ]]      #loads the data fromt he dataset

         subSet
         if user_inputa=='1':
            print
            Wealth_How_Inherited=subSet['Wealth How Inherited'].value_counts()
            plt.figure(figsize=(6,6))
            plt.pie(Wealth_How_Inherited,labels=Wealth_How_Inherited.index,autopct='%1.1f%%')              #Pie chart for how the wealth was inherited
            plt.title('Wealth How Inherited')                                                    
            plt.axis('on')
            plt.show()
            break
         
         if user_inputa=='2':
            print
            Gender_counts=subSet['Demographics Gender'].value_counts()
            plt.figure(figsize=(6,6))
            plt.pie(Gender_counts,labels=Gender_counts.index,autopct='%1.1f%%')                 #Pie chart for the billioanires' gender
            plt.title('Gender Ratio')  
            plt.axis('on')
            plt.show()
            break
         
         if user_inputa=='3':
             print
             Wealth_How_Industry = df['Wealth How Industry'].unique()
             age_by_wealth = df.groupby('Wealth How Industry')['Demographics Age'].mean().dropna()        #bar graph for the age distribution by Wealth How Industry
             plt.bar(age_by_wealth.index, age_by_wealth, color='green')
             plt.xlabel('Wealth How Industry')
             plt.ylabel('Age')                                                              
             plt.title('Age Distribution by Wealth How Industry')
             plt.xticks(rotation=45)
             plt.show()
         break
            
