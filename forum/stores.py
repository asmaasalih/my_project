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
		all_members = self.get_all()
		a=all_members.index(self.id)  #index of id in the list
		result=all_members[a]
		return result

	def entity_exists(self, member):
		all_members=self.get_all()
		if self.member in all_members:
			return True
		return False
		
	def delete(self,id):
		member_deleted=self.get_by_id(self.id)
		self.all_members.remove(member_deleted)		
			
			



	
	

class PostStore:
	posts=[]

	def get_all(self):
		return self.posts



	def add(self,post):
		self.posts.append(post)
	

		