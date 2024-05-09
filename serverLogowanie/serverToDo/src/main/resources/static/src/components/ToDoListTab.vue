<script>
import { onMounted, ref } from 'vue'
import router from '@/router'

export default {
  setup() {
    var todos = ref([]) // Zdefiniuj todos jako ref

    const todosList = async () => {
      try {
        const response = await fetch('http://localhost:5000/api/all', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
            'mode': 'no-cors'
          }
        })

        if (response.ok) {
          const data = await response.json()

          todos.value = data

        } else {
          console.log(response.body)
        }
      } catch (error) {
        console.error('An error occurred while fetching todos:', error)
        throw error
      }
    }

    onMounted(async () => {
      try {
        await todosList()
        console.log(todos.value)
      } catch (error) {
        console.log('An error occurred while fetching todos:', error)
      }
    })
    return {
      todos
    }
  },

  methods: {
    updateTodo: function (id) {
        router.push('/EditTask/'+id)
    },
    deleteTodo: function (id) {
        const deleteItem = async () => {
            try {
              const response = await fetch('http://localhost:5000/api/' + id, {
                method: 'DELETE',
                headers: {
                  'Content-Type': 'application/json',
                  'mode': 'no-cors'
                }
              })
      
              if (response.ok) {
                const data = await response.json()
                console.log(data)
                window.location.reload();
              } else {
                console.log(response.body)
              }
            } catch (error) {
              console.error('An error occurred while deleting todo:', error)
              throw error
            }
          }
      
        deleteItem()
        
    },
    changeCard: function () {
        router.push('/AddTaskToList')
    }
  
  }

}
</script>

<template>
    <div>
        <h2>ToDoListTab</h2>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Status</th>
                    <th>Due Date</th>
                    <v-btn style="background-color: rgb(207, 78, 2);" @click="changeCard">Add Task</v-btn>
                </tr>
            </thead>
            <tbody>
                <tr v-for="todo in todos" :key="todo.id">
                    <td>{{ todo.name }}</td>
                    <td>{{ todo.status }}</td>
                    <td> {{ todo.dueDate }}</td>
                    <td>
                        <button @click="deleteTodo(todo.id)">Delete</button>
                    </td>
                    <td>
                        <button @click="updateTodo(todo.id)">Edit</button>
                    </td>
                </tr>
            </tbody>
        </table>
        
    </div>
</template>



<style scoped>
    table {
        width: 100%;
        border-collapse: collapse;
    }

    th, td {
        border: 1px solid black;
        padding: 8px;
        text-align: left;
    }

    v-btn {
        background-color: rgb(207, 78, 2);
    }

</style>