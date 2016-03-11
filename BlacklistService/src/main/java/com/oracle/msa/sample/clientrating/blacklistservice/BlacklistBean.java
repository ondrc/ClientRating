package com.oracle.msa.sample.clientrating.blacklistservice;

import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.persistence.TypedQuery;
import java.util.List;

@Stateless
public class BlacklistBean {
    @PersistenceContext
    private EntityManager entityManager;

    public Customer.Status getCustomerStatus(Integer customerId) {
        TypedQuery<Customer> query = entityManager.createNamedQuery("getCustomer", Customer.class);
        query.setParameter("customerId", customerId);
        List<Customer> list = query.getResultList();
        return list.isEmpty()? Customer.Status.WHITELISTED: list.iterator().next().getStatus();
    }
}
