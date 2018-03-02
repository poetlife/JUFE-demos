package Jufe

import java.math.BigInteger
import java.security.KeyFactory
import java.security.PublicKey
import java.security.spec.RSAPublicKeySpec
import javax.crypto.Cipher

class EncryptionJufe(private val password: String){
    private val n = "5598e3b75d21a2989274e222fa59ab07d829faa29b544e3a920c4dd287aed9302a657280c23220a35ae985ba157" +
            "400e0502ce8e44570a1513bf7146f372e9c842115fb1b86def80e2ecf9f8e7a586656d12b27529f487e55052e5c31d0836b" +
            "2e8c01c011bca911d983b1541f20b7466c325b4e30b4a79652470e88135113c9d9"
    // 256 bit hex
    private val e = "10001"  // hex

    private fun generatePublicKey(n: String, e: String): PublicKey {
        // 根据n和e的值生成公钥
        val modulus = BigInteger(n, 16)
        val exponent = BigInteger(e, 16)
        val publicKeySpec = RSAPublicKeySpec(modulus, exponent)
        val keyFactory = KeyFactory.getInstance("RSA")
        val publicKey = keyFactory.generatePublic(publicKeySpec)
        return publicKey
    }

    private fun encryption(content: String, publicKey: PublicKey): ByteArray{
        // 利用公钥进行加密
        val cipher = Cipher.getInstance("RSA")
        cipher.init(Cipher.ENCRYPT_MODE, publicKey)
        val byteContent = content.toByteArray()
        val encryptedContent = cipher.doFinal(byteContent)
        return encryptedContent
    }

    private fun bytes2hex(content: ByteArray): String{
        var bigInteger = BigInteger(1, content)
        return bigInteger.toString(16)
    }

    fun run():String{
        val publicKey = generatePublicKey(n, e)
        var encryptedContent = encryption(password, publicKey)
        return bytes2hex(encryptedContent)
    }
}