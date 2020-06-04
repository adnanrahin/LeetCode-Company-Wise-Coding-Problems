package Adobe.Unique_Email_Addresses;

import java.util.HashSet;
import java.util.Set;

public class Main {

    public static void main(String args[]) {

        System.out.println(numUniqueEmails(new String[]{"test.email+alex@leetcode.com",
                "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"}));

    }

    public static int numUniqueEmails(String[] emails) {

        Set<String> set = new HashSet<>();

        for (String string : emails) {

            int i = string.indexOf('@');
            String address = string.substring(0, i);
            String domain = string.substring(i);

            if (address.contains("+")) {
                address = address.substring(0, string.indexOf('+'));
            }

            address = address.replaceAll("\\.", "");

            set.add(address + domain);

        }

        return set.size();

    }

}
