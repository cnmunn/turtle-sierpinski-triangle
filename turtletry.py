from turtle import *
def kockSnowflake(lengthSide, levels):
	if(levels == 0):
		forward(lengthSide)
		return
	lengthSide /=3
	kockSnowflake(lengthSide, levels-1)
	left(60)
	kockSnowflake(lengthSide, levels-1)
	right(120)
	kockSnowflake(lengthSide, levels-1)
	left(60)
	kockSnowflake(lengthSide, levels-1)


if __name__ == "__main__":
	speed(150000)
	length = 100.00
	penup()
	#pendown()
	backward(50)
	pendown()
	begin_fill()
	for i in range(6):
		for i in range(3):
			kockSnowflake(length, 3)
			right(120)
		left(60)
	end_fill()
	mainloop()
	done()
