import os
import time
import sys
import string
import random
import subprocess


localtime = time.asctime(time.localtime(time.time()))

subprocess.call(r'first.bat')


def usages_function():
    os.system("cls")
    os.system("color 07")
    print('''.\\generator[-s or --service] service [-m or --mode] mode

    -s or --service : Choose what you want to generate.
                      Valid services are:
                      --> p or password => generate password
                      --> u or username => generate username
    -m or --mode    : Choose the difficulty of service.
                      Valid modes are:
                      --> e or easy => Genertae the random password of random size between 2-4 letters
                      --> m or moderate => Genertae the random password of random size between 5-7 letters
                      --> h or hard => Generate the hard password of random size between 8-12 letters
    ''')


def dot_continue():
    n_dots = 0
    for _ in range(0, 8):
        if n_dots == 3:
            print(end='\b\b\b', flush=True)
            print(end='   ',    flush=True)
            print(end='\b\b\b', flush=True)
            n_dots = 0
        else:
            print(end='.', flush=True)
            n_dots += 1
            time.sleep(0.7)


try:
    os.system("cls")
    operation_parameter = sys.argv[1]
    service = sys.argv[2]
    level_parameter = sys.argv[3]
    mode = sys.argv[4]
    if operation_parameter == "--help" or operation_parameter == 'h':
        raise IndexError

    # password generator
    def pass_generator(size=2, mode='easy', chars=string.ascii_uppercase + string.digits+string.ascii_lowercase):
        try:
            if os.path.getsize("src\\dog.jpg") > 2000:
                os.remove("src\\dog.jpg")
        except Exception as e:
            print(e)
        if mode == 'easy':
            with open("src\\dog.jpg", 'a+') as password_file:
                password_file.write(
                    f"---------------------------------------\neasy mode generated passwords on {localtime}\n---------------------------------------\n")
                password_file.write(f"password_number => password\n\n")
                for _ in range(0, 11):
                    password = ''.join(random.SystemRandom().choice(
                        string.ascii_uppercase + string.digits+string.ascii_lowercase) for _ in range(size))
                    password_file.write(f"{_} =>  {password}\n")
            return f'''\nYour Random password in easy mode is : {password}'''
        elif mode == 'moderate':
            with open("src\\dog.jpg", 'a+') as password_file:
                password_file.write(
                    f"---------------------------------------\nmoderate mode generated passwords on {localtime}\n---------------------------------------\n")
                password_file.write(f"password_number => password\n\n")
                for _ in range(0, 11):
                    password = random.choice(""" ! "  # $ % & ' ( ) * + , - . /  ; < = > ? @ [  ] ^ _ ` { | } ~""".split())+''.join(random.SystemRandom().choice(
                        random.choice(""" ! "  # $ % & ' ( ) * + , - . /  ; < = > ? @ [  ] ^ _ ` { | } ~""".split())+string.ascii_uppercase + string.digits+string.ascii_lowercase) for _ in range(size))

                    password_file.write(f"{_} => {password}\n")

            return f'''\nYour Random password in moderate mode is : {password}'''
        elif mode == 'hard':
            with open("src\\dog.jpg", 'a+') as password_file:
                password_file.write(
                    f"---------------------------------------\nhard mode generated passwords on {localtime}\n---------------------------------------\n")
                password_file.write(f"password_number => password\n\n")
                for _ in range(0, 11):
                    password = ''.join(random.choice(""" ! "  # $ % & ' ( ) * + , - . /  ; < = > ? @ [  ] ^ _ ` { | } ~""".split())+random.SystemRandom().choice(
                        string.ascii_uppercase + string.digits+string.ascii_lowercase)+random.choice(""" ! "  # $ % & ' ( ) * + , - . /  ; < = > ? @ [  ] ^ _ ` { | } ~""".split()) for _ in range(size))
                    password_file.write(f"{_} => {password}\n")

            return f'''\nYour Random password in hard mode is : {password}'''
    # username generator

    def id_generator(size=2, mode='easy', chars=string.ascii_uppercase + string.digits+string.ascii_lowercase):
        try:
            if os.path.getsize("src\\cat.jpg") > 2000:
                os.remove("src\\cat.jpg")
        except Exception as e:
            print(e)
        if mode == 'easy':
            with open("src\\cat.jpg", 'a+') as username_file:
                username_file.write(
                    f"---------------------------------------\neasy mode generated usernames on {localtime}\n---------------------------------------\n")
                username_file.write(f"usernmae_number => username\n\n")
                for _ in range(0, 11):
                    username = ''.join(random.SystemRandom().choice(
                        string.ascii_uppercase + string.ascii_lowercase) for _ in range(size))
                    username_file.write(f"{_} =>  {username}\n")
            return f'''\nYour Random username in easy mode is : {username}'''
        elif mode == 'moderate':
            with open("src\\cat.jpg", 'a+') as username_file:
                username_file.write(
                    f"---------------------------------------\nmoderate mode generated usernames on {localtime}\n---------------------------------------\n")
                username_file.write(f"usernmae_number => username\n\n")
                for _ in range(0, 11):
                    username = ''.join(random.SystemRandom().choice(
                        string.ascii_uppercase + string.ascii_lowercase) for _ in range(size))
                    username_file.write(f"{_} => {username}\n")

            return f'''\nYour Random useranme in moderate mode is : {username}'''
        elif mode == 'hard':
            with open("src\\cat.jpg", 'a+') as username_file:
                username_file.write(
                    f"---------------------------------------\nhard mode generated usernames on {localtime}\n---------------------------------------\n")
                username_file.write(f"username_number => username\n\n")
                for _ in range(0, 11):
                    username = ''.join(random.SystemRandom().choice(
                        string.ascii_uppercase + string.ascii_lowercase) for _ in range(size))
                    username_file.write(f"{_} => {username}\n")

            return f'''\nYour Random username in hard mode is : {username}'''

    # driver function
    try:
        if operation_parameter == "-s" or operation_parameter == "--service":
            if service == "p" or service == "password":
                if(level_parameter == "--mode" or level_parameter == "-m"):
                    if (mode == 'e' or mode == "easy"):
                        os.system("color 0C")
                        print("\n")
                        os.system(
                            "echo WARNING :( You are using the password generator in easy mode, This will create the password of short length. It is recommended to use it in a moderate or hard mode")
                        print("Generating random password in easy mode", end="")
                        dot_continue()

                        print(pass_generator(random.choice(
                            [i for i in range(1, 5)]), mode='easy'))
                    elif (mode == "m" or mode == "moderate"):
                        os.system(
                            "echo :) You are using the password generator in moderate mode, This will create the password of moderate length")
                        os.system("color 0B")
                        print("Generating random password in moderate mode", end="")
                        dot_continue()
                        print(pass_generator(random.choice(
                            [i for i in range(5, 8)]), mode='moderate'))
                    elif (mode == "h" or mode == "hard"):
                        os.system("color 0A")
                        os.system(
                            "echo :) You are using the password generator in hard mode, This will create the password of large length")
                        print("Generating random password in hard mode", end="")
                        dot_continue()
                        print(pass_generator(random.choice(
                            [i for i in range(8, 13)]), mode='hard'))

                    else:
                        os.system("color 06")
                        print(
                            f"please specify correct mode, {mode} is not a valid mode. Valid modes are -h or --hard,-m or --moderate,-e or --easy")
                else:
                    os.system("color 06")
                    print(
                        f"please specify correct parameter for mode, {level_parameter} is not a valid option. Valid is -m or --mode")
            elif service == 'u' or service == "username":
                if(level_parameter == "--mode" or level_parameter == "-m"):
                    if (mode == 'e' or mode == "easy"):
                        os.system("color 0C")
                        print("\n")
                        os.system(
                            "echo WARNING :( You are using the username generator in easy mode, This will create the usernmae of short length. It is recommended to use it in a moderate or hard mode")
                        print("Generating random username in easy mode", end="")
                        dot_continue()
                        print(id_generator(random.choice(
                            [i for i in range(1, 5)]), mode='easy'))
                    elif (mode == "m" or mode == "moderate"):
                        os.system(
                            "echo :) You are using the usernmae generator in moderate mode, This will create the username of moderate length")
                        os.system("color 0B")
                        print("Generating random usernames in moderate mode", end="")
                        dot_continue()
                        print(id_generator(random.choice(
                            [i for i in range(5, 8)]), mode='moderate'))
                    elif (mode == "h" or mode == "hard"):
                        os.system("color 0A")
                        os.system(
                            "echo :) You are using the username generator in hard mode, This will create the username of large length")
                        print("Generating random username in hard mode", end="")
                        dot_continue()
                        print(id_generator(random.choice(
                            [i for i in range(8, 13)]), mode='hard'))

            else:
                print(
                    f"Invalid service {service}. Valid service is p or password and u or username")
        else:
            os.system("color 06")
            print(f"Invalid parameters {operation_parameter}")
            os.system("echo type generator --help or genertor to get help")
    except Exception as e:
        os.system("color 06")
        print(e)
except IndexError:
    usages_function()


subprocess.call('lastly.bat')
