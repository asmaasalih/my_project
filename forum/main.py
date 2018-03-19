import models


member1=models.Member("ahmed",33)
member2=models.Member("mohamed",30)

post1=models.Post("Computer Science and Engineering","Computer Science and Engineering (CSE) is an interdisciplinary academic program at some universities that combines aspects of both computer science and computer engineering programs.")
post2=models.Post("Civil engineer","A civil engineer is a person who practices civil engineering, the application of planning, designing, constructing, maintaining, and operating infrastructures while protecting the public and environmental health, as well as improving existing infrastructures that have been neglected.")
post3=models.Post("Telecommunications engineering","Telecommunications engineering is an engineering discipline centered on electrical and computer engineering which seeks to support and enhance telecommunication systems.")

print member1
print "_"*10
print member2
print "_"*50
print post1
print "_"*50
print post2
print "_"*50
print post3