# pingdom-rss-eu-diffcheck
This Repository is automatically updated once per day at around 7:30 CET. 

Solarwinds Pingdom is a Uptime Probe Service, that you can monitor your server uptimes with. They either use ICMP/Ping Requests or Curl Requests regularly to check if your service/application is online. If the curl/ping request results in a negative, you will get alerted that your application/service is DOWN. 

Pingdom uses a wide variety of servers all around the globe for their uptime probe service. Sadly, these servers can change (some might be dismissed, new ones might be added etc.). Therefore, if you have to manually manage your firewall in order to let the curl/ping requests come trough, you will start getting false DOWN-notifications, if a pingdom server is dismissed or a new one is added. 
The only information about their uptime probe servers that solarwinds provides is a daily updated list of these servers in an rss feed. Not very user-friendly or readable at all, if you need to know about the changes of the servers as quickly as possible.

This python script checks the rss-feed daily, pulls all relevant information (hostname, ip-adress, location) about the servers out of the feed,


T B C ... ... ... 
