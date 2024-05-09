import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import ToDoView from '@/views/TodoListView.vue'
import AddToListView from '@/views/AddToListView.vue'
import EditTask from '@/views/EditListView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/register',
      name: 'register',
      component: RegisterView
    },
    {
      path: '/signUp',
      name: 'signUp',
      component: LoginView
    },
    {
      path: '/AddTaskToList',
      name: 'AddTaskToList',
      component: AddToListView
    },
    {
      path: '/EditTask/:id',
      name: 'EditTask',
      component: EditTask
    },
    {
      path: '/todoList',
      name: 'Todo',
      component: ToDoView,
      beforeEnter: (to, from, next) => {
        const authToken = localStorage.getItem('authToken')
  
        if (!authToken) {
          next({ name: 'signUp' })
        } else {
          next()
        }
      }
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('@/views/NotFoundView.vue')
    }
  ]
})


export default router
