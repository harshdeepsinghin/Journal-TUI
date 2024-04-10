import argparse
import time
from notifypy import Notify

## Pomodoro Timer Function
def pomodoro_timer(WORK=25, BREAK=5, CYCLES=8):
    notification = Notify()
    notification.title = "Pomodoro Timer"
    print("⏰  POMODORO STARTED  ⏰")

    for i in range(CYCLES):
        print(f"\nROUND {i+1}...")
        notification.message = f"Work Time ({WORK}m) Started!"
        notification.audio = "/Users/ektara/gitrepos/StudyToolkit/work_sound.wav"
        notification.send()

        print(f"\n⏰  WORK TIME  ⏰  ROUND {i+1}  ⏰")
        print("(Pres `Ctrl + C` to stop)\n")
        SECONDS=WORK*60
        while SECONDS:
            MIN, SEC = divmod(SECONDS,60)
            timer = '\t{:02d}:{:02d}'.format(MIN,SEC)
            print(timer, end='\r')
            time.sleep(1)
            SECONDS-=1


        print(f"\n\n⌛  BREAK TIME  ⌛  ROUND {i+1}  ⌛")
        print("(Pres `Ctrl + C` to stop)\n")

        notification.message = f"Break ({BREAK}m) Time!"
        notification.audio = "/Users/ektara/gitrepos/StudyToolkit/break_sound.wav"
        notification.send()

        if ( (i+1) % 4 == 0 ):      # For bigger break after 4 rounds
            SECONDS = BREAK*3*60
        else:
            SECONDS = BREAK*60

        while SECONDS:
            MIN, SEC = divmod(SECONDS,60)
            timer = '\t{:02d}:{:02d}'.format(MIN,SEC)
            print(timer, end='\r')
            time.sleep(1)
            SECONDS-=1

    print("\n⏰  POMODORO ENDED  ⏰")
    return 0

def main():
    parser = argparse.ArgumentParser(description="A Pomodoro Timer written in Python")
    parser.add_argument('-w', '--work-time', type=int, default=25, help='Minutes for work (default: 25)')
    parser.add_argument('-b', '--break-time', type=int, default=5, help='Minutes for break (default: 5)')
    parser.add_argument('-c', '-r', '--cycles', '--rounds', type=int, default=8, help='Number of cycles/rounds (default: 8)')
    args = parser.parse_args()
    pomodoro_timer(args.work_time, args.break_time, args.cycles)

if __name__ == '__main__':
    main()
