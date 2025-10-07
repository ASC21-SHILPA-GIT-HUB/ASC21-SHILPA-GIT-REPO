package com.task4.demo.storage;

import com.task4.demo.entity.Employee;

public interface Storage {
    void addEmployee(Employee e);
    Employee getEmployee(int empno);
}
