import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import RegisterView from '@/views/RegisterView.vue'
import ToDoView from '@/views/TodoListView.vue'

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
      path: '/todo',
      name: 'Todo',
      component: ToDoView,
      beforeEnter: (to, from, next) => {
        const authToken = localStorage.getItem('authToken')
  
        if (!authToken) {
          next({ name: 'register' }) // redirect to Login page if authToken is not present
        } else {
          next() // proceed to /todo if authToken is present
        }
      }
    },
    {
      path: '/signUp',
      name: 'signUp',
      component: LoginView
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'not-found',
      component: () => import('@/views/NotFoundView.vue')
    }
  ]
})


export default router