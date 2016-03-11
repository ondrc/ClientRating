package com.oracle.msa.sample.clientrating.blacklistservice;

import javax.ejb.EJB;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/blacklist")
public class BlacklistService {
    @EJB
    private BlacklistBean blacklistBean;

    @GET
    @Path("{customerId}/")
    @Produces(MediaType.APPLICATION_JSON)
    public String getCustomerStatus(@PathParam("customerId") Integer customerId) {
        return blacklistBean.getCustomerStatus(customerId).name();
    }
}
