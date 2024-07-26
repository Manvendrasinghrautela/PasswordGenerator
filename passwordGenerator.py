import random
import array


max_length = 12

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']   
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',  
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 
                     'z'] 
  
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',  
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                     'Z'] 
  
symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',  
           '*', '(', ')', '<'] 

combined_list = digits + lower_case + upper_case + symbols

rand_digits = random.choice(digits)
rand_lower = random.choice(lower_case)
rand_upper = random.choice(upper_case)
rand_symbols = random.choice(symbols)

temp_pass = rand_digits + rand_lower + rand_upper + rand_symbols


for x in range(max_length - 4):
    temp_pass += random.choice(combined_list)

    temp_pass_list = array.array("u", temp_pass)
    random.shuffle(temp_pass_list)

password = ""

for x in temp_pass_list:
    password = password + x

print(password)
