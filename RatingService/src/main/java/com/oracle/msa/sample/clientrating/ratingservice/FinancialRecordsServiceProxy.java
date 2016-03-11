package com.oracle.msa.sample.clientrating.ratingservice;

import javax.annotation.PostConstruct;
import javax.annotation.Resource;
import javax.ejb.Stateless;
import javax.ws.rs.client.Client;
import javax.ws.rs.client.ClientBuilder;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.MediaType;

@Stateless
public class FinancialRecordsServiceProxy {
    private WebTarget target;

    @Resource(name = "recordsServiceURL")
    private String recordsServiceURL;

    @PostConstruct
    private void init() {
        Client client = ClientBuilder.newClient();
        target = client.target(recordsServiceURL);
    }

    public FinancialHistoryRating getHistoryRating(Integer customerId) {
        return FinancialHistoryRating.valueOf(target.resolveTemplate("customerId", customerId).request(MediaType.APPLICATION_JSON_TYPE).get(String.class));
    }
}
