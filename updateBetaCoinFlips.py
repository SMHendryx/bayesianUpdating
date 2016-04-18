__author__ = 'seanhendryx'
# Aurthored by Sean Hendryx
# Script built to run on Python version 2.7.11
# References:
# Probabilistic Graphical Models by Koller and Friedman
# Python documentation 2.7.11 https://docs.python.org/2/



import math
import numpy
import matplotlib.pyplot as plt
import scipy
from scipy import special



def main():
    """
    Main function
    :return:none, visualizes the updating of a beta distribution with data, using the classic example of flips of a coin
    """
    numberOfSamples = raw_input("How many coins would you like to flip?")
    print(numberOfSamples, " samples")
    xValues = numpy.linspace(0.0, 1.0, numberOfSamples)

    alpha = 5
    beta = 5
    print ("alpha={} and beta={}".format(alpha, beta))

    #UPDATE PRIOR WITH DATA:
    count = 0
    for i in range(0, 6):

        numberOfHeads = count
        numberOfHeads = float(numberOfHeads)

        numberOfTails = count
        numberOfTails = float(numberOfTails)
        gamma = alpha + numberOfHeads
        delta = beta + numberOfTails
        px = betaDistribution(xValues, gamma, delta)
        print ("Gamma = {}, delta = {}, number of heads = number of tails = {}".format(gamma, delta, count))
        label = "beta({},{})".format(gamma, delta)
        print(label)
        plt.figure(1)
        line = plt.plot(xValues, px, label = label)
        plt.legend()

        plt.title("Bayesian Updating: Prior and Posterior Beta Distributions")

        plt.xlabel("x")
        plt.ylabel("p(x)")
        count = count + 1
        print(count)



    plt.show()



def betaDistribution(xValues, alpha, beta):
    """
    Computes beta distribution and returns p(x)
    :param xValues: input array of x values within [0,1]
    :param alpha: alpha hyperparameter of beta distribution
    :param beta: beta hyperparameter of beta distribution
    :return:p(x)
    """
    gammaConstant = scipy.special.gamma(alpha+beta)/(scipy.special.gamma(alpha)*scipy.special.gamma(beta))
    #print "gammaConstant: ", gammaConstant
    firstExponent = alpha-1.0
    secondPart = numpy.power(xValues, firstExponent)

    secondExponent = beta-1.0
    thirdPart = numpy.power((1.0 - xValues), secondExponent)

    secondAndThirdParts = numpy.multiply(secondPart, thirdPart)
    px = numpy.multiply(gammaConstant, secondAndThirdParts)

    return px



# Main Function
if __name__ == '__main__':
    main()
