#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo $DIR
chmod +x currency.py

write out current crontab
crontab -l > mycron
#echo new cron into cron file
echo "0 10 * * * python $DIR/currency.py" >> mycron
#install new cron file
crontab mycron
rm mycron
