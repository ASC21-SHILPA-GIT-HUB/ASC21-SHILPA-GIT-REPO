package com.task4.demo.storage;

public class StorageFactory {
    public static Storage getStorage() {
        return new StorageImpl();
    }
}
