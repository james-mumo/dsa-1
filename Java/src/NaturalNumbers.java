import java.math.BigInteger;

public class NaturalNumbers {
    static int SumNaturalNo() {
        int sum = 0;
        BigInteger i = BigInteger.ONE;
        BigInteger myVar = new BigInteger("100000000000");

        while (i.compareTo(myVar) <= 0) {
            sum += i.intValue();
            i = i.add(BigInteger.ONE);
        }

        return sum;
    }

    public static int SunNat2(int n){
        return n*(n+1)/2;
    }

    public static void main(String[] args) {
//        System.out.println(SumNaturalNo());
        System.out.println(SunNat2(1000000000));
    }
}
