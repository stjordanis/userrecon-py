## userrecon-py
Find usernames in social networks.

---

#### Installation

1. Install dependencies (Debian/Ubuntu):
```
sudo apt install python3 python3-pip
```

2. Install with `pip3`:
```
sudo -H pip3 install git+https://github.com/decoxviii/userrecon-py.git
userrecon-py --help
```

---

#### Building from Source

Clone this repository, and:
```
git clone https://github.com/decoxviii/userrecon-py.git ; cd userrecon-py
sudo -H pip3 install -r requirements.txt
python3 setup.py build
sudo python3 setup.py install
```

---

#### Update

To update this tool to the latest version, run:
```
sudo -H pip3 install git+https://github.com/decoxviii/userrecon-py.git --upgrade
userrecon-py --version
```

---

#### Usage
Start by printing the available actions by running `userrecon-py --help`. Then you can perform the following tests:

```
userrecon-py target decoxviii -o test1
```

---

#### Thanks

This program is inspired by the projects:
+ [userrecon](https://github.com/thelinuxchoice/userrecon) by: thelinuxchoice

---

**decoxviii**

**[MIT](https://github.com/decoxviii/userrecon-py/blob/master/LICENSE)**

