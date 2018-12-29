# flags
The challange was:  
![Challange](https://i.imgur.com/e29Lffm.png)

When you open the link this shows up.
![Page of the call](https://i.imgur.com/37svQGY.png)

It shows the php code of the server, an warning and an image of flags.   

It can be observed that it takes the Accept-Language fild of the http header and it uses to open a file in the dir `flags/`. So it seems simple, just traverse back to `/` and get the flag.  
The only hicup is the str_replace function removes `../` from the string. To bypass that we use the string  `....//` that when passed onto the replace func it retruns `../`  

With that I created a script that changed the  Accept-Language fild of th http request's header to `....//....//....//....//flag` and then get the base64 file and decode it.  
In the end the flag is outputed `35c3_this_flag_is_the_be5t_fl4g `