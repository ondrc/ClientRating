package com.oracle.msa.sample.clientrating.ratingservice;

import javax.ejb.EJB;
import javax.ws.rs.GET;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.Path;
import javax.ws.rs.core.MediaType;

@Path("/rating")
public class RatingService {
    @EJB
    BlacklistServiceProxy blacklistService;

    @EJB
    FinancialRecordsServiceProxy financialRecordsService;

    @GET
    @Path("{customerId}/")
    @Produces(MediaType.APPLICATION_JSON)
    public String getClientRating(@PathParam("customerId") Integer customerId) {
        CustomerStatus customerStatus = blacklistService.getCustomerStatus(customerId);
        if(customerStatus == CustomerStatus.BLACKLISTED) {
            return "0";
        }
        else {
            return String.valueOf(FinancialHistoryRating.values().length - financialRecordsService.getHistoryRating(customerId).ordinal());
        }
    }
}
