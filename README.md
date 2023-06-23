# A Home Assistant Integration to monitor and control NBE pelletburners using the  UDP protocol

This integration should be able to connect to a scotte/RTB V7/V13 controllers (and apparently also aduro pellet hybrid stoves). The software 
is based on the NBE Test program https://github.com/motoz/nbetest by https://github.com/motoz

## Purpose

To reduce pellet consumption. The easiest way to reduce pellet consumption is to turn the pelletboiler off. The RTB App/Stokercloud makes it 
possible to set up weekly operating schedules for the boiler and for DHW. However it is only possible to define timeslots with a granularity 
of 2 hours. It is only possible to start and stop the boiler in equal hours (e.g. 04:00 or 06:00). The controller does not allow you to run the boiler for e.g. 3 hours. 

This can be adressed by adding an external switch/relay or by letting the Home Assistant communicate with the boiler directly. 

## Prerequsites

You'll need the boiler serial and the boiler passord (should be printet on a boiler label). You're using the same seriel/password when setting up your App, or logging in to StokerCloud.

Optionally you can choose to enter the boiler IP address. Either you need to set a fixed IP address in the boiler controller or you'll eed to make the address static with the help of your router. 

You can also choose to leave the IP-field empty. In that case, this integration will autodiscover the boiler. 

