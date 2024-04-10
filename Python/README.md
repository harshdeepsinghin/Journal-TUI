# Pomodoro Timer - Python

### Introduction
A Pomodoro Timer written in Python.

### Installation

```bash
git clone https://github.com/harshdeepsinghin/Pomodoro-Timer.git
cd Pomodoro-Timer/Python
```

Setup a virtual environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies.

```bash
pip3 install -r requirements.txt
```

Run the program

```bash
python3 Pomodoro-Timer.py
```

Customized timer

```bash
python3 Pomodoro-Timer.py --work-time 30 --break-time 10 --cycles 4
```

Help Menu

```bash
python3 Pomodoro-Timer.py --help
```

```
usage: Pomodoro-Timer.py [-h] [-w WORK_TIME] [-b BREAK_TIME] [-c CYCLES]

A Pomodoro Timer written in Python

optional arguments:
  -h, --help            show this help message and exit
  -w WORK_TIME, --work-time WORK_TIME
                        Minutes for work (default: 25)
  -b BREAK_TIME, --break-time BREAK_TIME
                        Minutes for break (default: 5)
  -c CYCLES, -r CYCLES, --cycles CYCLES, --rounds CYCLES
                        Number of cycles/rounds (default: 8)
```
