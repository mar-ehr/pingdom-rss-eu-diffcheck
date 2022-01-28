# pingdom-rss-eu-diffcheck


Solarwinds Pingdom is a Uptime Probe Service, that you can use to monitor your webservers or webapplications uptimes. 

They either use ICMP or CURL Requests to try and reach your host. If their requests result in too many negatives from more than one location, you will get an alert that your application/service is DOWN. 
This can be used to create availability-reports for web-applications, or to simply get notified, when your application can't be reached from the internet. 


Solarwinds Pingdom uses a wide variety of servers all around the globe for their uptime probes. These servers may change sometimes (some might be dismissed, new ones might be added etc.). 
Therefore, if you want to use pingdom with restricted internet access, you have to manually open up ports in your firewall for the certain ip-adresses of the probe servers in order to use this uptime monitoring solution.
If a new pingdom server is added without you knowing and adding it to your firewall, you could start getting false DOWN-notifications. If a pingdom server is dismissed, there still will be a rule in your firewall that opens the webservers ports for the ip-adress of the dismissed webserver. 

Sadly, solarwinds does not "notify" users when they are either adding or dismissing any of their servers. The only information about their uptime probe servers that solarwinds provides is a daily automatically updated list of these servers via an rss feed, which is not very user-friendly or easily readable at all.


For my use of pingdom uptime monotirong and availability reports for my restricted-access internet-application, I wrote these few scripts, to daily grab the rss-feeds and check the differences to the day before, so I get a quick and easy daily overview if any uptime probe servers have changed. 

This python-based script is used to automatically grab the pingdom uptime probe server list rss feed, which is based on "https://my.pingdom.com/probes/feed", and generate a list of all servers of the EU-Region with the most important data (ip-adress, hostname and location).
This list is then saved into a text-file which is named after the date of creation. The seconds script then compares the actual days file with the file of the day before, to check if there have been any changes to the server list (for example if uptime probe servers have been removed or added by solarwinds.)

A third shell script then automatically pushes the result-files of the comparation in the /results directory, as well as the actaul days file in the /rss directory into the github-repository automatically.

All these scripts are run on a lightweight linux vm and are triggered automatically via crontab on a set time of day.

