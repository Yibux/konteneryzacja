package com.konteneryzacja.kontener.models

import org.springframework.data.annotation.Id
import org.springframework.data.mongodb.core.mapping.Document

@Document
data class User(
    @Id
    val id: String?,
    var name: String,
    var email: String,
    var password: String
)

data class UserRequest(
    val name: String,
    val email: String,
    val password: String
)