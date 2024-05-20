<template>
  <div>
    <h2>Edit Task</h2>
    <form @submit.prevent="updateTask">
      <label for="name">Name:</label>
      <input type="text" id="name" v-model="editedTask.name" required>

      <label for="status">Status:</label>
      <select id="status" v-model="editedTask.status" required>
        <option value="TODO">To Do</option>
        <option value="IN_PROGRESS">In Progress</option>
        <option value="DONE">Done</option>
      </select>

      <label for="dueDate">Due Date:</label>
      <input type="date" id="dueDate" v-model="editedTask.dueDate">

      <button type="submit">Update Task</button>
    </form>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

export default {
  setup() {
    const router = useRouter()
    const taskId = router.currentRoute.value.params.id
    const editedTask = ref({
      name: '',
      status: '',
      dueDate: ''
    })

    const fetchTask = async () => {
      try {
        const response = await fetch(`http://localhost:5000/api/${taskId}`, {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json'
          }
        })
        const task = await response.json()
        editedTask.value = {
          name: task.name,
          status: task.status,
          dueDate: task.dueDate
        }
      } catch (error) {
        console.error('An error occurred while fetching task:', error)
        throw error
      }
    }

    const updateTask = async () => {
      try {
        const response = await fetch(`http://localhost:5000/api/${taskId}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(editedTask.value)
        })

        if (response.ok) {
          console.log('Task updated successfully')
          router.push('/todoList')
        } else {
          console.log('Failed to update task:', await response.json())
        }
      } catch (error) {
        console.error('An error occurred while updating task:', error)
        throw error
      }
    }

    onMounted(() => {
      fetchTask()
    })

    return {
      editedTask,
      updateTask
    }
  }
}
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
  margin: 2%;
}

input, select {
  margin: 2%;
  background-color: white;
  border: 1px solid white;
  border-radius: 5px;
  color: black;
}

button {
  background-color: rgb(207, 78, 2);
}

option {
  color: black;
}
</style>
