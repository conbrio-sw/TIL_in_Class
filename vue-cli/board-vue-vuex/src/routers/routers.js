import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

import BoardMain from "@/components/BoardMain.vue";
import Login from "@/components/Login.vue";
import User from "@/components/User.vue";
import store from "@/store/store.js";
import Register from "@/components/Register.vue";
// import NavBar from "@/components/NavBar.vue";
// import Pagination from "@/components/Pagination.vue";
export default new VueRouter({
  routes: [
    {
      path: "/",
      component: BoardMain,
      beforeEnter: (to, from, next) => {
        if (!store.state.login.isLogin) {
          next("/login");
        } else {
          return next();
        }
      },
    },
    {
      path: "/board",
      name: "BoardMain",
      component: BoardMain,
      beforeEnter: (to, from, next) => {
        if (!store.state.login.isLogin) {
          next("/login");
        } else {
          return next();
        }
      },
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
    {
      path: "/register",
      name: "Register",
      component: Register,
    },
  ],
});
