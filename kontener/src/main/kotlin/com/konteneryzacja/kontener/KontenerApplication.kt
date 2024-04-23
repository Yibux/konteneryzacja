package com.konteneryzacja.kontener

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.context.annotation.ComponentScan

@SpringBootApplication
@ComponentScan("com.konteneryzacja.kontener.controllers")
class KontenerApplication


fun main(args: Array<String>) {
	runApplication<KontenerApplication>(*args)
}
