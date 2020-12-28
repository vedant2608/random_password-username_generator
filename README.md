## <span style="background-color:#97CBEE">Random password and username generator using python 😄😄</span>

##### Please read the `README.md ` file carefully 
###### I am working on how can I make this code run on linux too. I am a beginner but surely I will write the script for that too
----
### <span style="background-color:#8FBC8F">General Information 😃</span>
- ##### Clone this repository to your local system using command prompt in administrative mode
- ##### Run this command is cmd to make a symbolic link to todo.bat `mklink generator generator.bat` 
- ##### If the link is created succesfully script can be run using .\generator
- ##### This script generate random passwords and random usernames :)
- ##### Two files known as `dog.jpg` and `cat.jpg` are important please do not delete those files
- ##### If you remove those files you will an error. I am working on how to deal with that error. Removal does not stop the execution #&7892 . It still works and generate passwords and usernames
- ##### If you run as  `path\to\script>.\generator.bat` first time it will make the files hidden as this is intended. Also it will make the two images `cat.jpg` & `dog.jpg` read-only. It's kind of small security I tried to add from my side😋😅.Those two images will not be hidden
- ##### To see the hidden files type in cmd
  #### ````path\to\script> attrib -h *````
   
   ###### Note:it is not recommended to show the files
- ##### Those two images are important cause these will store your passwords. The scrpits will store 10 passwords or usernames to those images. Passwords are stored in `dog.jpg` and `cat.jpg` contains your username. 
- ##### Your default image viewer will not be able to open this files. Now you know how to open files in another way,don't you?😉😉
- ##### Your command promt will only show you the one password or username ,but it actually generate 10 passwords or usernames at a time
- ##### To see those passwords open `dog.jpg` and for usernames open `cat.jpg`
- ##### These files are created in a way such that if the length of both files are more than 2kb they will be deleted and new files will be created. So if you get an error saying file not found (:(),it's okay  scripts still works well :)
----
## <span style="background-color:#F37615">How to use this script</span>😄
 -  ##### Clone this repository from the github to your local machine
 - ##### Change your directory to where you cloned the repository 
 - ##### Type the following in terminal
   ```batch
   path\to\script>.\generator
   ```
   ##### This will gives you the output as 
   ```batch
   .\generator[-s or --service] service [-m or --mode] mode

    -s or --service : Choose what you want to generate.
                      Valid services are:
                      --> p or password => generate password
                      --> u or username => generate username
    -m or --mode    : Choose the difficulty of service.
                      Valid modes are:
                      --> e or easy => Generate the random password of random size between 1-4 letters
                      --> m or moderate => Generate the random password of random size between 5-7 letters
                      --> h or hard => Generate the hard password of random size between 8-12 letters
   ```
   ###### This is help for script
   ---
## <span style="background-color:#F37615">Description of help</span>😄
##### The parameter -s or --service are necessary to define the services you want to use. The valid services are 
- u or username to generate username
- p or password to generate passwords
##### The parameter -m or --mode is necessary to define the difficulty level of generation of usernames and passwords
- e or easy to generate the passwords of easy level. The size of passwords and username generated is betwwen 1 to 4
- m or moderate to generate the passwords of moderate level. The size of passwords and username generated is betwwen 5 to 7
-h or hard to generate the passwords of difficult level> The size of passwords and usernames generated between 8-12 letters
---
 
 <iframe src="https://www.youtube.com/embed/r9i2cZ2rYtc" frameborder="0" allowfullscreen="true"> </iframe>


# <span style="background-color:lightblue">Thank you for reading upto this part. I hope you liked the project. Any suggestions are always welcome😊😊</span>

 
