# ClientRating
## Microservices minimal proof of concept

This sample application is meant to demonstrate the development of a Java EE based Microservices application and deployment on WebLogic application server. For that purpose we have created a very minimalistic application demonstrating the scenario of a number of services cooperating in order to calculate a banking customer's rating for the purpose of risk assessment. 

The application is composed of four services. Customer service is the service initiating the call, asking for the rating of all customers in the system. It exposes a REST endpoint through JAX-RS, returning the result in plain text. The EJB implementing the business functionality performs a JPA query to retrieve all customers and performs a REST call to RatingService to retrieve the customer rating. 

RatingService initially performs a REST call to BlacklistService to verify that the customer has not been blacklisted. The latter performs a JPA query to its own database and returns the status for the customers who are stored there (a subset of the customers requested). Then a call to FinancialRecordsService is performed in order to retrieve the customer's financial history rating from a public authority. A stub is used in the example application to represent this remote call. 

This fork of original [ClientRating by Petros Splinakis](https://github.com/psplinakis/ClientRating) is intended to adapt this application to containerized deployment. The goal is to create docker images for each service in order to start the containers on AWS ECS. As we wish to be able to fit into the free tier of AWS, we need to change application server to something smaller than Weblogic. The current plan is to adapt it to TomEE, which should, in theory, mean just to swap JPA provider in persistence.xml.

## TODO

