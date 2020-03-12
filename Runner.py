import csv
import Solver
import ImprovedSolver


def main():

    file = open('basicAgentPerformance.csv', 'w+')

    with open('basicAgentPerformance.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Trial No.", "Mine Density", "Average Final Score"])

        trialNumber = 1
        dimension = 22 #closest to dimension of HARD Minecraft board
