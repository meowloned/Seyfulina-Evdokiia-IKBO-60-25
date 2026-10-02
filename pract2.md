
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
digraph matplotlib_dependencies {
    matplotlib -> contourpy;
    matplotlib -> cycler;
    matplotlib -> fonttools;
    matplotlib -> kiwisolver;
    matplotlib -> numpy;
    matplotlib -> packaging;
    matplotlib -> pillow;
    matplotlib -> pyparsing;
    matplotlib -> "python-dateutil";
}
```

<img width="735" height="148" alt="Снимок экрана — 2026-10-02 в 16 24 49" src="https://github.com/user-attachments/assets/2dfb856d-d2fb-464e-a178-99ac0b86f3a9" />


```
digraph express_dependencies {
    layout=twopi;
    root=express;
    ranksep=2;
    overlap=false;

    node [
        shape=box,
        fontsize=11
    ];

    express [
        shape=ellipse,
        fontsize=16
    ];

    express -> accepts;
    express -> "body-parser";
    express -> "content-disposition";
    express -> "content-type";
    express -> cookie;
    express -> "cookie-signature";
    express -> debug;
    express -> depd;
    express -> encodeurl;
    express -> "escape-html";
    express -> etag;
    express -> finalhandler;
    express -> fresh;
    express -> "http-errors";
    express -> "merge-descriptors";
    express -> "mime-types";
    express -> "on-finished";
    express -> once;
    express -> parseurl;
    express -> "proxy-addr";
    express -> qs;
    express -> "range-parser";
    express -> router;
    express -> send;
    express -> "serve-static";
    express -> statuses;
    express -> "type-is";
    express -> vary;
}
```
 
<img width="735" height="620" alt="Снимок экрана — 2026-10-02 в 16 46 47" src="https://github.com/user-attachments/assets/74b078ba-07ae-4f66-beb6-5d14ff1e8f70" />


## Задание 4
```
include "alldifferent.mzn";
var 0..9: a;
var 0..9: b;
var 0..9: c;
var 0..9: d;
var 0..9: e;
var 0..9: f;

constraint a + b + c = d + e + f;

constraint all_different([a, b, c, d, e, f]);

solve minimize a + b + c;

￼
Running untitled_model.mzn
103msec

a = 8;
b = 1;
c = 0;
d = 4;
e = 3;
f = 2;
_objective = 9;
----------
a = 6;
b = 2;
c = 0;
d = 4;
e = 3;
f = 1;
_objective = 8;
----------
==========
Finished in 103msec.
```


# #Задание 5
```
set of int: menu_vers = {10, 11, 12, 13, 14, 15};
set of int: dropdown_vers = {18, 20, 21, 22, 23};
set of int: icons_vers = {10, 20};

var menu_vers: menu;
var dropdown_vers: dropdown;
var icons_vers: icons;

constraint menu >= 10;

constraint icons = 10;

constraint
    (menu >= 11) ->
    (dropdown >= 20);

constraint
    (menu = 10) ->
    (dropdown = 18);

constraint
    (dropdown >= 20) ->
    (icons = 20);


solve satisfy;


￼
Running untitled_model.mzn
95msec

menu = 10;
dropdown = 18;
icons = 10;
----------
Finished in 95msec.
```


## Задание 6
```
set of int: foo_vers = {10, 11};
set of int: left_vers = {0, 10};
set of int: right_vers = {0, 10};
set of int: target_vers = {10, 20};
set of int: shared_vers = {0, 10, 20};

var foo_vers: foo;
var left_vers: left;
var right_vers: right;
var target_vers: target;
var shared_vers: shared;

constraint foo >= 10 /\ foo < 20;

constraint target  >= 20 /\ target < 30;

constraint
    (foo = 11) ->
    (left >= 10 /\ left < 20 /\ right >=10 /\ right < 20);
    
constraint
    (left = 10) ->
    (shared >= 10);
    
constraint
    (right = 10) ->
    (shared < 20);

constraint
    (shared = 10) ->
    (target >= 10 /\ target < 20);

solve satisfy;


￼
Running untitled_model.mzn
90msec

foo = 10;
left = 0;
right = 0;
target = 20;
shared = 0;
----------
Finished in 90msec.
```


## Задание 7
```

```
