import java.lang.*;
import java.io.*;
import java.util.Scanner;
import java.math.BigInteger;

class DesCrypto{
	public String desEncryption(String cipher, String Key){
		int[] IP={
				58,50,42,34,26,18,10,2,
				60,52,44,36,28,20,12,4,
				62,54,46,38,30,22,14,6,
				64,56,48,40,32,24,16,8,
				57,49,41,33,25,17,9,1,
				59,51,43,35,27,19,11,3,
				61,53,45,37,29,21,13,5,
				63,55,47,39,31,23,15,7};
		String BinCipher = HextoBinSplit(cipher);
		String L = BinCipher.substring(0,32);
		String R = BinCipher.substring(32);
		String BinKey = HextoBinSplit(Key);
		String IPvals = new String();
		for (int i=0;i<64;i++){
			IPvals = IPvals+BinCipher.charAt(IP[i]-1);
		}
		String sixteenkeys[]=SixteenSubkeys(BinKey);
		String plainvals = processDES(IPvals,sixteenkeys);
		String finalHexa = new String();
		String[] substrings = plainvals.split("(?<=\\G.{8})");
		for(int i=0;i<substrings.length;i++){
			int dec = Integer.parseInt(substrings[i],2);
			String dummy = Integer.toString(dec,16);
			int len = dummy.length();
			if(len < 2)
			{
				for (int k=0;k<2-len;k++){
					dummy = "0"+dummy;
				}
			}
			finalHexa = finalHexa + dummy;
		}
		return finalHexa;
	}
	public String desDecryption(String cipher, String Key){
		int[] IP={
				58,50,42,34,26,18,10,2,
				60,52,44,36,28,20,12,4,
				62,54,46,38,30,22,14,6,
				64,56,48,40,32,24,16,8,
				57,49,41,33,25,17,9,1,
				59,51,43,35,27,19,11,3,
				61,53,45,37,29,21,13,5,
				63,55,47,39,31,23,15,7};
		String BinCipher = HextoBinSplit(cipher);
		String L = BinCipher.substring(0,32);
		String R = BinCipher.substring(32);
		String BinKey = HextoBinSplit(Key);
		String IPvals = new String();
		for (int i=0;i<64;i++){
			IPvals = IPvals+BinCipher.charAt(IP[i]-1);
		}
		String sixteenkeys[]=SixteenSubkeys(BinKey);
		String[] InverseKeys = new String[16];
		for(int i=15,j=0;i>=0;i--,j++){
			InverseKeys[j] = sixteenkeys[i];
		}
		//String plainvals = processDES(IPvals,sixteenkeys);
		String plainvals = processDES(IPvals,InverseKeys);
		//binary to Hexadecimal
		String finalHexa = new String();
		String[] substrings = plainvals.split("(?<=\\G.{8})");
		for(int i=0;i<substrings.length;i++){
			int dec = Integer.parseInt(substrings[i],2);
			String dummy = Integer.toString(dec,16);
			int len = dummy.length();
			if(len < 2)
			{
				for (int k=0;k<2-len;k++){
					dummy = "0"+dummy;
				}
			}
			finalHexa = finalHexa + dummy;
		}
		return finalHexa;
	}
	public String Sbox(String KE){
		int[][][] S={
			{{14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7},
			 {0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8},
			 {4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0},
			 {15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13}
			},
			{
			 {15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10},
			 {3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5},
			 {0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15},
			 {13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9}
			},
			{
			  {10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8},
			  {13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1},
			  {13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7},
			  {1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12}
			},
			{
			  {7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15},
			  {13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9},
			  {10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4},
			  {3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14}
			},
			{
			  {2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9},
			  {14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6},
			  {4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14},
			  {11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3},
			},
			{
			   {12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11},
			   {10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8},
			   {9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6},
			   {4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13}
			},
			{
			  {4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1},
			  {13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6},
			  {1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2},
			  {6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12}
			},
			{
			  {13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7},
			  {1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2},
			  {7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8},
			  {2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11}
			}
		};
		int[] P={
			16,7,20,21,
			29,12,28,17,
			1,15,23,26,
			5,18,31,10,
			2,8,24,14,
			32,27,3,9,
			19,13,30,6,
			22,11,4,25
		};
		String[] substrings_8 = KE.split("(?<=\\G.{6})");
		String S_8 = new String();
		for(int l=0;l<8;l++){
			String temp = substrings_8[l];
			int i = Integer.parseInt(temp.substring(0,1)+temp.substring(5,6),2);
			int j = Integer.parseInt(temp.substring(1,5),2);
			int val = S[l][i][j];
			String res = Integer.toString(val,2);
			int len = res.length();
			if(len < 4)
			{
				for (int k=0;k<4-len;k++){
					res = "0"+res;
				}
			}
			S_8 = S_8 + res;
		}
		String finalRes = new String();
		for(int i=0;i<32;i++){
			finalRes = finalRes +S_8.charAt(P[i]-1);
		}
		return finalRes;
	}
	public String xorFun(String L, String R, String Key){
		int[] E={
				32,1,2,3,4,5,
				4,5,6,7,8,9,
				8,9,10,11,12,13,
				12,13,14,15,16,17,
				16,17,18,19,20,21,
				20,21,22,23,24,25,
				24,25,26,27,28,29,
				28,29,30,31,32,1};
		//change 32 to 48 bit; E(R)
		String R_48 = new String();
		for(int i=0;i<48;i++){
			R_48 = R_48 +R.charAt(E[i]-1);
		}
		//xor
		String KE = new String();
		for(int i=0;i<48;i++){
			KE = KE + Integer.toString(Character.getNumericValue(R_48.charAt(i))^Character.getNumericValue(Key.charAt(i)));
		}
		//Sbox
		String res = Sbox(KE);
		String resAfterXor = new String();
		for(int i=0;i<32;i++){
			resAfterXor = resAfterXor + Integer.toString(Character.getNumericValue(L.charAt(i))^Character.getNumericValue(res.charAt(i)));
		}
		return resAfterXor;
	}
	public String processDES(String IP,String[] sixteenkeys){
		int[] IPinverse={
			40,8,48,16,56,24,64,32,
			39,7,47,15,55,23,63,31,
			38,6,46,14,54,22,62,30,
			37,5,45,13,53,21,61,29,
			36,4,44,12,52,20,60,28,
			35,3,43,11,51,19,59,27,
			34,2,42,10,50,18,58,26,
			33,1,41,9,49,17,57,25
		};
		String L_0 = IP.substring(0,32);
		String R_0 = IP.substring(32);
		for(int i=0;i<16;i++){
			String L_temp = R_0;
			String R_temp = xorFun(L_0,R_0,sixteenkeys[i]);
			L_0 = L_temp;
			R_0 = R_temp;
		}
		String temp = new String();
		temp = R_0 + L_0;
		//IPinverse
		String final_vals = new String();
		for (int i=0;i<64;i++){
			final_vals = final_vals+temp.charAt(IPinverse[i]-1);
		}
		return final_vals;
	}
	public String PCOnePermutation(String key){
		int[] PC_1={
				  57,49,41,33,25,17,9,
				  1,58,50,42,34,26,18,
				  10,2,59,51,43,35,27,
				  19,11,3,60,52,44,36,
				  63,55,47,39,31,23,15,
				  7,62,54,46,38,30,22,
				  14,6,61,53,45,37,29,
				  21,13,5,28,20,12,4
	};
		String fiveSixkey = new String();
		for (int i=0;i<56;i++){
			fiveSixkey = fiveSixkey+key.charAt(PC_1[i]-1);
		}
		return fiveSixkey;
	}
	public String[] SixteenSubkeys(String key){
		String[] c = new String[16];
		String[] d = new String[16];
		String[] subKeys = new String[16];
		int[] PC_2={
				14,17,11,24,1,5,
				3,28,15,6,21,10,
				23,19,12,4,26,8,
				16,7,27,20,13,2,
				41,52,31,37,47,55,
				30,40,51,45,33,48,
				44,49,39,56,34,53,
				46,42,50,36,29,32
				};
		String fiveSixkey = PCOnePermutation(key);
		String c_0 = fiveSixkey.substring(0,fiveSixkey.length()/2);
		String d_0 = fiveSixkey.substring(fiveSixkey.length()/2);
		for(int i=0;i<16;i++){
			if(i==0 || i==1 || i==8 || i==15){
				c_0 = c_0.substring(1)+c_0.charAt(0);
				d_0 = d_0.substring(1)+d_0.charAt(0);
			}
			else{
				c_0 = c_0.substring(2)+c_0.charAt(0)+c_0.charAt(1);
				d_0 = d_0.substring(2)+d_0.charAt(0)+d_0.charAt(1);
			}
			c[i]=c_0;
			d[i]=d_0;
		}
		for(int j=0;j<16;j++){
			String tempKey = c[j]+d[j];
			String finalkey = new String();
			for (int i=0;i<48;i++){
				finalkey = finalkey + tempKey.charAt(PC_2[i]-1);
				}
			subKeys[j]=finalkey;
		}

		return subKeys;
	}
	public String HextoBinSplit(String cipher){
		int len = cipher.length();
		String res=new String();
		for (int i=0;i<len;i=i+2){
			res = res + HextoBin(cipher.substring(i, i+2));
		}
		return res;
	}
	public String HextoBin(String cipher){
		BigInteger hexVal = new BigInteger(cipher,16);
		String res = hexVal.toString(2);
		int len = hexVal.bitLength();
		if(len < 8)
		{
			for (int i=0;i<8-len;i++){
				res = "0"+res;
			}
		}
		return res;
	}
}

class desprog1
{
	public static void main(String args[]){
		Scanner input = new Scanner(System.in);
		System.out.println(" ------ DES cryptosystem ------");
		System.out.println("  1. Encryption");
		System.out.println("  2. Decryption"+"\n");
		System.out.print(" Enter the choice: ");
		String choice = input.next();
		System.out.println("Enter Hexadecimal key:");
		String key = input.next();
		if(choice.equals("1")){
			System.out.println("Encryption selected");
			String ciphertext = new String();
			System.out.println("Enter plain:");
			String plain = input.next();
			DesCrypto ob = new DesCrypto();
			String res = ob.desEncryption(plain,key);
			System.out.println("Hexadecimal cipher: "+res.toUpperCase( ));
		}
		else if(choice.equals("2")){
			System.out.println("Decryption selected");
			try{
				String ciphertext = new String();
				System.out.println("Enter file name:");
				File filename = new File(input.next());
				Scanner filereader = new Scanner(filename);
				while(filereader.hasNextLine()){
					ciphertext += filereader.nextLine();
			}
			String cipherSubstrings[]=ciphertext.split("(?<=\\G.{16})");
			DesCrypto ob = new DesCrypto();
			//create file
			PrintWriter writer = new PrintWriter("desDecryptionResult.txt", "UTF-8");
			for(int i=0;i<cipherSubstrings.length;i++){
				String finalres=ob.desDecryption(cipherSubstrings[i],key);
				System.out.println(HexaToText(finalres));
				writer.print(HexaToText(finalres));
			}
			writer.close();
		}
		catch (Exception e){
			System.out.println(e);
		}
		}else{
			System.out.println("Select correct choise");
		}
	}
	public static String HexaToText(String hexaVals){
		String  res = new String();
		for(int i=0;i<hexaVals.length();i+=2){
			String temp = hexaVals.substring(i,i+2);
			res += (char)Integer.parseInt(temp, 16);
		}
		return res;
	}
}
