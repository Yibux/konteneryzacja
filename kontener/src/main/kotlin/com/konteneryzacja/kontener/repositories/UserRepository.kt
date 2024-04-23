package com.konteneryzacja.kontener.repositories

import com.konteneryzacja.kontener.models.User
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.data.mongodb.repository.MongoRepository
import org.springframework.stereotype.Repository

@Repository
interface UserRepository : MongoRepository<User, String> {}
