package todo.servertodo

import org.springframework.boot.autoconfigure.SpringBootApplication
import org.springframework.boot.runApplication
import org.springframework.context.annotation.ComponentScan
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer
import todo.servertodo.controller.TaskController

@SpringBootApplication
@ComponentScan("todo.servertodo.controller")
class ServerTodoApplication : WebMvcConfigurer {
	override fun addResourceHandlers(registry: ResourceHandlerRegistry) {
		registry.addResourceHandler("/todoList/**")
			.addResourceLocations("classpath:/static/src/App.vue")
	}
}

fun main(args: Array<String>) {
	runApplication<ServerTodoApplication>(*args)
}
