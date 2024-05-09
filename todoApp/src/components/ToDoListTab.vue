<template>
    <div>
        <h2>ToDoListTab</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Title</th>
                    <th>Completed</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="todo in todos" :key="todo.id">
                    <td>{{ todo.id }}</td>
                    <td>{{ todo.title }}</td>
                    <td>{{ todo.completed }}</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
// export default {
//     name: 'ToDoListTab',
//     data() {
//         return {
//             todos: [],
//         };
//     },
//     mounted() {
//         this.fetchTodos();
//     },
//     methods: {
//         async fetchTodos() {
//             try {
//                 const response = await fetch('https://api.example.com/todos');
//                 const data = await response.json();
//                 this.todos = data;
//             } catch (error) {
//                 console.error(error);
//             }
//         },
//     },
// };
</script>

<style scoped>
/* Add your component styles here */
</style>