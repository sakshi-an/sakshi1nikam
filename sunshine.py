from turtle import *
bgcolor('black')
color('white','yellow')
begin_fill()
while True:
         forward(200)
         left(170)
         if abs(pos())<1:
                  break
end_fill()
done()
