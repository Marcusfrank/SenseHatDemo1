from sense_hat import SenseHat


sense = SenseHat()


b = (255,0,0)
y = (255,255,255)

image = [
b,b,y,y,b,b,b,b,
b,b,y,y,b,b,b,b,
b,b,y,y,b,b,b,b,
y,y,y,y,y,y,y,y,
y,y,y,y,y,y,y,y,
b,b,y,y,b,b,b,b,
b,b,y,y,b,b,b,b,
b,b,y,y,b,b,b,b
  ]
  
sense.set_pixels(image)
