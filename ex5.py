name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74.00000 / 0.39370 # inches to cm
weight = 180 / 2.2046 # lbs to kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %x centimeters tall." % height
print "He's %x kilograms heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)