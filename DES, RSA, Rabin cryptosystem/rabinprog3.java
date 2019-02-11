import java.lang.*;
import java.io.*;
import java.util.Scanner;
import java.math.BigInteger;

class Rabincrypto{
  public void encryp(String p,String q,String plain){
    BigInteger pp = new BigInteger(p);
    BigInteger qq = new BigInteger(q);
    BigInteger nn = pp.multiply(qq);
    BigInteger x  = new BigInteger(plain);
    BigInteger y  = x.modPow(new BigInteger("2"),nn);
    System.out.println("n :"+nn);
    System.out.println("encrypted plain: "+y);
  }
  public void decrypt(String pp,String qq,String cipher){
    BigInteger p = new BigInteger(pp),q=new BigInteger(qq),y=new BigInteger(cipher);
    BigInteger n = p.multiply(q);
    System.out.println("n :"+n.toString());
    BigInteger x_p = sqrtmod(y,p);
    BigInteger x_q = sqrtmod(y,q);
    BigInteger xp_1 = x_p.mod(p);
    BigInteger xp_2 = x_p.negate().mod(p);
    BigInteger xq_1 = x_q.mod(q);
    BigInteger xq_2 = x_q.negate().mod(q);
    BigInteger[] result =  xgcd(q,p);
    BigInteger b_1 = result[0];
    BigInteger b_2 = result[1];
    System.out.println("sqrt("+y.toString()+") mod "+ p.toString()+" (positive) :"+xp_1.toString());
    System.out.println("sqrt("+y.toString()+") mod "+ p.toString()+" (negetive) :"+xp_2.toString());
    System.out.println("sqrt("+y.toString()+") mod "+ q.toString()+" (positive) :"+xq_1.toString());
    System.out.println("sqrt("+y.toString()+") mod "+ q.toString()+" (negetive) :"+xq_2.toString());
    System.out.println("b1 :"+b_1.toString());
    System.out.println("b2 :"+b_2.toString());
    BigInteger res_1 = q.multiply(b_1).multiply(xp_1).add(p.multiply(b_2).multiply(xq_1)).mod(n);
    BigInteger res_2 = q.multiply(b_1).multiply(xp_1).add(p.multiply(b_2).multiply(xq_2)).mod(n);
    BigInteger res_3 = q.multiply(b_1).multiply(xp_2).add(p.multiply(b_2).multiply(xq_1)).mod(n);
    BigInteger res_4 = q.multiply(b_1).multiply(xp_2).add(p.multiply(b_2).multiply(xq_2)).mod(n);
    System.out.println("plain1 :"+res_1.toString());
    System.out.println("plain2 :"+res_2.toString());
    System.out.println("plain3 :"+res_3.toString());
    System.out.println("plain4 :"+res_4.toString());
  }
  public BigInteger sqrtmod(BigInteger y,BigInteger a){
    BigInteger temp = a.add(BigInteger.ONE);
    BigInteger temp1 = temp.divide(new BigInteger("4"));
    BigInteger val = y.modPow(temp1,a);
    return val;
  }
  public BigInteger[] xgcd(BigInteger a, BigInteger b) {
  BigInteger x = a,y=b;
	BigInteger[] temp = new BigInteger[2],res = new BigInteger[2];
	BigInteger x_0 = BigInteger.ONE, x_1 = BigInteger.ZERO,y_0 = BigInteger.ZERO, y_1 = BigInteger.ONE;
	while (true){
	    temp = x.divideAndRemainder(y);
      x = temp[1];
	    x_0 = x_0.subtract(y_0.multiply(temp[0]));
	    x_1 = x_1.subtract(y_1.multiply(temp[0]));
	    if (x.equals(BigInteger.ZERO)) {
        res[0]=y_0;
        res[1]=y_1;
        return res;
      };
	    temp = y.divideAndRemainder(x);
      y = temp[1];
	    y_0 = y_0.subtract(x_0.multiply(temp[0]));
	    y_1 = y_1.subtract(x_1.multiply(temp[0]));
	    if (y.equals(BigInteger.ZERO)) {
        res[0]=x_0;
        res[1]=x_1;
        return res;};
	}
}
public void encrypmethod2(String p,String q,String plain){
  BigInteger pp = new BigInteger(p);
  BigInteger qq = new BigInteger(q);
  BigInteger B = new BigInteger("1357");
  BigInteger nn = pp.multiply(qq);
  BigInteger x  = new BigInteger(plain);
  BigInteger temp = x.multiply(x.add(B));
  BigInteger y = temp.mod(nn);
  System.out.println("n :"+nn);
  System.out.println("encrypted plain: "+y);
}
public void decryptmethod2(String pp,String qq,String cipher){
  BigInteger p = new BigInteger(pp),q=new BigInteger(qq),y=new BigInteger(cipher),B = new BigInteger("1357");
  BigInteger n = p.multiply(q);
  System.out.println("n :"+n.toString());
  BigInteger yi = calculate_C(y,n);
  System.out.println("intermediate y val :"+yi);
  //find possible values for xi
  BigInteger x_p = sqrtmod(yi,p);
  BigInteger x_q = sqrtmod(yi,q);
  BigInteger xp_1 = x_p.mod(p);
  BigInteger xp_2 = x_p.negate().mod(p);
  BigInteger xq_1 = x_q.mod(q);
  BigInteger xq_2 = x_q.negate().mod(q);
  BigInteger[] result =  xgcd(q,p);
  BigInteger b_1 = result[0];
  BigInteger b_2 = result[1];
  System.out.println("sqrt("+yi.toString()+") mod "+ p.toString()+" (positive) :"+xp_1.toString());
  System.out.println("sqrt("+yi.toString()+") mod "+ p.toString()+" (negetive) :"+xp_2.toString());
  System.out.println("sqrt("+yi.toString()+") mod "+ q.toString()+" (positive) :"+xq_1.toString());
  System.out.println("sqrt("+yi.toString()+") mod "+ q.toString()+" (negetive) :"+xq_2.toString());
  System.out.println("b1 :"+b_1.toString());
  System.out.println("b2 :"+b_2.toString());
  BigInteger xi_1 = q.multiply(b_1).multiply(xp_1).add(p.multiply(b_2).multiply(xq_1)).mod(n);
  BigInteger xi_2 = q.multiply(b_1).multiply(xp_1).add(p.multiply(b_2).multiply(xq_2)).mod(n);
  BigInteger xi_3 = q.multiply(b_1).multiply(xp_2).add(p.multiply(b_2).multiply(xq_1)).mod(n);
  BigInteger xi_4 = q.multiply(b_1).multiply(xp_2).add(p.multiply(b_2).multiply(xq_2)).mod(n);
  System.out.println("xi_1 :"+xi_1.toString());
  System.out.println("xi_2 :"+xi_2.toString());
  System.out.println("xi_3 :"+xi_3.toString());
  System.out.println("xi_4 :"+xi_4.toString());
  BigInteger Bdiv_2 = new BigInteger("21673");
  BigInteger res_1 = xi_1.subtract(Bdiv_2).mod(n);
  BigInteger res_2 = xi_2.subtract(Bdiv_2).mod(n);
  BigInteger res_3 = xi_3.subtract(Bdiv_2).mod(n);
  BigInteger res_4 = xi_4.subtract(Bdiv_2).mod(n);
  System.out.println("plain1 :"+res_1.toString());
  System.out.println("plain2 :"+res_2.toString());
  System.out.println("plain3 :"+res_3.toString());
  System.out.println("plain4 :"+res_4.toString());
}
public BigInteger calculate_C(BigInteger y,BigInteger n){
  BigInteger TwoInverse = new BigInteger("20995");
  BigInteger B = new BigInteger("1357");
  BigInteger temp = y.add(B.multiply(TwoInverse).pow(2));
  BigInteger y_temp = temp.mod(n);
  return y_temp;
}
}
class rabinprog3
{
	public static void main(String args[]){
		Scanner input = new Scanner(System.in);
    while(true){
		    System.out.println(" ------ Rabin cryptosystem ------");
        System.out.println(" SELECT Encryption method");
        System.out.println(" 1. ek(x)=x^2 mod n ");
        System.out.println(" 2. ek(x) = x(x+B) mod n ");
        System.out.println(" 3. exit");
        System.out.print(" Enter the choice: ");
        int choice = Integer.parseInt(input.next());
        if(choice==1){
          System.out.print("\n      p:");
          String p = input.next();
          System.out.print("\n      q:");
          String q = input.next();
          System.out.println("\n    Method selected ek(x)=x^2 mod n ");
          System.out.println("        1.Encryption");
  		    System.out.println("        2.Decryption");
          System.out.print("        Enter the choice: ");
          int choice1 = Integer.parseInt(input.next());
          Rabincrypto ob = new Rabincrypto();
          if(choice1==1){
            try{
              System.out.println("Encryption selected");
              System.out.println("plain:");
              String plain = input.next();
              ob.encryp(p,q,plain);
            }
            catch(Exception e){
              System.out.println("Exception "+e+" catched");
            }
          }else if(choice1==2){
            try{
              System.out.println("Decryption selected");
              System.out.println("cipher:");
              String cipher = input.next();
              ob.decrypt(p,q,cipher);
            }
            catch(Exception e){
              System.out.println("Exception "+e+" catched");
            }
          }
          else{
            System.out.println("\nEnter correct choice !");
          }
        }else if(choice==2){
          System.out.print("\n      p:");
          String p = input.next();
          System.out.print("\n      q:");
          String q = input.next();
          System.out.println("    Method selected ek(x) = x(x+B) mod n ");
          System.out.println("      1.Encryption");
  		    System.out.println("      2.Decryption");
          System.out.print("      Enter the choice: ");
          int choice2 = Integer.parseInt(input.next());
          Rabincrypto ob = new Rabincrypto();
          if(choice2==1){
            try{
              System.out.println("Encryption selected");
              System.out.println("plain:");
              String plain = input.next();
              ob.encrypmethod2(p,q,plain);
            }
            catch(Exception e){
              System.out.println("Exception "+e+" catched");
            }
          }else if(choice2==2){
            try{
              System.out.println("Decryption selected");
              System.out.println("cipher:");
              String cipher = input.next();
              ob.decryptmethod2(p,q,cipher);
            }
            catch(Exception e){
              System.out.println("Exception "+e+" catched");
            }
          }
          else{
            System.out.println("\nEnter correct choice !");
          }
        }else if(choice==3){
          System.exit(0);
        }
        else{
          System.out.println("\nEnter correct choice !");
        }
    }
  }
}
