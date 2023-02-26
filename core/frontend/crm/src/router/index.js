import {createRouter, createWebHistory} from 'vue-router'
import HomeView from '../views/HomeView.vue'
import SignUpView from "@/views/SignUpView";
import LoginView from "@/views/LoginView";
import DashboardView from "@/views/dashboard/DashboardView";
import MyAccountView from "@/views/dashboard/MyAccountView";
import store from "@/store";

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomeView
    },
    {
        path: '/about',
        name: 'about',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    },
    {
        path: '/sign-up',
        name: 'signup',
        component: SignUpView
    },
    {
        path: '/login',
        name: 'login',
        component: LoginView
    },
    {
        path: '/dashboard',
        name: 'dashboard',
        component: DashboardView,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/my-account',
        name: 'my-account',
        component: MyAccountView,
        meta: {
            requireLogin: true
        }
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})
router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
        next("/login")
    } else {
        next()
    }
})


export default router
