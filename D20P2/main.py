# Initialize dictionary
test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
  
# printing original dictionary
print("The original dictionary : " +  str(test_dict))
  
# Initialize value 
K = 2

# Using loop
# Selective key value in dictionary
res = 0
for key in test_dict:
    if test_dick[key] == K:
        res = res + 1

# printing result
print("frequency of K is : " + str (res))
