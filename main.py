
response = {}
response['pennies'] = 0 # Running counts of each coin
response['nickels'] = 0
response['dimes'] = 0
response['quarters'] = 0
response['total'] = 0 # Running total of monetary amount

with open('Myfile.txt', 'r') as results_file:
    response_lines = results_file.readlines()
    for line in response_lines:
        line = line.strip()
        item, percent = line.split(': ')
        response[item] = percent
        if "penny" in line:
            response['pennies']+=1
        elif "nickel" in line:
            response['nickels']+=1
        elif "dime" in line:
            response['dimes']+=1
        elif "quarter" in line:
            response['quarters']+=1
print("You have %d pennies" % response['pennies'], "%d dimes" % response['dimes'] , "%d nickels" % response['nickels'] ,"and %d quarters" % response['quarters'])
p = 0.01 * response['pennies']
n = 0.05 * response['nickels']
d = 0.10 * response['dimes']
q = 0.25 * response['quarters']
response['total'] = p+n+d+q
print("Your total is $%.2f" % response['total'])
