import Login from "./components/login.js";
import Main from "./components/main.js";
import child1 from "./components/mainChild1.js";
import child2 from "./components/mainChild2.js";
export default new VueRouter({
    routes: [
        { path: "/", component: Login },
        { path: "/login", component: Login },
    {
      path: "/main",
      component: Main,
      children: [
        { path: "/main/child1", component: child1 },
        { path: "/main/child2", component: child2 },
      ],
    },
      ],
});