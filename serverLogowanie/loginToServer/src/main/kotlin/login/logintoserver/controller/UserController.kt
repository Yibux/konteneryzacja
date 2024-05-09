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
    private fun addUser(@RequestBody user: UserRegistser): ResponseEntity<out Any> {
        val newUser = User(null, null, user.email, user.password)
        val allUsers: MutableList<User> = userService.findAll()
        for (u in allUsers) {
            if (u.email == newUser.email) {
                return ResponseEntity.badRequest().body(mapOf("meesage" to "User already exists"))
            }
        }
        userService.save(newUser)
        return ResponseEntity.ok(mapOf("meesage" to "User added successfully"))
    }

    @PostMapping("/login")
    private fun loginUser(@RequestBody user: UserRequest): ResponseEntity<out Any> {
        val allUsers: MutableList<User> = userService.findAll()
        for (u in allUsers) {
            if (u.email == user.email && u.password == user.password) {
                return ResponseEntity.ok(mapOf("meesage" to "Login successful"))
            }
        }
        return ResponseEntity.badRequest().body(mapOf("meesage" to "Invalid credentials"))
    }
}