import Gather
class Mq2:
	def __init__(self,value=0):
		self.smoke=value
	def getValue(self):
		return self.smoke
        def updateValue(self):
            Gather.gather(self,"Smoke")

d=Mq2()
print "Hello"
d.updateValue()
print d.getValue()
