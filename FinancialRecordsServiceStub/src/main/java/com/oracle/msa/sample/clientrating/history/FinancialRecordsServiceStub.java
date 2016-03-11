package com.oracle.msa.sample.clientrating.history;

import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/history")
public class FinancialRecordsServiceStub {
    @GET
    @Path("{customerId}/")
    @Produces(MediaType.APPLICATION_JSON)
    public String getHistoryRating(@PathParam("customerId") Integer customerId) {
        return FinancialHistoryRating.values()[(int)Math.floor(Math.random() * FinancialHistoryRating.values().length)].name();
    }
}
