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


# PyRoll script
