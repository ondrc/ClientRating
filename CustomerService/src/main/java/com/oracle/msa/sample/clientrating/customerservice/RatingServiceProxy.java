package com.oracle.msa.sample.clientrating.customerservice;

import javax.annotation.PostConstruct;
import javax.annotation.Resource;
import javax.ejb.Stateless;
import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.MediaType;

@Stateless
public class RatingServiceProxy {
    private WebTarget target;

    @Resource(name = "ratingServiceURL")
    private String ratingServiceURL;

    @PostConstruct
    private void init() {
        Client client = ClientBuilder.newClient();
        target = client.target(ratingServiceURL);
    }

    public Integer getRating(Integer customerId) {
        return Integer.valueOf(target.resolveTemplate("customerId", customerId).request(MediaType.APPLICATION_JSON_TYPE).get(String.class));
    }
}
