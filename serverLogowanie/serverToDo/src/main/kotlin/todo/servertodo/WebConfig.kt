package todo.servertodo

import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry
import org.springframework.web.servlet.config.annotation.ViewControllerRegistry
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer
import org.springframework.web.servlet.resource.EncodedResourceResolver

class WebConfig : WebMvcConfigurer {
    override fun addViewControllers(registry: ViewControllerRegistry) {
        registry.addViewController("/{spring:\\w+}")
            .setViewName("forward:/")
        registry.addViewController("/**/{spring:\\w+}")
            .setViewName("forward:/")
        registry.addViewController("/{spring:\\w+}/**{spring:?!(\\.js|\\.css)$}")
            .setViewName("forward:/")
    }

    override fun addResourceHandlers(registry: ResourceHandlerRegistry) {
        registry.addResourceHandler("/**")
            .addResourceLocations("classpath:/static/")
            .resourceChain(true)
            .addResolver(EncodedResourceResolver())
    }
}