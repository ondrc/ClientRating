package com.oracle.msa.sample.clientrating.ratingservice;

import javax.annotation.PostConstruct;
import javax.annotation.Resource;
import javax.ejb.Stateless;
import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.MediaType;

@Stateless
public class BlacklistServiceProxy {
    private WebTarget target;

    @Resource(name = "blacklistServiceURL")
    private String blacklistServiceURL;

    @PostConstruct
    private void init() {
        Client client = ClientBuilder.newClient();
        target = client.target(blacklistServiceURL);
    }

    public CustomerStatus getCustomerStatus(Integer customerId) {
        return CustomerStatus.valueOf(target.resolveTemplate("customerId", customerId).request(MediaType.APPLICATION_JSON_TYPE).get(String.class));
    }
}
