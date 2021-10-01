import scala.io.StdIn

import java.net.Socket

import java.io.{DataInputStream, DataOutputStream}



object Client extends App {

    val csocket = new Socket("localhost", 3001)



    val d_input_stream = new DataInputStream(csocket.getInputStream())



    val d_output_stream = new DataOutputStream(csocket.getOutputStream())



    d_output_stream.writeBytes(s"${StdIn.readLine()}\n")



    val server_data = d_input_stream.readLine()



    println(s"Message from server: $server_data")

}