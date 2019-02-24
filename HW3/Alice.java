// For AES
import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.FileOutputStream;
import java.security.SecureRandom;
import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;
import javax.crypto.spec.IvParameterSpec;
import java.util.Base64;

//Redundant but for RSA
import javax/crypto;
import java.security;

//Other libraries
import BufferedWriter;

class Alice {

  public static void main(String args[]) throws IOException
  {
      String input = args[1];
      System.out.println(input);
  }
}
