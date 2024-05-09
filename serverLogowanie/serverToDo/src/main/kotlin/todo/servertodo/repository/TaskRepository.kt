package todo.servertodo.repository

import org.springframework.data.jpa.repository.JpaRepository
import todo.servertodo.model.Task

interface TaskRepository : JpaRepository<Task, String> {
}