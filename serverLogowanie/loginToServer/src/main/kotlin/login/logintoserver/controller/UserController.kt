package login.logintoserver.controller

import login.logintoserver.model.User
import login.logintoserver.model.UserRegistser
import login.logintoserver.model.UserRequest
import login.logintoserver.repository.UserRepository
import org.springframework.data.annotation.Id
import org.springframework.http.HttpStatus
import org.springframework.http.ResponseEntity
import org.springframework.stereotype.Controller
import org.springframework.web.bind.annotation.*
import java.net.http.HttpHeaders
@CrossOrigin(origins =["http://localhost:5173"])
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


        return ResponseEntity<User>(user.email?.let { userService.findByEmail(it) }, null, 200)
    }


    @PostMapping("/login")
    private fun loginUser(@RequestBody user: UserRequest): ResponseEntity<out Any> {
        val allUsers: MutableList<User> = userService.findAll()
        for (u in allUsers) {
            if (u.email == user.email && u.password == user.password) {
                val headers = org.springframework.http.HttpHeaders()
                headers.add("Access-Control-Allow-Origin", "*")
                headers.add("Access-Control-Allow-Methods", "POST, GET, OPTIONS, DELETE")
                headers.add("Access-Control-Allow-Headers", "Content-Type, Authorization")
                return ResponseEntity<User>(u, headers, HttpStatus.OK)
            }
        }
        return ResponseEntity.badRequest().body(mapOf("meesage" to "Invalid credentials"))
    }
}