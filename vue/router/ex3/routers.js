import Login from "./components/login.js";
import Main from "./components/main.js";
export default new VueRouter({
    routes: [
        { path: "/", component: Login },
        { path: "/main", component: Main },
        { path: "/login", component: Login },
      ],
});