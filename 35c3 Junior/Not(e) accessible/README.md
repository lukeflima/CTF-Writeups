# Not(e) accessible
The challange was:  
![Challenge](https://i.imgur.com/UsDfSEZ.png)

When you open the link this shows up.  
![Firt page](https://i.imgur.com/HjFvFt6.png)

When you enter something on the input box and hit submit it return an ID, a password for the note and a link to view your note.    
![Return from submit](https://i.imgur.com/ydwZsuL.png)   

Clicking on the link it sends you to a page with whatever you wrote wrinten on it. The URL of this is 
```
http://35.207.120.163/view.php?id=-4133353959107185265&pw=437b930db84b8079c2dd804a71936b5f
```

Going on the page source code you can download the actual php souce code.  
```
.
├── backend
│   └── app.rb
└── frontend
    ├── assets
    │   ├── css
    │   │   └── bootstrap.min.css
    │   ├── fonts
    │   ├── images
    │   └── js
    │       ├── bootstrap.min.js
    │       ├── jquery-3.3.1.slim.min.js
    │       └── popper.min.js
    ├── index.php
    └── view.php
```
Going into the index.php we can see that the ID is a random int and the password is a md5 sum of whatever the note is and the password is stored in a file `./pws/$id.pw` and the note is stored in `$BACKEND."store/".$id."/".$note`.  

Looking into view.php we can gether that it checks if the file `./pws/".(int) $id.".pw"` exists, if so it get its content and compares with the password, if it matches echo the content of a get of the back end.  

Looking on the backend file, a ruby file, we can see that the have a /get entry that requires the id, and a entry /adim that echos the flag.  
So to get the flag we have to run the `$BACKEND/adimn` .  

To do so we'll use Directory Traversal to get into the admin, and type juggling to get through index.php.  
The idea of Directory Traversal is that we can access `$BACKEND/adimn` using ../ on the URL.  
And bypassing index.php using type juggling as that in the php code the ID is casted to an int. For that reason is why we can use the payload  
```
http://35.207.120.163/view.php?id=-4133353959107185265/../../admin&pw=437b930db84b8079c2dd804a71936b5f
```
cause in php 
```
echo( int '-4133353959107185265/../../admin')
$ -4133353959107185265
```
Using the payload it return us with the flag.
`35C3_M1Cr0_S3rvices_4R3_FUN!`
