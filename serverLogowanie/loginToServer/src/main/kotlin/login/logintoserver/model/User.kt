package login.logintoserver.model

import lombok.Data
import org.springframework.data.annotation.Id
import org.springframework.data.mongodb.core.mapping.Document

@Document
@Data
class User(@Id var id: String?, var username: String?, var email: String?, var password: String?) {

}

class UserRequest(var username: String?, var email: String?, var password: String?)

class UserRegistser(var email: String?, var password: String?)