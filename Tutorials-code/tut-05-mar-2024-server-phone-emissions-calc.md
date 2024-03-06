---
linkcolor: blue
---
# Carbon footprints of servers and phones

I recommend that you use a Jupyter notebook for this exercise, for example [https://jupyterlite.github.io/demo](https://jupyterlite.github.io/demo/lab/index.html).

## Embodied carbon and emissions from use of a server

Based on a Dell PowerEdge R7515 with an Nvidia A100 GPU

### Embodied carbon

Given a server with the following specification:

* CPU: AMD 32 cores, 1GHz
* GPU: Nvidia A100, 1GHz, 40 GB on-board memory
* SSD: 4 TB, 2x
* RAM: 128 GB (8 x 16 GB)
* NIC: Gb Ethernet

We can get the following figures for embodied carbon from various data sheets and papers:

* CPU: 40 kgCO2e
* GPU: 200 kgCO2e (incl on-board RAM) 
* SSD: 400 kgCO2e per disk
* RAM: 30 kgCO2e per 16 GB module
* all other components: 112 kgCO2e

#### Question 1

How much (in kgCO2e) is the embodied carbon of this server?

#### Question 2

- How much of this is contributed by the SSD, the GPU and the CPU? 
- Which component dominates and by how much? 


### CO2 emissions from use

* Assuming the server consumes 1660 kWh/year and has a lifetime of 4 years
* Using the following figures for electricity carbon intensity:
	- World: 475 gCO2e/kWh
	- EU: 265 gCO2e/kWh
	- UK: 182 gCO2e/kWh
	- Glasgow: 30 gCO2e/kWh

#### Question 3

How much (in kgCO2e) are the CO2 emissions from lifetime use of this server in these four geographical areas?

#### Question 4

If we want to minimise emissions, what does this mean for the lifetime of the server?


## Carbon emissions of a smartphone

Based on a Apple iPhone X

### Embodied carbon

Given a phone with the following specification:

* CPU+GPU: Apple A11 Arm CPU (Hexa-core 2.39 GHz (2x Monsoon + 4x Mistral)) + 3-core GPU
* SSD: 64 GB / 256 GB
* RAM: 3 GB

We can get a total figure for embodied carbon from the paper by Clément et al:

* Total 70 kgCO2e 

#### Question 5

- Based on the information in the lecture slides, what percentage of this is contributed by the chips, display and battery?
- Which component dominates and by how much?

### CO2 emissions from use

* Assuming the phone consumes 4 kWh/year and has a lifetime of 3 years

* Using the following figures for electricity carbon intensity:
    - World: 475 gCO2e/kWh (the paper by Clément et al assumed 813)
	- EU: 265 gCO2e/kWh
	- UK: 182 gCO2e/kWh
	- Glasgow: 30 gCO2e/kWh

#### Question 6

How much (in kgCO2e) are the CO2 emissions from lifetime use of this phone in these four geographical areas?

#### Question 7

How does this compare to the embodied carbon

## Comparison servers and phones

#### Question 8

Assuming that all phones and servers are similar to these two examples, what causes most emissions, phones or servers? There are an estimate 5-10 billion smart phones and 50-200 million servers in the world.

