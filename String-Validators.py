'''
You are given a string S .
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
'''

if __name__ == '__main__':
    s = input()
    
    for i in s:
        if i.isalnum()==True:
            print("True")
            if i.isalpha()==True:
                print("True")
                if i.isdigit()==True:
                    print("True")
                    if i.islower()==True:
                        print("True")
                        if i.isupper()==True:
                            print("True")
                        else:
                            print("False")
            
