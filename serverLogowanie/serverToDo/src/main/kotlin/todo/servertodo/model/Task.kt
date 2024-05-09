package todo.servertodo.model

import jakarta.persistence.*
import lombok.Data
import java.util.*

@Data
@Entity
@Table(name="TodoList")
class Task {
    @Id
    var id: UUID? = null
    var name: String? = null
    @Enumerated(EnumType.STRING)
    var status: Status? = null
    var dueDate: Date? = null
}

enum class Status {
    TODO, IN_PROGRESS, DONE
}

class TaskRequest(var name: String?, var status: Status?, var dueDate: Date?)