package com.oracle.msa.sample.clientrating.customerservice;

import javax.ejb.EJB;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.core.MediaType;

@Path("/customers")
public class CustomerService {
    @EJB
    private CustomerBean customerBean;

    @EJB
    private RatingServiceProxy ratingService;

    @GET
    @Produces(MediaType.TEXT_PLAIN)
    public String getCustomersRating() {
        StringBuilder builder = new StringBuilder();
        for (Customer customer : customerBean.getCustomers()) {
            builder.append(customer.getName()).append('\t').append(ratingService.getRating(customer.getId())).append('\n');
        }
        return builder.toString();
    }
}
