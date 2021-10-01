import java.net.{ServerSocket, Socket}

import scala.concurrent.Future

import java.io.{DataInputStream, DataOutputStream}

import scala.concurrent.ExecutionContext.Implicits.global




object Server5 extends App {



    val ssocket = new ServerSocket(3001)



    val clientSocket: Future[Socket] = Future { ssocket.accept() }    //blocking call



    def processSocket(x: Socket): Unit = {

        val clientSocket2: Future[Socket] = Future { ssocket.accept() }



        clientSocket2.foreach( x => {

            processSocket(x)

        })



        val d_input_stream = new DataInputStream(x.getInputStream())



        val d_output_stream = new DataOutputStream(x.getOutputStream())



        val client_incoming_data = d_input_stream.readLine()



        println(s"Message from client: $client_incoming_data")



        d_output_stream.writeBytes("Hello\n")



        x.close()



    }



    clientSocket.foreach(x => {

        processSocket(x)

    })



    scala.io.StdIn.readLine("Press any key to quit\n")



    ssocket.close()

}