class Member:
	def __init__(self, name , age):
		self.name = name
		self.age=age

	def __str__(self):
		return "name:{} ,age: {}".format(self.name,self.age)



class Post:
	def __init__(self , title , content):
		self.title = title
		self.content = content

	def __str__(self):
		return "post title:{},\n post content:{} ".format(self.title,self.content)
			

				