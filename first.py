class student:
  def __init__(self,name):
    self.name = name 
  def show(self):
    print(f"name = {self.name}") 
c = student("sudam") 
c.show()
