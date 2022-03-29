#ex1
var1 = "priscille mutoba"
basic.show_string(var1)

def on_forever():
    pass
basic.forever(on_forever)

#ex1
def on_forever():
    led.plot(3, 2)
    basic.pause(200)
    led.unplot(3, 2)
basic.forever(on_forever)
