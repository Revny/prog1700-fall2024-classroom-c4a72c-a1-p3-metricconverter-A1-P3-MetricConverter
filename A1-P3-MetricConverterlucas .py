#Program 3 – Imperial to Metric Conversion
#Write a console program that converts a weight given in tons (imperial), stones, pounds, and ounces 
# to the metric equivalent in metric tons, kilograms, and grams.

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
   #create the inputs 
    tons=float(input("put in the weight using tons"))
    stone=float(input("put in the weight using stones"))
    pounds=float(input("put in the weight using pounds"))
    ounces=float(input("put in the weight using ounces"))
    #the formulas for the program
    totalounces = 35840 * tons + 224 * stone + 16 * pounds + ounces
    totalkilos = totalounces / 35.274
    metrictons=int(totalkilos/1000)
    #print all 3 and add in text telling the user the order of weights
    print("here is your total weight in metrictons,totalkilos,totalounces", metrictons,totalkilos,totalounces)






    # YOUR CODE ENDS HERE

main()