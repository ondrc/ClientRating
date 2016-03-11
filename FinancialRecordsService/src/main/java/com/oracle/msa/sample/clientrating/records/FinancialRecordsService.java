package com.oracle.msa.sample.clientrating.records;

import javax.ejb.EJB;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/records")
public class FinancialRecordsService {
    @EJB
    private FinancialRecordsProxy financialRecords;

    @GET
    @Path("{customerId}/")
    @Produces(MediaType.APPLICATION_JSON)
    public String getHistoryRating(@PathParam("customerId") Integer customerId) {
        return financialRecords.getHistoryRating(customerId).name();
    }
}
