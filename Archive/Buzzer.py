# Author: Hugo P. (Taken from http://www.linuxcircle.com/2015/04/12/how-to-play-piezo-buzzer-tunes-on-raspberry-pi-gpio-with-pwm/)
# Project: https://github.com/HugoCMU/SolarTree
# Description: Buzzer Class contains methods for playing tunes through the
# Piezzo buzzer


from brain import ser, params, pins
import RPi.GPIO as GPIO  # import the GPIO library
import time  # import the time library


class Buzzer(object):

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.buzzer_pin = pins.p['BUZZER']
        GPIO.setup(self.buzzer_pin, GPIO.IN)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)
        print("Buzzer ready")

    def __del__(self):
        class_name = self.__class__.__name__
        print (class_name, "... done")

    def buzz(self, pitch, duration):  # Create buzz given a pitch and duration

        if(pitch == 0):
            time.sleep(duration)
            return
        # in physics, the period (sec/cyc) is the inverse of the frequency
        # (cyc/sec)
        period = 1.0 / pitch
        delay = period / 2  # calcuate the time for half of the wave
        # the number of waves to produce is the duration times the frequency
        cycles = int(duration * pitch)

        # Loop through cycles
        for i in range(cycles):
            GPIO.output(self.buzzer_pin, True)  # set pin 18 to high
            time.sleep(delay)  # wait with pin 18 high
            GPIO.output(self.buzzer_pin, False)  # set pin 18 to low
            time.sleep(delay)  # wait with pin 18 low

    def play(self, tune):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)

        # Define counter variable for repetitive buzzer tunes
        x = 0

        print("Playing tune ", tune)
        if(tune == 1):
            pitches = [262, 784, 880, 988, 1047]
            duration = 0.1
            for p in pitches:
                self.buzz(p, duration)
                time.sleep(duration * 0.5)
            for p in reversed(pitches):
                self.buzz(p, duration)
                time.sleep(duration * 0.5)

        elif(tune == 2):
            pitches = [262, 330, 392, 523, 1047]
            duration = [0.2, 0.2, 0.2, 0.2, 0.2, 0, 5]
            for p in pitches:
                self.buzz(p, duration[x])
                time.sleep(duration[x] * 0.5)
                x += 1

        elif(tune == 3):
            pitches = [
                392, 294, 0, 392, 294, 0, 392, 0, 392, 392, 392, 0, 1047, 262]
            duration = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2,
                        0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.8, 0.4]
            for p in pitches:
                self.buzz(p, duration[x])
                time.sleep(duration[x] * 0.5)
                x += 1

        elif(tune == 4):
            pitches = [1047, 988, 659]
            duration = [0.1, 0.1, 0.2]
            for p in pitches:
                self.buzz(p, duration[x])
                time.sleep(duration[x] * 0.5)
                x += 1

        elif(tune == 5):
            pitches = [1047, 988, 523]
            duration = [0.1, 0.1, 0.2]
            for p in pitches:
                self.buzz(p, duration[x])
                time.sleep(duration[x] * 0.5)
                x += 1

        GPIO.setup(self.buzzer_pin, GPIO.IN)

if __name__ == "__main__":
    a = input("Enter Tune number 1-5:")
    buzzer = Buzzer()
    buzzer.play(int(a))
