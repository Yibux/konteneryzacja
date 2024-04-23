package com.konteneryzacja.kontener.controllers

import com.konteneryzacja.kontener.models.User
import com.konteneryzacja.kontener.models.UserRequest
import com.konteneryzacja.kontener.repositories.UserRepository
import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("users")
class UserController(
    private val repository: UserRepository
) {

    @GetMapping("/")
    fun getALlUsers(): ResponseEntity<List<User>> {
        return ResponseEntity.ok(repository.findAll())
    }

    @GetMapping("/{id}")
    fun getUserById(@PathVariable id: String): ResponseEntity<User> {
        return ResponseEntity.ok(repository.findById(id).orElse(null))
    }


    @PostMapping("/login")
    fun getUserById(@RequestBody user: User): ResponseEntity<User> {
        return ResponseEntity.ok(repository.save(user))
    }

    @PostMapping("/register")
    fun registerUser(@RequestBody user: UserRequest): ResponseEntity<User> {
        val newUser = User(null, user.name, user.email, user.password)
        return ResponseEntity.ok(repository.save(newUser))
    }

    @PutMapping("/{id}")
    fun updateUser(@PathVariable id: String, @RequestBody user: User): ResponseEntity<User> {
        val userToUpdate = repository.findById(id).orElse(null)
        userToUpdate?.let {
            it.name = user.name
            it.email = user.email
            it.password = user.password
            return ResponseEntity.ok(repository.save(it))
        }
        return ResponseEntity.notFound().build()
    }

    @DeleteMapping("/{id}")
    fun deleteUser(@PathVariable id: String): ResponseEntity<Void> {
        repository.deleteById(id)
        return ResponseEntity.noContent().build()
    }
}