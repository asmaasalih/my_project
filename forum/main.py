import models
import stores


member1 =models.Member("ahmed",33)
member2 =models.Member("mohamed",30)

post1=models.Post("Post1", "Content1")
post2= models.Post("Post2", "Content2")
post3= models.Post("Post3", "Content3")

#member store
member=stores.MemberStore()
member.add(member1)
member.add(member2)
print (member.get_all())

post=stores.PostStore()
post.add(post1)
post.add(post2)
post.add(post3)
print (post.get_all())
