#!/usr/bin/env python
# coding: utf-8

# In[60]:


# Modules
import os
import csv


# In[61]:


# Set path for file
csvpath = os.path.join("..", "Resources", "election_data.csv")
# Set variable to check if we found the item
found = False


# In[62]:


# Declare and initialize the variables
all_voteCount = 0
winner = ""
winner_voteCount = 0

# Creating an empty dictionary to store the data
# In this case, the key will be the candidate name, and the value corresponding to it will be the number of votes that person gets
# "Charles": 1000 for example
candidate_pool = {}
percent_pool = {}
vote_counter = 0


# In[63]:


# Open the CSV using module
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header for the first row
    header = next(csvreader)  
    
    # Loop through the file, Read each row of data after the header
    for row in csvreader:
         # Each row from the file is returned as a list of string, 3rd column will give you candidate names
        candidate_name = row[2]
        
        # Check if the candidate name already exists in the dict, if not then we add new pair to the dict (plus 1 to the value, increment each iteration)
        if candidate_name not in candidate_pool:
            candidate_pool[candidate_name] = 0  
        # Increment the vote count for the candidate
        candidate_pool[candidate_name] += 1
        
   #----------This is the end of For loop---------------

#Debugging with print function, to see what is inside the dictionary
print(candidate_pool)


# In[64]:


# Calculate total votes of all the candidates
for voteCount in candidate_pool.values():
    all_voteCount += voteCount

# Using .item() to get access both key and its value inside the dict
for candidate_name, num_vote in candidate_pool.items():
    
    # Calculate the percentage by dividing the each candidate's votes by the total counts and times 100
    percent = (num_vote/all_voteCount) * 100
    # Add new key-value pair to the new dict
    percent_pool[candidate_name] = percent
    
    # Find the winner by comparing the current voteCount to previous voteCount
    # Keep updating if the current voteCount is bigger than the previous one
    # If it's less than the previous one, we can just skip until we find a new larger value
    if num_vote > winner_voteCount:
        # Update the winner votes
        winner_voteCount = num_vote
        # Update the winner
        winner = candidate_name

# Check the percent_pool dict
print(percent_pool)


# In[72]:


csv_lines_txt =[]
# Printing out the results
output1 = (
    f"Election Results\n"
    f"---------------------------\n"
    f"Total Votes: {all_voteCount}\n"
    f"---------------------------\n"
)
print(output1)
csv_lines_txt.append(output1)

for candidate_name, percent in percent_pool.items():
        print(f"{candidate_name}: {percent:.3f}% ({candidate_pool[candidate_name]})")
        csv_lines_txt.append(f"{candidate_name}: {percent:.3f}% ({candidate_pool[candidate_name]})")
    
output3 = (    
    f"\n---------------------------\n"
    f"Winner: {winner}"
    f"\n---------------------------\n"
)
print(output3)
csv_lines_txt.append(output3)


# In[73]:


# Export the result to a text file
output_file = 'election_analysis.txt'
with open(output_file, 'w') as text_file:
    for line in csv_lines_txt:
        text_file.write(line + "\n")

