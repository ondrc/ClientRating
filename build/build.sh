#!/bin/sh

mvn -f ../pom.xml clean install
mvn -f ../CustomerService/pom.xml war:war
mvn -f ../RatingService/pom.xml war:war
mvn -f ../BlacklistService/pom.xml war:war
mvn -f ../FinancialRecordsService/pom.xml war:war
mvn -f ../FinancialRecordsServiceStub/pom.xml war:war