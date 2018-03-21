class Member:
	def __init__(self, name , age):
		self.name = name
		self.age=age
		self.id=0

	def __str__(self):
		return "name:{} ,age: {},id:{}".format(self.name,self.age,self.id)



class Post:
	def __init__(self , title , content):
		self.title = title
		self.content = content
		self.id=0

	def __str__(self):
		return "post title:{},\n post content:{} ".format(self.title,self.content)
			

				