import Vue from 'vue'
import Router from 'vue-router'
import Chat from '@/components/Chat'
import UserAuth from '@/components/UserAuth'
import AppModal from '@/components/AppModal'

Vue.use(Router)
const router = new Router({
  routes: [
    {
      path: '/chats/:uri?',
      name: 'Chat',
      component: Chat
    },

    {
      path: '/auth',
      name: 'UserAuth',
      component: UserAuth
    },
    {
      path: '/modal',
      name: 'AppModal',
      component: AppModal
    }
  ]
})

// вызывается перед переходом к любому маршруту в нашем приложении
router.beforeEach((to, from, next) => {
  // проверка есть ли токен
  if (sessionStorage.getItem('authToken') !== null || to.path === '/auth') {
    next()
  } else {
    next('/auth')
  }
})

export default router
