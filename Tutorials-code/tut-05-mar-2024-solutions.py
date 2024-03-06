"""
# Carbon emissions of a server

Based on a Dell PowerEdge R7515 with an Nvidia A100 GPU

## Embodied carbon

Given a server with the following specification:

* CPU: AMD 32 cores, 1GHz
* GPU: Nvidia A100, 1GHz, 40 GB on-board memory
* SSD: 4 TB, 2x
* RAM: 128 GB (8 x 16 GB)
* NIC: Gb Ethernet

We can get the following figures for embodied carbon from various data sheets and papers:

* CPU: 41 kgCO2e
* GPU: 200 kgCO2e (incl on-board RAM) 
* SSD: 434 kgCO2e per disk
* RAM: 33 kgCO2e per 16 GB module
* all other components: 225 kgCO2e

# Question 1. How much (in kgCO2e) is the embodied carbon of this server?
"""

embodied_carbon_cpu  = 41
embodied_carbon_gpu = 200
embodied_carbon_ssd = 434
embodied_carbon_ram = 33
embodied_carbon_rest = 225
embodied_carbon_tot = embodied_carbon_cpu+embodied_carbon_gpu+8*embodied_carbon_ram+2*embodied_carbon_ssd+embodied_carbon_rest
print('Total embodied carbon:',embodied_carbon_tot)


"""
# CO2 emissions from use

* Assuming the server consumes 1660 kWh/year and has a lifetime of 4 years
* Using the following figures for electricity carbon intensity:
	- EU: 265 gCO2e/kWh
	- UK: 182 gCO2e/kWh
	- Glasgow: 30 gCO2e/kWh

Question 3. How much (in kgCO2e) are the CO2 emissions from lifetime use of this server in these three locations?
"""

lifetime = 4 # years
energy_consumption = 1660 # kWh/year
ci_world = 475 # https://www.iea.org/reports/global-energy-co2-status-report-2019/emissions
ci_eu = 265 # gCO2e/kWh
ci_uk = 182
ci_gl = 30

co2_world = lifetime*energy_consumption*ci_world/1000
co2_eu = lifetime*energy_consumption*ci_eu/1000
co2_uk = lifetime*energy_consumption*ci_uk/1000
co2_gl = lifetime*energy_consumption*ci_gl/1000
print(co2_world,co2_eu,co2_uk,co2_gl)

# Phone 

embodied_carbon_tot_phone = 70
lifetime_phone = 3 # years
energy_consumption_phone = 4 # kWh/year

co2_world_phone = lifetime_phone*energy_consumption_phone*ci_world/1000
co2_eu_phone = lifetime_phone*energy_consumption_phone*ci_eu/1000
co2_uk_phone = lifetime_phone*energy_consumption_phone*ci_uk/1000
co2_gl_phone = lifetime_phone*energy_consumption_phone*ci_gl/1000
print(co2_world_phone,co2_eu_phone,co2_uk_phone,co2_gl_phone)

n_servers_min =  50*1e6
n_servers_max =  200*1e6
n_phones_min = 5*1e9
n_phones_max = 10*1e9

total_emissions_server_min = int(n_servers_min*(embodied_carbon_tot+co2_world)*1e-9)
total_emissions_server_max = int(n_servers_max*(embodied_carbon_tot+co2_world)*1e-9)
total_emissions_phone_min = int(n_phones_min*(embodied_carbon_tot_phone+co2_world_phone)*1e-9)
total_emissions_phone_max = int(n_phones_max*(embodied_carbon_tot_phone+co2_world_phone)*1e-9)

print('Servers:',total_emissions_server_min,total_emissions_server_max)
print('Phones:',total_emissions_phone_min,total_emissions_phone_max)