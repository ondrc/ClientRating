# ClientRating
## Microservices minimal proof of concept

This sample application is meant to demonstrate the development of a Java EE based Microservices application and deployment on WebLogic application server. For that purpose we have created a very minimalistic application demonstrating the scenario of a number of services cooperating in order to calculate a banking customer's rating for the purpose of risk assessment. 

The application is composed of four services. Customer service is the service initiating the call, asking for the rating of all customers in the system. It exposes a REST endpoint through JAX-RS using Jersey and MOXy, returning the result in plain text. The EJB implementing the business functionality performs a JPA query to retrieve all customers and performs a REST call to RatingService to retrieve the customer rating. 

RatingService initially performs a REST call to BlacklistService to verify that the customer has not been blacklisted. The latter performs a JPA query to its own database and returns the status for the customers who are stored there (a subset of the customers requested). Then a call to FinancialRecordsService is performed in order to retrieve the customer's financial history rating from a public authority. A stub is used in the example application to represent this remote call. 

Configuration of the REST endpoints for each service is performed using WebLogic server's Deployment Plans. This feature will be detrimental in implementing the second scenario, which is migrating one service to a new dynamic cluster for the purpose of scaling. For that purpose we are also using HttpClusterServlet as a load balancer.

## Requirements
The application can be built and deployed to a single WebLogic domain using domain partitioning for services separation. Prerequisites for running this example is having a Unix based operating system with [JDK 8](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) and [Maven](https://maven.apache.org/download.cgi?Preferred=ftp://mirror.reverse.net/pub/apache/) installed, and a [WebLogic 12.2.1 Fusion Middleware Infrastructure](http://www.oracle.com/technetwork/middleware/weblogic/downloads/wls-main-097127.html) installation. 

The following variables can be used to control the setup:

- **ORACLE_HOME** (default: /opt/wls/Oracle_Home)
- **WL_HOME** (default: $ORACLE_HOME/wlserver)
- **DOMAIN_HOME** (default: /opt/wls)
- **DOMAIN_NAME** (default: domain)

## Executing simple scenario
Executing bash script **execute_single_server.sh** will build the example, create and configure the WebLogic domain, deploy the example into partitions, display the simple text output of CustomerService and shut down the domain. 

## Executing clustered domain scenario
Executing bash script **execute_dynamic_cluster_step_1.sh** will build the example, create the Weblogic domain, configure the dynamic cluster and start the Admin server.

The following manual steps will need to be performed in order to start up the cluster servers:

- $DOMAIN_HOME/$DOMAIN_NAME/bin/startManagedWeblogic.sh DynamicCluster-0-LoadBalancer
- $DOMAIN_HOME/$DOMAIN_NAME/bin/startManagedWeblogic.sh DynamicCluster-0-Server-1
- $DOMAIN_HOME/$DOMAIN_NAME/bin/startManagedWeblogic.sh DynamicCluster-0-Server-2

In every case the Admin server user and password will need to be provided (default: weblogic/welcome1)

Finally, executing bash script **execute_dynamic_cluster_step_2.sh** will deploy the example, display the simple text output of CustomerService and shut down the domain.
