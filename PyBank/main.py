import pandas as pd
from pathlib import Path 
csv_file=Path('budget_data.csv')
data=pd.read_csv(csv_file)
data.head()

##The total number of months included in the dataset.
number_month=data.count()
number_month=number_month.Date
print(number_month)

##The net total amount of Profit/Losses over the entire period.
total=data.sum()
total=total['Profit/Losses']
print(total)

##The average of the changes in Profit/Losses over the entire period.
data_PnL=data[['Profit/Losses']]
data_PnL.head()
data_diff=data_PnL.diff(periods=1, axis=0)
avg_change=data_diff.mean()
avg_change=avg_change['Profit/Losses']
print(avg_change)

##The greatest increase in profits (date and amount) over the entire period.
max_increase=data_diff.max()
max_increase=max_increase['Profit/Losses']
print(max_increase)

location=data_diff.loc[data_diff['Profit/Losses']==max_increase]
value_max=location
value_max

date_max=data.iloc[25,:]
date_max.head()
date_max=date_max.Date
date_max

##The greatest decrease in losses (date and amount) over the entire period.
max_decrease=data_diff.min()
max_decrease=max_decrease['Profit/Losses']
print(max_decrease)

location=data_diff.loc[data_diff['Profit/Losses']==max_decrease]
value_min=location
value_min

date_min=data.iloc[44,:]
date_min.head()
date_min=date_min.Date
date_min

f = open('output_hw_2_AO.txt','w')
f.write("Financial Analysis\n")
f.write("---------------------------------\n")
f.write("Total Months: ")    
f.write('{}'.format(number_month))
f.write("\nTotal: $")    
f.write('{}'.format(total))
f.write("\nAverage  Change: $")    
f.write('{}'.format(avg_change))
f.write("\nGreatest Increase in Profits: ")   
f.write('{}'.format(date_max))
f.write(" ($")   
f.write('{}'.format(max_increase))
f.write(")")  
f.write("\nGreatest Decrease in Profits: ")   
f.write('{}'.format(date_min))
f.write(" ($")  
f.write('{}'.format(max_decrease))
f.write(")")  
f.close()

f = open('output_hw_2_AO.txt', 'r')
FinalcialAnalysis = f.read()
print (FinalcialAnalysis)
f.close()