class User:
    def __init__(self,password,email,name, current_job_title):
        self.password = password
        self.email = email
        self.name = name
        self.current_job_title = current_job_title
    
    def change_pass(self,new_password):
        self.password = new_password
        
    def change_job_title(self,new_job_title):
        self.current_job_title = new_job_title
    
    def get_user_info(self):
        print(f"User {self.name}, currently works as a {self.current_job_title}")
    
    def get_name(self):
        return self.name 

