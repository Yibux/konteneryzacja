package login.logintoserver.controller

import login.logintoserver.model.User
import login.logintoserver.model.UserRegistser
import login.logintoserver.model.UserRequest
import login.logintoserver.repository.UserRepository
import org.springframework.http.ResponseEntity
import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.*
@RestController
@RequestMapping("/user")
class UserController(private val userService: UserRepository) {
    @GetMapping("/all")
    private fun getAllUsers(): ResponseEntity<MutableList<User>> {
        return ResponseEntity.ok(userService.findAll())
    }

    @PostMapping("/add")
    private fun addUser(@RequestBody user: UserRegistser): ResponseEntity<User> {
        val newUser = User(null, null, user.email, user.password)
        userService.save(newUser)
        return ResponseEntity.ok(newUser)
    }
}