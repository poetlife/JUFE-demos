package Jufe

import okhttp3.*
import org.jsoup.Jsoup
import org.jsoup.nodes.Document

/*
this file can really get into the websites of Jufe.
we should process the cookies when GET the website the first time
and then POST data into the website to get the final login cookie
actually if we can right set the cookie
we can set the redirects right(but these still remain confused!)
 */

class Crawler private constructor(){
    /*
    这个爬虫应该不仅仅爬取江西财经大学信息门户网，而且还应该和应用本身的服务器进行通信
    目标在于构建分布式的爬虫系统，在对系统造成最小伤害的时候，达到最大程度的爬取
    由于OkHTTPClient的特性，所以我们对这个类限制成为单例模式
     */

    private val client = OkHttpClient.Builder().cookieJar(CookieJarApp()).build()  // 带有头部的client

    private object mHolder {val INSTANCE = Crawler()}

    companion object {
        // 这个伴随对象确保单例模式
        fun getInstance(): Crawler{
            return mHolder.INSTANCE
        }
    }

    // 这个是用来POST登录的data数据
    private val data = mutableMapOf("username" to "",
            "password" to "",
            "errors" to "0",
            "imageCodeName" to " ",
            "_rememberMe" to "on",
            "cryptoType" to "1",
            "lt" to "",
            "_eventId" to "submit")

    // 登录的链接
    private val LoGIN_URL = "https://ssl.jxufe.edu.cn/cas/login?service=http%3A%2F%2Fecampus.jxufe.edu.cn%2Fc%2Fportal" +
            "%2Flogin%3Fredirect%3D%252Fc"

    private fun getBodyDataByMap(data: Map<String, String>): FormBody{
        // 将封装好的Map里面的data转化为FromBody以便POST出去
        val formData = FormBody.Builder()
        println(data)
        // 循环data以将data中的数据换回formData
        for (key in data.keys){
            formData.add(key, data.getOrDefault(key, "不存在此值"))  // 这里可能存在错误
        }
        val temp = formData.build()
        return temp
    }

    private fun getLt(doc: Document): String {
        try {
            val lt = doc.getElementsByAttributeValue("name", "lt").attr("value")
            return lt
        } catch (e: Exception) {
            e.printStackTrace()
        }
        return ""
    }

    private fun getHtml(response: Response): Document {
        val html = response.body()?.string()
        val doc = Jsoup.parse(html)
        return doc
    }

    private fun processData(username: String, password: String, response: Response){
        data["username"] = username
        data["password"] = EncryptionJufe(password).run()
        data["lt"] = getLt(getHtml(response))
    }

    fun loginJufe(username: String, password: String): Boolean{
        // 这个用来登录江西财经大学信息门户
        var response = client.newCall(Request.Builder().url(LoGIN_URL).build()).execute()
        processData(username, password, response)  // 这里封装好数据
        val body = getBodyDataByMap(data)
        response = client.newCall(Request.Builder().url(LoGIN_URL).post(body).build()).execute()

        // 通过识别response中的页面来判断是否登录成功
        val doc = Jsoup.parse(response.body()?.string())
        if (doc.getElementsByTag("title")[0].text().contains("本科生首页")){
            println("containing")
            return true
        } else{
            println("not containing")
            return false
        }
    }

    fun getResponse(url: String): Response{
        // get
        val response = client.newCall(Request.Builder().url(url).build()).execute()
        return response
    }

    fun postResponse(url: String, data: Map<String, String>): Response{
        // post
        val body = getBodyDataByMap(data)
        val response = client.newCall(Request.Builder().url(url).post(body).build()).execute()
        return response
    }

}

class CookieJarApp: CookieJar{
    /*
    用来储存和更改Cookies，这里的话根据host的不同去存储数据，而且这里的话暂时不使用持久化存储cookies
     */

    private val cookieStore = HashMap<String, MutableList<Cookie>>()

    override fun loadForRequest(url: HttpUrl): MutableList<Cookie> {
        println("Using Cookies of ${url.host()}")
        return cookieStore[url.host()] ?: ArrayList()
    }

    override fun saveFromResponse(url: HttpUrl, cookies: MutableList<Cookie>) {
        println("Saving Cookies of ${url.host()}")
        cookieStore.put(url.host(), cookies)
    }
}

fun main(args: Array<String>){
    val a = Crawler.getInstance()
    a.loginJufe("220150", "p")
}
