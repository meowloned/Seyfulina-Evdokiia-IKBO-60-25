
# Практическая 2

## Задание 1
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

## Задание 2
```
bash-3.2$ node --version
v24.21.0
bash-3.2$ npm --version
11.19.0
bash-3.2$ mkdir express-practice
bash-3.2$ cd express-practice
bash-3.2$ npm init -y
Wrote to /Users/meowloned/express-practice/package.json:

{
  "name": "express-practice",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "type": "commonjs"
}


bash-3.2$ npm install express
bash-3.2$ cat node_modules/express/package.json
{
  "name": "express",
  "description": "Fast, unopinionated, minimalist web framework",
  "version": "5.2.1",
  ...
  "dependencies": {
    "accepts": "^2.0.0",
    "body-parser": "^2.2.1",
    "content-disposition": "^1.0.0",
    "content-type": "^1.0.5",
    "cookie": "^0.7.1",
    "cookie-signature": "^1.2.1",
    "debug": "^4.4.0",
    "depd": "^2.0.0",
    "encodeurl": "^2.0.0",
    "escape-html": "^1.0.3",
    "etag": "^1.8.1",
    "finalhandler": "^2.1.0",
    "fresh": "^2.0.0",
    "http-errors": "^2.0.0",
    "merge-descriptors": "^2.0.0",
    "mime-types": "^3.0.0",
    "on-finished": "^2.4.1",
    "once": "^1.4.0",
    "parseurl": "^1.3.3",
    "proxy-addr": "^2.0.7",
    "qs": "^6.14.0",
    "range-parser": "^1.2.1",
    "router": "^2.2.0",
    "send": "^1.1.0",
    "serve-static": "^2.2.0",
    "statuses": "^2.0.1",
    "type-is": "^2.0.1",
    "vary": "^1.1.2"
  },
  ...
  "engines": {
    "node": ">= 18"
  },
...

```
Как получить пакет без менеджера пакетов, прямо из репозитория?
```
git clone https://github.com/expressjs/express.git
```

## Задание 3
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
