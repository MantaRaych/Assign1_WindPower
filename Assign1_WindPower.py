#######################################################################
# Program Filename: Wind Turbine Efficiency
# Author:  Rachel Lindgren
# Date: 11 April 2022
# Description: This program will calculate the wind power generated
# by a turbine
# Input: Average wind speed, blade radius, turbine efficiency
# Output: Area of turbine blade, maximum available power,
# actual power generated
#######################################################################
##################
#Constants
PI = 3.14159265359
RHO = 1.2
OR_POWER_PER_CAP_PER_YR = (2.57*10e10)/31536000 #W

#Calculating area of the blade
Turbine_blade_radius = float(input("Enter radius of turbine blade: ")) #m
Blade_area = Turbine_blade_radius**2 * PI #m2
print("Area of blade:", Blade_area, "m2")

#Calculate maximum power generation
Avg_Wind_Speed = float(input("Enter average wind speed in m/s: ")) #m/s
Pmax = round(0.5*RHO*Blade_area*(Avg_Wind_Speed)**3, 2) #W
print("Maximum available power:", Pmax, "W")

#Calculate actual power generation
Turbine_efficiency = float(input("Enter turbine efficiency: ")) #%
Actual_power = round((Turbine_efficiency/100)*Pmax,2) #W
print("Actual power generated:", Actual_power, "W")

#Turbines needed to power one Oregonian for one year
numTurbines = OR_POWER_PER_CAP_PER_YR/Actual_power
print("It will take", numTurbines, "turbines to power an Oregonian "
      "for one year.")