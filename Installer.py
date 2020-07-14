# Quick installer for FRC 2020 
# Made by: Ryan Bellknapp 
# Published: 7/13/20
#
# I did not write these following products 
# and I am not taking credit for said programs,
# this is simply a compilation for an easier download.
#
# WARNING: At the time of installation, 
# not all programs might be up to date!

import webbrowser
import time

print("")
print("----------------------------------------")
print(" Ryan Bellknapp is not the owner of     ")
print(" these products*.  I accept the terms of")
print(" services for each and every product    ")
print(" listed below.                          ")
print("                                        ")
print(" *Excluding Github FRC Code.            ")
print("----------------------------------------")

time.sleep(2)

print("")
print("I understand and agree to these terms.")
print("")
print("(enter) = YES ")

x = input("")

if(x != ""):
    print("")
    print("Installation Canceled.")
    quit()



# AUTOMATIC DOWNLOADS:

# Visual Studio Code 1.470
webbrowser.open("https://az764295.vo.msecnd.net/stable/d5e9aa0227e057a60c82568bf31c04730dc15dcd/VSCodeUserSetup-x64-1.47.0.exe")

time.sleep(.25)

# Gradle 6.5.1
webbrowser.open("https://downloads.gradle-dn.com/distributions/gradle-6.5.1-all.zip")

time.sleep(.25)

# Code From 2020 FRC Season:
webbrowser.open("https://codeload.github.com/ryanb44363/3-10-20/zip/master")

time.sleep(.25)



# MANUAL DOWNLOADS:

# Java (JRE)
webbrowser.open("https://www.java.com/en/download/win10.jsp")

# Java (JDK)
webbrowser.open("https://www.oracle.com/java/technologies/javase-jdk11-downloads.html")

# Git 2.27.0
webbrowser.open("https://gitforwindows.org/")


print("Would you like to see the homepages for the automatic downloads?")

print("")

x = input("(enter) = YES ")

if(x != ""):
    print("")
    print("Program Complete.")
    quit()

# Visual Studio Code 1.470
webbrowser.open("https://code.visualstudio.com/")

time.sleep(.25)

# Gradle 6.5.1
webbrowser.open("https://gradle.org/releases/")

time.sleep(.25)

# Code From 2020 FRC Season:
webbrowser.open("https://github.com/ryanb44363/3-10-20")

time.sleep(.25)

print("")
print("Program Complete.")

quit()
