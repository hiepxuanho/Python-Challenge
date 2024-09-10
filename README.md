# Python-Challenge
Creating Python scripts to analyze the financial records of a company.
There are two folders contains 2 Python scripts, 2 csv files for analyzing, and 2 Analysis txt files for results checking.

# PyBank script
Creating a csv file path to read was fairly simple, and creating empty lists to store all the values of the rows is the best choice. We can simply use "Append" to collect the datas and use them however we want as calculating the sum, average, etc. 

At first, I ran into a problem while calculating the changes in profit/losses. I already knew that I had to create a list to store all the values of the changes. 
The diff will be equal to changes[i] - changes[i-1] (or new profit/loss minus old profit/loss), then I will find the avergage of all the changes by taking the sum / length of the list. This will give us the needed avagerage result. However, it kept giving me incorrect values instead of the right answer given in the screenshot as the final result. 

I fgured out that by initializing the changes[i-1], in this case is considered as previous profit/loss, to 0. Because when we first initialize the loop, there is no precious or old profit/loss value. We can't calculate the change value for the first row of the data. By giving the old profit/loss to 0 as first, we will calculate the change incorrectly with the equation new profit/loss - old profit/loss. Therefore, we need to make no calculation for the first row, and skip the calculation of the change for the first iteration of the loop.

I thought about initializing the old profit/loss to empty but it also seemed to be incorret asl well, and I had to look up on Chat GPT to find a way to skip the first calculation. 

/-------------------Chat GPT code------------------------------------/
if previous_profit_loss is not None:
    change = profit_loss - previous_profit_loss
/--------------------------------------------------------------------/

It seems like by declearing the old value to be "not none" and with an if statement, it will solve the issue. All we have to do next is updating the a new value for the old profit/loss at the end of the first iteration of the loop.

/----------------Update the previous profit/loss value---------------/
        previous_profit_loss = profit_loss
/--------------------------------------------------------------------/

To find the greatest increase/decrease with date and amount, we only have to compare the diff value to the greatest_increase_net value. 
If diff > greatest_increase_net, then we update the new greatest_increase_net with the diff value and store the date 
We will do the same steps for the greastest decrease with the comparision as If diff < greatest_decrease_net

To export the result to a text file we can follow this step. The professor already showed us how to do it in class through the activities.
/--------------------------------------------------------------------/
with open('financial_analysis.txt', 'w') as text_file:
    text_file.write(output)
/--------------------------------------------------------------------/

Finally, I got all the correct results on the terminal as well as the analysis text file. 

# PyRoll script

Creating an empty dictionary to store the data. In this case, the key will be the candidate name, and the value corresponding to it will be the number of votes that person gets
"Charles": 1000 for example. The key (Charles) will map to the value (1000)
In addition, when we iterate over the dictionary, we can access both the keys and values using .tem(). Or we can access a value by using its key such as candidate_pool["Charles"]
Adding the a new value to the dictionary will be much simplier with better time complexity O(1). Because we can directly acess the key and its value and with efficient lookups and updates.
Ex: candidate_pool["Adam"] = 99 to update/add a pair.

/-------------------------Chat GPT code-------------------------------/
        if candidate_name is not in candidate_pool:
            candidate_pool[candidate_name] = 0
        candidate_pool[candidate_name] +=1
/--------------------------------------------------------------------/

I need to look up on Chat GPT to find how to add/update a new pair to a dictionary. At first, I tried to add the key and value in the dict at the same time. For example with my code:
/------------------------------My code-------------------------------/
vote_counter = 0
if candidate_name is not in candidate_pool:
    vote_counter += 1
    candidate_pool[candidate_name] = vote_counter  
/--------------------------------------------------------------------/
However, this didn't seem to be the right way since we can directly update/reset the count inside the dictionary. No counter needed
Before I resetted the counter each time there's a new key, and then update the key with the new counter value such as:
candidate_pool[candidate_name] = vote_counter
/--------------------------------------------------------------------/

In conclusion, when we see a new key, then we can just update the value of that key to 1:
candidate_pool[candidate_name] = 1
then in the next iteration, we can increment the value of that key directly inside the dictionary:
candidate_pool[candidate_name] += 1
/--------------------------------------------------------------------/

Another note when I was looking up on Chat GPT to learn more about dictionary. If you need to access both key and value, you have to use .item()
Because without .item(), you can only either access to the key, or value. For example:
/--------------------------------------------------------------------/
for candidate_name in candidate_pool:
/--------------------------------------------------------------------/
You can only access the key of the dict. And with the code below, you can access both key and value for calculation, printing.
/--------------------------------------------------------------------/
for candidate, votes in candidate_votes.items():
/--------------------------------------------------------------------/

Printing to terminal and exporting to txt file was harder than I thought. One of the reason was that I didn't have a simple concise (output). Therefore, I couldn't just do:
/--------------------------------------------------------------------/
with open('election_analysis.txt', 'w') as text_file:
    text_file.write(output)
/--------------------------------------------------------------------/
I have two dictionaries, one of them has ["candidate_name" : voteCount] and the other dict has ["candidate_name" : percent].
In order to print to the terminal, I have to split the result into 3 parts: output1, printing through loop with dict, output3.
Then I have to combine all 3 parts altogether by append to a new csv_lines_txt list.
From here I can export the result to a text file by using the module and For-loop to display line by line in the csv_lines_txt list.
/--------------------------------------------------------------------/
output_file = 'election_analysis.txt'
with open(output_file, 'w') as text_file:
    for line in csv_lines_txt:
        text_file.write(line + "\n")
/--------------------------------------------------------------------/

Finally, I got all the correct results on the terminal as well as the analysis text file. 
Throughout this project, I believe I got a pretty good understanding of a dictionary and how to access its key and value. How to print all the datas to the terminal with either a string, or a list. How to export the result to a text file with different methods (basic write to file by using a string, line by line through looping)
