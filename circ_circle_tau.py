#!/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/09/22
# Takes user input for the radius and calculates the circumference of a circle using Tau.

# importing the tau constant in the constants.py file
import constants


def main():
    # title
    print("Circumference of a circle with Tau")
    radius = int(input("Enter the radius here (cm): "))

    # calculation
    circ = radius * constants.TAU

    # display the calculation back to the user
    print("The circumference is = {}cm^2".format(circ))


if __name__ == "__main__":
    main()
