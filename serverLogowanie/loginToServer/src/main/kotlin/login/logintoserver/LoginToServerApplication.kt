package login.logintoserver

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.context.annotation.ComponentScan

@SpringBootApplication
class LoginToServerApplication

fun main(args: Array<String>) {
	runApplication<LoginToServerApplication>(*args)
}
