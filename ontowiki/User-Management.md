---
title: User Management
tags: [ontowiki]
sidebar: ontowiki_sidebar
permalink: /User-Management.html
editme_path: ontowiki/User-Management.md
---

# Creating a new User
You have to create the user with the "Register User" function (Menu: "User" > "Register New User", `http://<ontowiki>/application/register`)
Per default this functionality is publicly available.

If you directly create or edit an instance of `sioc:User` with the normal editing functionality it takes all of the properties literally, this means especially, that the password is not encrypted resp. hashed.

# Change Password
If you want to change the password of a user you have to login as this user and go to Menu: "User" > "Preferences", (`http://<ontowiki>/application/preferences`).
Don't forget to tick the field "Change Password?"

If you don't know the password of the user and want to set a new one, the workaround is:

1. Login as Administrator or System-Administrator
2. remove the password property of this user
3. logout and login as the user with an empty password
4. Now you can set a new password as described above
