package Adobe.Jewels_And_Stones;

import java.util.HashSet;
import java.util.Set;

public class Main {

    public static void main(String args[]) {

    }

    public static int numJewelsInStones(String J, String S) {

        int numberOfJewels = 0;

        Set<Character> set = new HashSet<>();

        for (int i = 0; i < J.length(); i++)
            set.add(J.charAt(i));

        for (int i = 0; i < S.length(); i++)
            if (set.contains(S.charAt(i)))
                numberOfJewels++;

        return numberOfJewels;

    }

}
