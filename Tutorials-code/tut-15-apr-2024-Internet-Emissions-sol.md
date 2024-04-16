# Sustainability Part 2: Internet Emissions Life Cycle Analysis

Given a mobile device (e.g. an iPad) that communicates with a server in a cloud. Ten million users watch a TV show for half an hour, e.g. on the Apple TV app. Assume that it requires a thousand servers in a cloud data centre to serve the video stream. Assume the tablet is used for 15,000 hours over its whole life; the server is used for 40,000 hours. Given the following figures:

- Tablet embodied carbon: 120 kgCO2e
- Server embodied carbon: 1400 kgCO2e
- Data center PUE: 1.4 (*)
- Tablet electricity consumption: 0.002 kWh/h
- Server electricity consumption: 0.2 kWh/h
- Carbon intensity: 0.2 kgCO2e/kWh

(*) PUE = Power Usage Effectiveness. It expresses the overhead of cooling, lighting etc for every unit of energy spent on compute. So ideally, this should be 1 (no overhead), but in reality, overheads are often 50% or more. If all servers in a data centre together consume `servers_total` kWh, then the entire data centre consumes `servers_total*PUE` kWh.

(i)	What is the total carbon footprint of this activity (i.e. cloud + all end users)? Explain the calculation.

n_servers*(carbon_intensity*PUE*server_kWh + server_use_time*server_embodied/server_lifetime)
+ n_tablets*(carbon_intensity*PUE*tablet_kWh + tablet_use_time*tablet_embodied/tablet_lifetime)
1000*(0.2*1.4*0.2 + 0.5*1400/40000 ) + 10000000*( 0.002*0.2 = 0.5*120/15000+)
= (2*14*2 + 70/4) + 1000*( 2*2 + 240/6)
= 4*14+17.5 + 1000*(4+40)
= 56+17.5 + 44000

= 44.0735 ton CO2e: 73.5 kg for the cloud, 44 ton for the tablets.


(ii) How do the contribution to the emissions (embodied/from use; cloud/end user) compare in this case?

It is entirely dominated by the embodied carbon of the tablets (40 tons)

(iii) Discuss the contributions from the network between the cloud and the tablet to the emissions. How could they be included in the calculation under (i)?

The problem is that the network is always on, and that there are other users active besides the 10M watching that show. So both the embodied carbon and emissions from use need to be scaled on the total number of users. Because the internet is 85% video, a good approximation is to assume that it is 100% video. Then estimate the total number of video hours watched and use that as the scale factor to get at the emissions per hour of video watched. 
