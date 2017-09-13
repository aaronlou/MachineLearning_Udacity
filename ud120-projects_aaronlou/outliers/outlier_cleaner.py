#!/usr/bin/python
#coding:utf-8


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """


    cleaned_data = []

    ### your code goes here
    error = abs(predictions-net_worths)
    top10percent_value = sorted(error,reverse=True)[int(0.1*len(predictions))]

    for i in zip(ages,net_worths,predictions):
        error = abs(predictions-net_worths)
        if error >= top10percent_value:
            pass
        else:
            cleaned_data.append(zip(i[0],i[1],error))
    
    return cleaned_data

