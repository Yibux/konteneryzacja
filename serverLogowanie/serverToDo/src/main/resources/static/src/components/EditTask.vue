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
  import { ref } from 'vue'
  import { useRouter } from 'vue-router'
  
  export default {
    setup() {
      const router = useRouter()

        const taskId = router.currentRoute.value.params.id
  
      const editedTask = ref({
        name: '',
        status: 'TODO',
        dueDate: new Date().toISOString().substr(0, 10)
      })
  
      const updateTask = async () => {
        try {
        //   console.log(taskId)
          const response = await fetch(`http://localhost:5000/api/${taskId}`, {
            method: 'PUT',
            headers: {
              'Content-Type': 'application/json',
                'mode': 'no-cors'
            },
            body: JSON.stringify(editedTask.value)
          })
  
          if (response.ok) {
            console.log('Task updated successfully')
            router.push('/todoList') // Po udanej aktualizacji, przekieruj użytkownika z powrotem do listy zadań
          } else {
            console.log('Failed to update task:', response.body)
          }
        } catch (error) {
          console.error('An error occurred while updating task:', error)
          throw error
        }
      }
  
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
  label {
    /* Dodaj style dla etykiet */
  }
  input, select {
    margin: 2%;
    background-color: white;
    border: 1px solid white;
    border-radius: 5px;
    color: black;
  }
  button {
    /* Dodaj style dla przycisku */
  }

  option {
    color: black;
  }
  </style>
  