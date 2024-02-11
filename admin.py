#!/usr/bin/env python
# coding: utf-8

# In[ ]:



class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        return self.username == username and self.password == password

    def forgot_password(self):
        # Implement the forgot password logic here
        pass

    def edit_profile(self, new_username, new_password):
        self.username = new_username
        self.password = new_password

    def change_password(self, new_password):
        self.password = new_password

