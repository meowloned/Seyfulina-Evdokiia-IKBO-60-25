#Практическая 2

##Задание 1
```
bash-3.2$ python3 --version
Python 3.13.3
bash-3.2$ pip3 --version
pip 25.0.1 from /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/pip (python 3.13)
bash-3.2$ pip3 show matplotlib
WARNING: Package(s) not found: matplotlib
bash-3.2$ pip3 install matplotlib
bash-3.2$ pip3 show matplotlib
...
Location: /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages
Requires: contourpy, cycler, fonttools, kiwisolver, numpy, packaging, pillow, pyparsing, python-dateutil
Required-by: 
bash-3.2$ cd /Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages
bash-3.2$ ls | grep matplotlib
matplotlib
matplotlib-3.11.2.dist-info
bash-3.2$ cd matplotlib-3.11.2.dist-info
bash-3.2$ ls
INSTALLER	LICENSE		METADATA	RECORD		REQUESTED	WHEEL
bash-3.2$ head -40 METADATA
Metadata-Version: 2.1
Name: matplotlib
Version: 3.11.2
Summary: Python plotting package
Author: John D. Hunter, Michael Droettboom
Author-Email: Unknown <matplotlib-users@python.org>
License: License agreement for matplotlib versions 1.3.0 and later
...
bash-3.2$ grep "^Requires-Dist" METADATA
Requires-Dist: contourpy>=1.0.1
Requires-Dist: cycler>=0.10
Requires-Dist: fonttools>=4.28.2
Requires-Dist: kiwisolver>=1.3.1
Requires-Dist: numpy>=1.25
Requires-Dist: packaging>=20.0
Requires-Dist: pillow>=9
Requires-Dist: pyparsing>=3
Requires-Dist: python-dateutil>=2.7
bash-3.2$ grep "^Requires-Python" METADATA
Requires-Python: >=3.11
```
Как получить пакет без менеджера пакетов, прямо из репозитория?
```
git clone https://github.com/matplotlib/matplotlib.git
```

##Задание 2
```

```

##Задание 2
```

```

##Задание 4
```

```

##Задание 5
```

```

##Задание 6
```

```

##Задание 7
```

```
