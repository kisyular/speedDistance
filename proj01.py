#
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:34:06 2015
@author: kisyular
"""

###########################################################################
#Algorithm
#   Prompt the user for values of speed and distance
#   display results of entered inputs by the user
#   display results of calculations for hare and tortoise
#   show the results of the final calculations
###########################################################################

import math

#   Prompt the user for values of speed and distance

total_distance=input ("the distance to finish line(in miles)")
speed_of_tortoise=input ("the speed of the tortoise (in inches per minute)")
speed_of_hare=input ("the speed of the hare (in miles per hour)")
time_hare_rest=input ("the time that the hare rests after running (in minutes)")
time_the_hare_runs=input ("the time that the hare runs before resting (in minutes)")

#   display results of entered

print( )
print( "The distance is", total_distance, )
print( "the speed of tortoise is", speed_of_tortoise, )
print( "the speed of hare is", speed_of_hare, )
print( "the time the hare rests is", time_hare_rest, )
print( "the time the hare runs before resting is", time_the_hare_runs, )

#   display results of calculations for hare and tortoise

total_distance_float = float( total_distance )
speed_of_tortoise_float = float( speed_of_tortoise )
speed_of_hare_float = float( speed_of_hare )
time_hare_rest_float = float( time_hare_rest )
time_the_hare_runs_float = float( time_the_hare_runs )

print( "The ceiling of", total_distance_float, "is", math.ceil( total_distance_float) )
print( "The floor of", total_distance_float, "is", math.floor( total_distance_float ) )
speed_of_tortoise_in_miles = (speed_of_tortoise_float * 0.00094696969)
print( "the speed of tortoise", speed_of_tortoise_in_miles, )

#   show the results of the final calculations

speed_of_tortoise_in_miles_float = float(speed_of_tortoise_in_miles)
print( "the total time the tortoise takes in hours is", total_distance_float/speed_of_tortoise_in_miles_float)

time_hare_takes_no_rest = (total_distance_float / speed_of_hare_float)
remaining_distance = (total_distance_float % speed_of_hare_float)

print("the combined time hare takes without resting is",total_distance_float / speed_of_hare_float)
print("the remaining distance is",total_distance_float % speed_of_hare_float)

time_hare_takes_no_rest_float = float( time_hare_takes_no_rest )


time_hare_takes_no_rest_float= (total_distance_float / speed_of_hare_float)
number_of_time_hare_runs = (math.ceil((time_hare_takes_no_rest_float)/(time_the_hare_runs_float/60))-1)
number_of_time_hare_runs_float = float(number_of_time_hare_runs)

time_hare_takes_to_finish =(time_hare_takes_no_rest_float)+(number_of_time_hare_runs_float*(time_hare_rest_float/60))
time_hare_takes_to_finish_float = float(time_hare_takes_to_finish)

print("the total time the hare takes in hours is",  time_hare_takes_to_finish_float)