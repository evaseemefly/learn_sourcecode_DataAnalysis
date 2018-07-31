# The current volume of a water reservoir (in cubic metres)
# 蓄水池的现时容量(以立方米计算)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
# 暴风雨的降雨量(立方米)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
# 降雨量减少10%，用于径流。
runoff=rainfall*0.1
print(runoff)
# add the rainfall variable to the reservoir_volume variable

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm

# decrease reservoir_volume by 5% to account for evaporation

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.

# print the new value of the reservoir_volume variable
