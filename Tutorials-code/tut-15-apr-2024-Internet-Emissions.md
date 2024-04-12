# CANS Part B Sustainability: Internet Emissions Life Cycle Analysis

The purpose of this tutorial is to illustrate by example the emissions arising from the use of networked systems. 

Let's consider a mobile device (e.g. an iPad) that communicates with a server in the cloud. Ten million users watch a TV show for half an hour on such a device, e.g. on the Apple TV app. Assume that it requires a thousand servers in a cloud data centre to serve the video streams. Assume the tablet is used for 15,000 hours over its whole life; the server is used for 40,000 hours. Given the following figures:

- Tablet embodied carbon: 120 kgCO2e
- Server embodied carbon: 1400 kgCO2e
- Data center PUE: 1.4 (*)
- Tablet electricity consumption: 0.002 kWh/h
- Server electricity consumption: 0.2 kWh/h
- Carbon intensity: 0.2 kgCO2e/kWh

(*) PUE = Power Usage Effectiveness. It expresses the overhead of cooling, lighting etc for every unit of energy spent on compute. So ideally, this should be 1 (no overhead), but in reality, overheads are often 50% or more. If all servers in a data centre together consume `servers_total` kWh, then the entire data centre consumes `servers_total*PUE` kWh.

1. What is the total carbon footprint of this activity (i.e. cloud + all end users)? Work out the calculation first in general, then using the specific values from above.

2. How do the contributions to the emissions (embodied/from use; cloud/end user) compare in this case? Can you think of a case where it would be very different?

3. Discuss the contributions from the network between the cloud and the tablet to the emissions. How could they be included in the total carbon footprint calculation?
