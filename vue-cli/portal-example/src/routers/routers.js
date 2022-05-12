import Vue from "vue"
import VueRouter from "vue-router"
Vue.use(VueRouter)

import NavBar from "@/components/NavBar.vue"
import Cafe from "@/components/Cafe.vue"
import Mail from "@/components/Mail.vue"
import Blog from "@/components/Blog.vue"
import TellMe from "@/components/TellMe.vue"
import Footer from "@/components/Footer.vue"


export default new VueRouter({
    routes: [
        {
            path: "/",
            components: {
                NavBar: NavBar,
                default: Cafe,
                Footer: Footer,
            } 
        },
        {
            path: "/cafe",
            name: "Cafe",
            components: {
                NavBar: NavBar,
                default: Cafe,
                Footer: Footer,
            } 
        },
        {
            path: "/mail",
            name: "Mail",
            components: {
                NavBar: NavBar,
                default: Mail,
                Footer: Footer,
            } 
        },
        {
            path: "/blog",
            name: "Blog",
            components: {
                NavBar: NavBar,
                default: Blog,
                Footer: Footer,
            } 
        },
        {
            path: "/tellMe",
            name: "TellMe",
            components: {
                NavBar: NavBar,
                default: TellMe,
                Footer: Footer,
            } 
        },

    ],
})