# Automated-Birthday-Wishes-on-Facebook
Automatically posts birthday wishes on friend's FB wall. Creates a cronjob to post wishes everyday. Uses selenium for accessing Facebook. **For using this script disable 2 factor authentication on facebook**. 
# Requirements
* selenium webdriver
# Instructions
* Run the bash script generate.sh using 
```
bash generate.sh
```
* Enter username, password and message for posting
```
Enter email/phone = harsh.sinha@students.iiit.ac.in
Enter password = **********
Enter message to post = Happy Birthday!!!
```
* Enter time for posting the message
```
Enter time in format Hour:Min = 13:00
```
Note - Time should be in 24 hour format. Hour - 0 to 23, Min - 0 to 59.
# TODO
* Handling 2 factor authentication
* Custom birthday message containing name of friend.
