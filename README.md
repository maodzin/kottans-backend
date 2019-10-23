# Hi!
## I'm glad to be here!
All stuff is new for me but very **useful**!


## Http & Https

*Requests:*
 - ```curl https://api.github.com/users/maodzin```
 - ```curl -i https://api.github.com/users/maodzin```
 - ```curl --user "maodzin:*********" https://api.github.com/gists/starred```
 -  ```curl --user "maodzin" https://api.github.com/gists/starred```
 - ```curl -i https://api.github.com/orgs/kottans/repos```
 - ```
   curl -H 'Authorization: token 5199831f4dd3b79e7c5b7e0ebe75d67aa66e79d4'
          -d '{\ 
             "title": "New logo", \
             "body": "We should have one", \
             "labels": ["design"] \
              }'\
           https://api.github.com/repos/maodzin/kottans-backend/issues
    ```       
    
1. 
 - Privacy - eavesdropping passwords and private information
 - Integrity - "man-in-the-middle" attack
 - Identification - phishing and fake sites


2. 	The main idea of public key is setting up initial connection ("hand shake") and access to digital signature of public key owner.
 

3. 
  
 Request: </br>
 `POST /pets {'petName': string, 'age': int, 'breed': string, 'ownerName': string, 'medicalHistory': string}`
	Response: </br>
 `201 {'id': int, 'petName': string, 'age': int, 'breed': string, 'ownerName': string, 'medicalHistory': string}`

	
 Request: </br>
 `GET /pets?name=string\`
	Response: </br>
 `200 [{'id': int, 'petName': string, 'age': int, 'breed': string, 'ownerName': string, 'medicalHistory': string}`


 Request: </br>
 `PUT /pets/<pet_id:int> {'petName': string}`\
	Response: </br>
 `200 {'id': int, 'petName': string}`

	 
 Request: </br>
 `PUT /pets/<pet_id:int> {'medicalHistory': string}`\
	Response: </br>
 `200 {'id': int, 'petName': string, 'medicalHistory': string}`

	 
 Request: </br>
 `PUT /doctors/<doctor_id:int> {'assignedPets': [int, ...]}`\
	Response: </br>
 `200 {doctor_id:int, 'id': int, 'petName': string, ..., 'assignedPets': [int, ...]}`

	
 Request: </br>
 `POST /appointments {'petId': int, 'doctorId': int, 'AppointmentDateTime': date, 'description': string}`\
 Response: </br>
  `201 {'id': int, 'petId': int, 'doctorId': int, 'AppointmentDateTime': date, 'description': string}`



## TCP. UDP. Network

[Link to sniffer.py](https://github.com/maodzin/kottans-backend/blob/master/task_networks/sniffer.py).


![TCP. UDP. Network](https://github.com/maodzin/kottans-backend/blob/master/task_networks/task_networks-1.jpg)


![TCP. UDP. Network](https://github.com/maodzin/kottans-backend/blob/master/task_networks/task_networks-2.jpg)


## Memory Management

- When program reaches maximum limit of stack we have a condition called stack overflow and the program receives a Segmentation Fault
- If program requests a big (more then 128KB) memory allocation on heap  the C library will create such an anonymous memory mapping instead of using heap memory
- The data segment holds the contents for static variables initialized in source code. This memory area is not anonymous. 
Data in Data memory segement has read/write permission. The string lives in the text segment, which is read-only and stores all of your code like string literals.

```md
00010000-000ea000 r-xp 00000000 b3:07 392484     /bin/bash
000f9000-000fa000 r--p 000d9000 b3:07 392484     /bin/bash
000fa000-000ff000 rw-p 000da000 b3:07 392484     /bin/bash
000ff000-00108000 rw-p 00000000 00:00 0 
01dce000-01ee2000 rw-p 00000000 00:00 0          [heap]
76b3c000-76b45000 r-xp 00000000 b3:07 1313216    /lib/arm-linux-gnueabihf/libnss_files-2.24.so
76b45000-76b54000 ---p 00009000 b3:07 1313216    /lib/arm-linux-gnueabihf/libnss_files-2.24.so
76b54000-76b55000 r--p 00008000 b3:07 1313216    /lib/arm-linux-gnueabihf/libnss_files-2.24.so
76b55000-76b56000 rw-p 00009000 b3:07 1313216    /lib/arm-linux-gnueabihf/libnss_files-2.24.so
76b56000-76b5c000 rw-p 00000000 00:00 0 
76b5c000-76b65000 r-xp 00000000 b3:07 1313218    /lib/arm-linux-gnueabihf/libnss_nis-2.24.so
76b65000-76b74000 ---p 00009000 b3:07 1313218    /lib/arm-linux-gnueabihf/libnss_nis-2.24.so
76b74000-76b75000 r--p 00008000 b3:07 1313218    /lib/arm-linux-gnueabihf/libnss_nis-2.24.so
76b75000-76b76000 rw-p 00009000 b3:07 1313218    /lib/arm-linux-gnueabihf/libnss_nis-2.24.so
76b76000-76b87000 r-xp 00000000 b3:07 1313212    /lib/arm-linux-gnueabihf/libnsl-2.24.so
76b87000-76b96000 ---p 00011000 b3:07 1313212    /lib/arm-linux-gnueabihf/libnsl-2.24.so
76b96000-76b97000 r--p 00010000 b3:07 1313212    /lib/arm-linux-gnueabihf/libnsl-2.24.so
76b97000-76b98000 rw-p 00011000 b3:07 1313212    /lib/arm-linux-gnueabihf/libnsl-2.24.so
76b98000-76b9a000 rw-p 00000000 00:00 0 
76b9a000-76ba0000 r-xp 00000000 b3:07 1313213    /lib/arm-linux-gnueabihf/libnss_compat-2.24.so
76ba0000-76baf000 ---p 00006000 b3:07 1313213    /lib/arm-linux-gnueabihf/libnss_compat-2.24.so
76baf000-76bb0000 r--p 00005000 b3:07 1313213    /lib/arm-linux-gnueabihf/libnss_compat-2.24.so
76bb0000-76bb1000 rw-p 00006000 b3:07 1313213    /lib/arm-linux-gnueabihf/libnss_compat-2.24.so
76bb1000-76d4c000 r--p 00000000 b3:07 1188408    /usr/lib/locale/locale-archive
76d4c000-76e76000 r-xp 00000000 b3:07 1313206    /lib/arm-linux-gnueabihf/libc-2.24.so
76e76000-76e85000 ---p 0012a000 b3:07 1313206    /lib/arm-linux-gnueabihf/libc-2.24.so
76e85000-76e87000 r--p 00129000 b3:07 1313206    /lib/arm-linux-gnueabihf/libc-2.24.so
76e87000-76e88000 rw-p 0012b000 b3:07 1313206    /lib/arm-linux-gnueabihf/libc-2.24.so
76e88000-76e8b000 rw-p 00000000 00:00 0 
76e8b000-76e8d000 r-xp 00000000 b3:07 1313209    /lib/arm-linux-gnueabihf/libdl-2.24.so
76e8d000-76e9c000 ---p 00002000 b3:07 1313209    /lib/arm-linux-gnueabihf/libdl-2.24.so
76e9c000-76e9d000 r--p 00001000 b3:07 1313209    /lib/arm-linux-gnueabihf/libdl-2.24.so
76e9d000-76e9e000 rw-p 00002000 b3:07 1313209    /lib/arm-linux-gnueabihf/libdl-2.24.so
76e9e000-76eba000 r-xp 00000000 b3:07 1314977    /lib/arm-linux-gnueabihf/libtinfo.so.5.9
76eba000-76eca000 ---p 0001c000 b3:07 1314977    /lib/arm-linux-gnueabihf/libtinfo.so.5.9
76eca000-76ecc000 r--p 0001c000 b3:07 1314977    /lib/arm-linux-gnueabihf/libtinfo.so.5.9
76ecc000-76ecd000 rw-p 0001e000 b3:07 1314977    /lib/arm-linux-gnueabihf/libtinfo.so.5.9
76ee2000-76ee7000 r-xp 00000000 b3:07 1187323    /usr/lib/arm-linux-gnueabihf/libarmmem.so
76ee7000-76ef6000 ---p 00005000 b3:07 1187323    /usr/lib/arm-linux-gnueabihf/libarmmem.so
76ef6000-76ef7000 r--p 00004000 b3:07 1187323    /usr/lib/arm-linux-gnueabihf/libarmmem.so
76ef7000-76ef8000 rw-p 00005000 b3:07 1187323    /usr/lib/arm-linux-gnueabihf/libarmmem.so
76ef8000-76f19000 r-xp 00000000 b3:07 1313189    /lib/arm-linux-gnueabihf/ld-2.24.so
76f1d000-76f24000 r--s 00000000 b3:07 1182424    /usr/lib/arm-linux-gnueabihf/gconv/gconv-modules.cache
76f24000-76f28000 rw-p 00000000 00:00 0 
76f28000-76f29000 r--p 00020000 b3:07 1313189    /lib/arm-linux-gnueabihf/ld-2.24.so
76f29000-76f2a000 rw-p 00021000 b3:07 1313189    /lib/arm-linux-gnueabihf/ld-2.24.so
7eece000-7eeef000 rw-p 00000000 00:00 0          [stack]
7eef0000-7eef1000 r-xp 00000000 00:00 0          [sigpage]
7eef1000-7eef2000 r--p 00000000 00:00 0          [vvar]
7eef2000-7eef3000 r-xp 00000000 00:00 0          [vdso]
ffff0000-ffff1000 r-xp 00000000 00:00 0          [vectors]
```
- Heap - 01dce000-01ee2000
- Stack - 7eece000-7eeef000
- MMS - 76b3c000-76b45000

- Memory managment is new thing for me
- Memory usage and leakage in Python  - I got additional knowledge in this theme that I'll definitily use in future


## Python Basic I

[Link to Hackerrank Profile](https://www.hackerrank.com/maxxox?hr_r=1).


![Python Basic I](https://github.com/maodzin/kottans-backend/blob/master/python_basic_1/python_basic_1.jpg)


![Python Basic I](https://github.com/maodzin/kottans-backend/blob/master/python_basic_1/python_basic_2.jpg)




## Git Collaboration

![Git Collaboration](https://github.com/maodzin/kottans-backend/blob/master/task_git_collaboration/task_git_collaboration.jpg)
- Git Collabaration is very useful and very powerful in team work
- To remember all commands and fluent applying in work require some experience
 

## Unix Shell

![Task unix shell](https://github.com/maodzin/kottans-backend/blob/master/task_unix_shell/task_unix_shell.jpg)

- Useful issue with file manipulation
- Navigation is a little familiar from previous experience
- Certainly, I'll use shell commands in future
- I/O redirection and pipelines issue have to be practice 
- Expensions is mighty thing
