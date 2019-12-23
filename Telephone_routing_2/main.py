""" Finding Cheapset Operator """



path="D:\Task_Approach_2\input.txt"

price_list=[]

operator_names=[]

MAX_PRICE=99


def add_operator_name(name):
    
    name=name.replace(":\n","")
    
    operator_names.append(name)


def file_lengthy(path):

        with open(path) as f:

                for i, l in enumerate(f):

                        pass

        return i + 1


def initialization():
      
    from nltk.tokenize import word_tokenize
    
    file_length = file_lengthy(path)

    file = open(path)

    prefix=[]

    price=[]
    
    text=file.readline()

    add_operator_name(text)
    

    for i in range(file_length-1):
    
        text=file.readline()

        if(text[0]=='O' or text[0]=='o'):

            price_list.append(list([prefix,price]))

            add_operator_name(text)

            prefix=[]

            price=[]
            
        else:

            tokens=word_tokenize(text)

            prefix.append(tokens[0])

            price.append(float(tokens[1]))
    
    price_list.append(list([prefix,price]))
    

def find_cheapest_operator(phone_number):
    
    import re

    phone_number_prices=[]
    
    for i in range(len(price_list)):

        my_price=99

        max_lenght=0

        for j in range(len(price_list[i][0])):

            pattern="^"+price_list[i][0][j]+"\d*"

            if(re.findall(pattern,phone_number) and len(price_list[i][0][j])>=max_lenght):

                max_lenght=len(price_list[i][0][j])

                my_price=price_list[i][1][j]

        phone_number_prices.append(my_price)
        
    min_price=min(phone_number_prices)

    if(min_price<MAX_PRICE):

        return (operator_names[phone_number_prices.index(min_price)])

    else:

        return ("Operator not found with Prefix given")


initialization()

phone_number=input("\nPlease Enter your Phone Number :\n -1 to exit\n")

while(phone_number!="-1"):

    print(find_cheapest_operator(phone_number))

    phone_number=input("\nPlease Enter your Phone Number :\n -1 to exit\n ")