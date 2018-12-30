# ultra secret
The challange was:  
![ultra secret chall](https://i.imgur.com/4kf9EnM.png)

And povides with a nc conection and source code.  

When you try to connect with the nc it ask you, very politly, to enter the "very secret password".  
```
$ nc 35.207.158.95 1337
$ Please enter the very secret password:
```
Looking to the source code we see that is in Rust.
It loads some hashes to a vector of strings and load the flag to the the flag variable. And then it ask for the password. The password must have at least 32 char and it only uses the first 32, and for each char of the password it calls function hash on it. If the hash of the char didn't match with the loaded one it killed the program whitch is useful for the attack. If it passes all the tests the flag is cat'd out.   
![hash function](https://i.imgur.com/NnvsxYp.png)  
Lookin at the hash function we see that peforms a SHA256 on itself 9999 times. Instinctively, I though that would take a long time, so I'll try a Timming Attack.  

So with a payload of containing 32 'a' it took the server 0.85s to respond. So I started to change the first char of the payload and see how much time it takes to respond.  
```
payload			                 time
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.858063936234
baaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.859606981277
caaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.858677148819
daaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.87083697319
eaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.859264135361
faaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.871843099594
gaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.857834815979
haaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.86031794548
iaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.860155105591
jaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.862596988678
kaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.86190199852
laaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.869740009308
maaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.859644889832
naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.857651948929
oaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.863571882248
paaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.857762813568
qaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.857203960419
raaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.867964982986
saaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.863717079163
taaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.868489980698
uaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.861666917801
vaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.861833095551
waaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.859680891037
xaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.858031988144
yaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.86004281044
zaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.86369395256
0aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.858286857605
1aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 1.52406692505
2aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.863839864731
3aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.860507011414
4aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.872466087341
5aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.857763767242
6aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.859325170517
7aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.858371973038
8aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.860785007477
9aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa 0.862840890884
```
And I notice when the payload started it with a '1', it took 0.66s more to respond and that the rest averaged at the same time to respond. So I gether that the hash function takes 0.66s to be executed on the server's machine.  
With that a created a script to extract char by char of the password using the time it takes to the server to respond.    

After a long time, the flag poped out on the terminal
`35C3_timing_attacks_are_fun!_:)`  
and the final payload was `10e004c2e186b4d280fad7f36e779ed4`  
