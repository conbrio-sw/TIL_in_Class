import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter)

import BoardMain from "@/components/BoardMain.vue";
import Login from "@/components/Login.vue";
import User from "@/components/User.vue";
// import NavBar from "@/components/NavBar.vue";
// import Pagination from "@/components/Pagination.vue";
export default new VueRouter({
    routes: [
        {
            path: "/",
            component: Login,
        },
        {
            path: "/board",
            name: "BoardMain",
            component: BoardMain,
        },
        {
            path: "/login",
            name: "Login",
            component: Login,
        },
        {
            path: "/user",
            name: "User",
            component: User,
        },
  ]  
})