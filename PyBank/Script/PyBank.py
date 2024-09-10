#!/usr/bin/env python
# coding: utf-8

# In[75]:


# Modules
import os
import csv


# In[76]:


# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")
# Set variable to check if we found the item
found = False


# In[77]:


# Declare and initialize the variables
# Created 2 lists to hold the data of the 2 columns in cvs file
date = []
net_value =[]

# Varibles for calculation and analysis
total_months = 0
net_total_amount = 0
prev_value = None
greatest_increase_net = 0
greatest_increase_date = ""
greatest_decrease_net = 0
greatest_decrease_date = ""


# In[78]:


# Open the CSV using module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header for the first row
    header = next(csvreader)  
    
    # Loop through the file, Read each row of data after the header
    for row in csvreader:
        # Each row from the file is returned as a list of string
        # Therefore, row[0] is the 1st element and row[1] will be the 2nd element in the list
        date_value = row[0]
        # Convert the value to integer for the 2nd column
        pl_value = int(row[1])

        # Total number of months, increment the counter by one every time we loop
        total_months = total_months + 1
        # Net total amount of Profit/losses, keep adding the value to the declared variable
        net_total_amount = net_total_amount + pl_value

        # Calculate changes in profit/loss
        if prev_value is not None:
            diff = pl_value - prev_value
            date.append(date_value)
            net_value.append(diff)
                        
            # Find the greatest increase and update the greatest increase every iteration
            if diff > greatest_increase_net:
                greatest_increase_net = diff
                greatest_increase_date = date_value
                
            # Find the greatest decrease and update the greatest decrease every iteration
            if diff < greatest_decrease_net:
                greatest_decrease_net = diff
                greatest_decrease_date = date_value
                
        # Update the old profit/losses for the next iteration
        prev_value = pl_value

    # ----This is the end of For loop

# Calculate average change
avg_change = sum(net_value) / len(net_value)


# In[79]:


# Printing out the results
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${net_total_amount}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_net})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_net})\n"
)


# In[80]:


# Print the analysis to the terminal
print(output)


# In[81]:


# Export the result to a text file
with open('financial_analysis.txt', 'w') as text_file:
    text_file.write(output)


# In[ ]:




