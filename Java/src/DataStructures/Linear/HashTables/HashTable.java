package DataStructures.Linear.HashTables;

import java.util.HashMap;
import java.util.Set;

public class HashTable {

    public static void main(String[] args) {
        HashMap<String, String> hm = new HashMap<>();
        hm.put("Name", "James");
        hm.put("Head", "Mike");
        hm.put("Nope", "John");

        Set<String> set = hm.keySet();
        for (String i : set) {

            System.out.println(hm.get(i));
        }
    }
}
