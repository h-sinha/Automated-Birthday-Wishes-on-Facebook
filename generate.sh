python3 get_cred.py
read -p "Enter time in format Hour:Min = " time
IFS=':' read -ra time_array <<< "$time"
min=${time_array[1]} 
hour=${time_array[0]}
set -f
cronjob=$min" "$hour" * * * "
cronjob+="export DISPLAY=:0.0 && cd "
cronjob+=`pwd`
cronjob+=" && "
cronjob+=`which python3`
cronjob+=" main.py"
crontab -l > mycron
echo $cronjob >> mycron
crontab mycron
rm mycron
echo "Done"