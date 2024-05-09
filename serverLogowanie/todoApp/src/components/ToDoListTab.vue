<script setup lang="ts">
import { onMounted } from 'vue'

var todos = []

const todosList = async () => {
    try {
        const response = await fetch('todo', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'mode': 'no-cors'
            }
        })

        if (response.ok) {
            const data = await response.json()

            for (let i = 0; i < data.length; i++) {
                todos.push(data[i])
            }
            return data[0]
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
        console.log(todos)
    } catch (error) {
        console.error('An error occurred while fetching todos:', error)
    }
})

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
                </tr>
            </thead>
            <tbody>
                <tr v-for="todo in todos" :key="todo.id">
                    <td>{{ todo.name }}</td>
                    <td>{{ todo.status }}</td>
                    <td> {{ todo.dueDate }}</td>
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

</style>