import Gather
class Mq135:
	def __init__(self,value=0):
		self.amonia=value
	def getValue(self):
		return self.amonia
        def updateValue(self):
            Gather.gather(self,"Amonia")

d=Mq135()
d.updateValue()
print "Hello"
print d.getValue()
