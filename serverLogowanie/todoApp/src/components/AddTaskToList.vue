<template>
    <div>
      <h2>Add New Task</h2>
      <form @submit.prevent="addTask">
        <label for="name">Name:</label>
        <input type="text" id="name" v-model="newTask.name" required>
        
        <label for="status">Status:</label>
        <select id="status" v-model="newTask.status" required>
          <option value="TODO">To Do</option>
          <option value="IN_PROGRESS">In Progress</option>
          <option value="DONE">Done</option>
        </select>
        
        <label for="dueDate">Due Date:</label>
        <input type="date" id="dueDate" v-model="newTask.dueDate">
        
        <button type="submit">Add Task</button>
      </form>
    </div>
  </template>
  
<script>
  import { ref } from 'vue'
  import router from '@/router'
  
  export default {
    setup() {
      const newTask = ref({
        name: '',
        status: 'TODO',
        dueDate: new Date().toISOString().substr(0, 10)
      })
  
      const addTask = async () => {
        try {
          const id = localStorage.getItem('userId');
          console.log(id)
          const response = await fetch('http://localhost:5000/api/add/' + id, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
                'mode': 'no-cors'
            },
            body: JSON.stringify(newTask.value)
          })
  
          if (response.ok) {
            console.log('Task added successfully')
            router.push('/todoList')
            newTask.value = {
              name: '',
              status: 'TODO',
              dueDate: ''
            }
          } else {
            console.log('Failed to add task:', response.body)
          }
        } catch (error) {
          console.error('An error occurred while adding task:', error)
          throw error
        }
      }
  
      return {
        newTask,
        addTask
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

    option {
      color: black;
    }
    button{
      background-color: rgb(207, 78, 2);
    }
  </style>
  