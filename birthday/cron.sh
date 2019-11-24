read -p "Enter time in format Hour:Min = " time
IFS=':' read -ra time_array <<< "$time"
min=${time_array[1]} 
hour=${time_array[0]}
set -f
var=$min" "$hour" * * * "
cronjob+="python3 "`pwd`
crontab -l > mycron
echo $cronjob >> mycron
crontab mycron
rm mycron