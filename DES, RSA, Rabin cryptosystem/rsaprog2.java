import java.lang.*;
import java.io.*;
import java.util.Scanner;
import java.math.BigInteger;

class RSAcrypto{
  public  BigInteger RSAfind(BigInteger n){
    //pollard p-1 Algorithm to find factors of numbers
    BigInteger p = Pollard(n);
    System.out.println("p :"+p);
    BigInteger one = new BigInteger("1");
    //calculate phi n
    BigInteger q = n.divide(p);
    System.out.println("q :"+q);
    BigInteger cN = p.subtract(one).multiply(q.subtract(one));
    return cN;
  }
  public BigInteger Pollard(BigInteger n){
    //BigInteger bound = new BigInteger("1500");
    int bound = 1500;
    BigInteger a= new BigInteger("2");
    BigInteger d = new BigInteger("0");
    for(int j=2;j<=bound;j++){
      BigInteger temp = a.pow(j);
      a = temp.mod(n);
    }
    d = a.subtract(new BigInteger("1")).gcd(n);
    if(new BigInteger("1").compareTo(d)== -1){
    System.out.println("sucess");
    }else
    {
    System.out.println("failure");
    }
    return d;
  }
  public void encryp(BigInteger NN,String bb,String plain){
    BigInteger b = new BigInteger(bb);
    BigInteger x = new BigInteger(plain);
    BigInteger y = x.modPow(b,NN);
    System.out.print(y);
  }
  public BigInteger findA(String bb,BigInteger rN){
    BigInteger b = new BigInteger(bb);
    BigInteger a = b.modInverse(rN);
    System.out.println("a :"+a);
    System.out.println("b :"+b);
    return a;
  }
  public String decrypt(BigInteger NN,BigInteger a,String cipher){
    //String cipherSubstrings[]=cipher.split("(?<=\\G.{2})");
    BigInteger y = new BigInteger(cipher);
    //cipher odd or even
    BigInteger x = y.modPow(a,NN);
    return x.toString();
  }
  public String valToText(String plainvals){
    String[][] alpha = new String[][]{
{"32","33","34","35","36","37","38","39","40","41"},
{"42","43","44", "45", "46", "47", "48", "49", "50", "51"},
{"52", "53", "54", "55", "56", "57", "58", "59", "60", "61"},
{"62", "63", "64", "65", "66", "67", "68", "69", "70", "71"},
{"72", "73", "74", "75", "76", "77", "78", "79", "80", "81"},
{"82", "83", "84", "85", "86", "87", "88", "89", "90", "91"},
{"92", "93", "94", "95", "96", "97", "98", "99", "100", "101"},
{"102", "103", "104", "105", "106", "107", "108", "109", "110", "111"},
{"112", "113","114","115","116","117","118","119", "120", "121"},
{"122", "123", "124", "125", "126","32" ,"32"  ,"10","13","32"  }
};
    if(plainvals.length()%2!=0){
      plainvals = "0"+plainvals;
    }

    String cipherSubstrings[]=plainvals.split("(?<=\\G.{2})");
    String output = new String();
    for(int i=0;i<cipherSubstrings.length;i++){
      String rowCol[] = cipherSubstrings[i].split("(?<=\\G.{1})");
      int row = Integer.parseInt(rowCol[0]);
      int col = Integer.parseInt(rowCol[1]);
      output += (char)Integer.parseInt(alpha[row][col]);
    }
    return output;
  }
}
class rsaprog2
{
	public static void main(String args[]){
		Scanner input = new Scanner(System.in);
		System.out.println(" ------ RSA cryptosystem ------\n");
    System.out.println(" 1.Encryption\n");
		System.out.println(" 2.Decryption\n");
    System.out.print(" Enter the choice: ");
    int choice = Integer.parseInt(input.next());
    System.out.println("\nNN:");
    BigInteger NN = new BigInteger(input.next());
    System.out.println("\nbb:");
    String bb = input.next();
    RSAcrypto ob = new RSAcrypto();
    if(choice==1){
      try{
        System.out.println("\nEncryption selected\n");
        System.out.println("plain:");
        String plain = input.next();
        ob.encryp(NN,bb,plain);
    }
    catch(Exception e){
      System.out.println("Exception "+e+" catched");
    }
    }else if(choice==2){
      try{
        BigInteger rN = ob.RSAfind(NN);
        System.out.println("phi n: "+rN+"\n");
        BigInteger a = ob.findA(bb,rN);
        System.out.println("Enter file name:");
        File filename = new File(input.next());
        Scanner filereader = new Scanner(filename);
        //create file
  			PrintWriter writer = new PrintWriter("RSADecryptionResult.txt", "UTF-8");
        while(filereader.hasNextLine()){
          String cipher=filereader.nextLine();
          String plainvals = ob.decrypt(NN,a,cipher);
          String plaintext = ob.valToText(plainvals);
          System.out.print(plaintext);
          writer.print(plaintext);
        }
        writer.close();
      }
        catch(Exception e){
          System.out.println("Exception "+e+" catched");
        }
    }
    else{
      System.out.println("\nEnter correct choice !");
    }
  }
}
