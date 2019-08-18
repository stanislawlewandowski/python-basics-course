text = 'Mechanical advantage is a measure of the force amplification achieved by using a tool, mechanical device' \
       ' or machine system. The device preserves the input power and simply trades off forces against movement to ' \
       'obtain a desired amplification in the output force. The model for this is the law of the lever. Machine' \
       ' components designed to manage forces and movement in this way are called mechanisms.[1] An ideal mechanism' \
       ' transmits power without adding to or subtracting from it. This means the ideal mechanism does not include' \
       ' a power source, is frictionless, and is constructed from rigid bodies that do not deflect or wear.' \
       ' The performance of a real system relative to this ideal.'
words = text.split(' ')
short_text = ' '
counter = 0
for word in words:
    short_text += word + ' '
    counter += 1
    if counter >= 20:
        print(short_text)
        break
