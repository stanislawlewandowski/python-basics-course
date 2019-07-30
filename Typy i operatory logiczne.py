isAutomaticMode = True
# is the level of day-lighr above 80%
is80PercentLight = True
# is the Sun ligthing directly into the driver's face
isDirectLight = True
# is it rainy, foggy or other weather conditions are present
isRainy = False
turnLightsOn = isAutomaticMode and (not is80PercentLight or isDirectLight or isRainy)
print("Automatic mode:", isAutomaticMode)
print("Is the light good:", is80PercentLight)
print("Is sun low: ", isDirectLight)
print("Is it rainy:", isRainy)
print("TURN LIGHTS ON:", turnLightsOn)
