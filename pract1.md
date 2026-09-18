# практическая 1

## Задание 1
```
grep -o '^[^:#][^:]*' passwd | sort
```

## Задание 2
```
grep -v '^#' protocols | sort -k2 -rn | head -n 5 | awk '{print $2, $1}'
```

## Задание 3
```
bash-3.2$ cat > banner << 'END'
> #!/bin/bash
> text="$1"
> len=${#text}
> line=""
> for ((i = 0; i < len + 2; i++)); do
> line+="-"
> done
> echo "+${line}+"
> echo "| ${text} |"
> echo "+${line}+"
> END
bash-3.2$ ls -l banner
-rw-r--r--  1 meowloned  staff  148 18 сент. 14:28 banner
bash-3.2$ chmod +x banner
bash-3.2$ set +H
bash-3.2$ ./banner "Hello from RTU MIREA!"
+-----------------------+
| Hello from RTU MIREA! |
+-----------------------+
```

## Задание 4
```
bash-3.2$ cat > hello.c << 'END'
> #include <stdio.h>
> 
> int h = 5;
> int n = 10;
> 
> int main() {
>     printf("Hello, world!\n");
>     return 0;
> }
> END
bash-3.2$ cat > identifier << 'END'
> #!/bin/bash
> if [ -z "$1" ]; then
> echo "No file used"
> exit 1
> fi
> 
> if [ ! -e "$1" ]; then
> echo "File not found"
> exit 1
> fi
> 
> grep -o '[A-Za-z_][A-Za-z0-9_]*' "$1" | sort -u | tr '\n' ' '
> echo
> END
bash-3.2$ chmod +x identifier
bash-3.2$ ./identifier
No file used
bash-3.2$ ./identifier what.c
File not found
bash-3.2$ ./identifier hello.c
h Hello include int main n printf return stdio world 
```

## Задание 5
```
bash-3.2$ cat > reg << 'END'
> #!/bin/bash
> if [ -z "$1" ]; then
> echo "No file used"
> exit 1
> fi
>  
> if [ ! -e "$1" ]; then
> echo "File not found"
> exit 1
> fi
> 
> sudo cp "$1" /usr/local/bin/
> sudo chmod +x /usr/local/bin/"$1"
> echo "'$1' registered in /usr/local/bin"
> END
bash-3.2$ ./reg banner
'banner' registered in /usr/local/bin
bash-3.2$ cd /tmp
bash-3.2$ banner 'Hi from anywhere!'
+-------------------+
| Hi from anywhere! |
+-------------------+
```

## Задание 6
```
bash-3.2$ cat > test.c << 'END'
> // комментарий
> int main() { return 0; }
> END
bash-3.2$ cat > test.js << 'END'
> console.log("hi");
> END
bash-3.2$ cat > test.py << 'END'
> # комментарий
> print("hi")
> END
bash-3.2$ cat > findComments
^C
bash-3.2$ cat findComments
bash-3.2$ nano findComments
for file in $(find . -name '*.c' -o -name '*.js'); do
	if head -n 1 "$file" | grep -q '^//'; then
		echo "In file $file first line is a comment"
	fi
	if head -n 1 "$file" | grep -q '^/\*'; then
                echo "In file $file first line is a comment"
        fi
done
for file in $(find . -name '*.py'); do
        if head -n 1 "$file" | grep -q '^#'; then
                echo "In file $file first line is a comment"
        fi
done
bash-3.2$ chmod +x findComments
bash-3.2$ ./findComments
In file ./test.c first line is a comment
In file ./test.py first line is a comment
```

## Задание 7
```
bash-3.2$ cd /tmp
bash-3.2$ echo "hello" > a.txt
bash-3.2$ echo "hello" > b.txt
bash-3.2$ echo "hello" > c.txt
bash-3.2$ echo "world" > d.txt
bash-3.2$ mkdir sub
bash-3.2$ echo "hello" > sub/e.txt
bash-3.2$ dups=$(for file in $(find . -type f); do
>     echo "$(md5 -q "$file") $file"
> done | sort | awk '{print $1}' | uniq -d)
bash-3.2$ 
bash-3.2$ for file in $(find . -type f); do
>     h=$(md5 -q "$file")
>     if echo "$dups" | grep -q "$h"; then
>         echo "$file"
>     fi
> done
./c.txt
./b.txt
./sub/e.txt
./a.txt
```

## Задание 8
```
bash-3.2$ cat > archiever << 'END'
> END
bash-3.2$ nano archiever
#!/bin/bash
if [ -z "$1" ]; then
echo "The path is not declared"
exit 1
fi
if [ -z "$2" ]; then
echo "The extension is not declared"
exit 1
fi
if [ ! -e "$1" ]; then
echo "There is no such path"
exit 1
fi
cd $1
find . -name "*$2" > /tmp/filelist.txt
if [ ! -s /tmp/filelist.txt ]; then
echo "No files found with extension '$2'"    
exit 1
fi
tar -cf archive.tar -T /tmp/filelist.txt
rm /tmp/filelist.txt
echo "The archive is ready"
bash-3.2$ ls
a.txt		b.txt		d.txt		filelist.txt	powerlog	sub		test.js
archiever	c.txt		dumps		findComments	steam.pipe	test.c		test.py
bash-3.2$ ./archiever /private/tmp .txt
The archive is ready
```

## Задание 9
```
bash-3.2$ cat > tabs << 'END'
> END
bash-3.2$ nano tabs
if [ -z "$1" ]; then
echo "The input file is not declared"
exit 1
fi
if [ -z "$2" ]; then
echo "The ouput file is not declared"
exit 1 
fi
if [ ! -e "$1" ]; then
echo "There is no such file(input)"
exit 1
fi
sed "s/    /  '/g" "$1" > "$2"
echo "Success"
bash-3.2$ cat > in.txt << 'END'
> Hello    world    MIREA    lol
> Test    text
> END
bash-3.2$ cat in.txt
Hello    world    MIREA    lol
Test    text
bash-3.2$ chmod +x tabs
bash-3.2$ ./tabs in.txt out.txt
Success
bash-3.2$ cat out.txt
Hello	world	MIREA	lol
Test	text
bash-3.2$ cat -et out.txt
Hello^Iworld^IMIREA^Ilol$
Test^Itext$
```


## Задание 10
```
bash-3.2$ cat > empties << 'END'
> END
bash-3.2$ nano empties
#!/bin/bash
if [ -z "$1" ]; then
echo "The path is not declared"
exit 1
fi
if [ ! -e "$1" ]; then
echo "There is no such path"
exit 1
fi
find "$1" -type f -empty
bash-3.2$ chmod +x empties
bash-3.2$ cat > empty1.txt << 'END'
> END
bash-3.2$ cat > empty2.txt << 'END'
> END
bash-3.2$ ./empties /private/tmp
/private/tmp/empty2.txt
/private/tmp/empty1.txt
```
