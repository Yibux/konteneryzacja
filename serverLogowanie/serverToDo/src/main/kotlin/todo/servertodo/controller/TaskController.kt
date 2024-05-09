package todo.servertodo.controller

import org.springframework.http.ResponseEntity
import org.springframework.web.bind.annotation.*
import todo.servertodo.model.Task
import todo.servertodo.model.TaskRequest
import todo.servertodo.repository.TaskRepository
import java.util.*

@RestController
@RequestMapping("/api")
@CrossOrigin("http://localhost:5173/todoList")
class TaskController(private val taskService: TaskRepository){
    @GetMapping("/all")
    private fun getAllTasks() : ResponseEntity<MutableList<Task>> {
        return ResponseEntity.ok(taskService.findAll())
    }

    @PostMapping("/add")
    private fun addTask(@RequestBody task: TaskRequest): ResponseEntity<out Any> {
        val newTask = Task()
        newTask.id = UUID.randomUUID()
        newTask.name = task.name
        newTask.status = task.status
        newTask.dueDate = task.dueDate
        taskService.save(newTask)
        return ResponseEntity.ok(mapOf("message" to "Task added successfully"))
    }

    @PutMapping("/{id}")
    private fun updateTask(@PathVariable id: String, task: Task): ResponseEntity<out Any> {
        val taskToUpdate = taskService.findById(id)
        if (taskToUpdate.isPresent) {
            taskService.save(task)
            return ResponseEntity.ok(mapOf("message" to "Task updated successfully"))
        }
        return ResponseEntity.badRequest().body(mapOf("message" to "Task not found"))
    }

    @DeleteMapping("/{id}")
    private fun deleteTask(@PathVariable id: String): ResponseEntity<out Any> {
        val taskToDelete = taskService.findById(id)
        if (taskToDelete.isPresent) {
            taskService.deleteById(id)
            return ResponseEntity.ok(mapOf("message" to "Task deleted successfully"))
        }
        return ResponseEntity.badRequest().body(mapOf("message" to "Task not found"))
    }

}