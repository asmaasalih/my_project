class MemberStore:
	members = []
	last_id= 1

	def add(self,member):
		member.id=MemberStore.last_id
		MemberStore.members.append(member)
		MemberStore.last_id += 1

	def get_all(self):
		return self.members

	def get_by_id(self,id):
		result=None
		all_members = self.get_all()
		for e in all_members:
			if e.id==id:
				result =e
				break
		return result

	def entity_exists(self, member):
		result=True
		if get_by_id(id)==None:
				result=False
		return result
		
	def delete(self,id):
		member_del=self.get_by_id(id)
		MemberStore.members.remove(member_del)
			
	

class PostStore:
	posts=[]
	last_id=1
	def get_all(self):
		return self.posts



	def add(self,post):
		post.id=PostStore.last_id
		PostStore.posts.append(post)
		PostStore.last_id =PostStore.last_id+1

	def get_by_id(self,id):
		result=None
		all_posts=self.get_all()
		for e in all_posts:
			if e.id==id:
				result=e
		return result

	def entity_exists(self,post):
		result=True
		if (get_by_id(id)==None):
			result =None
		return result	

	def delete(self,id):
		post_del=get_by_id(id)	
		PostStore.posts.remove(post_del)				
	

		