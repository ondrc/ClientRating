package com.oracle.msa.sample.clientrating.customerservice;

import javax.ejb.Stateless;
import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import java.util.List;

@Stateless
public class CustomerBean {
    @PersistenceContext
    private EntityManager entityManager;

    public List<Customer> getCustomers() {
        return entityManager.createNamedQuery("getCustomers", Customer.class).getResultList();
    }
}
