import models
import stores


member1 =models.Member("ahmed",33)
member2 =models.Member("mohamed",30)

post1=models.Post("Post1", "Content1")
post2= models.Post("Post2", "Content2")
post3= models.Post("Post3", "Content3")

#member store
member_store=stores.MemberStore()
member_store.add(member1)
member_store.add(member2)
print (member_store.get_all())

post_store=stores.PostStore()
post_store.add(post1)
post_store.add(post2)
post_store.add(post3)
print (post_store.get_all())
