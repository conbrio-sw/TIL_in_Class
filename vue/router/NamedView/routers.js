import NavBar from "./components/NavBar.js"
import Cafe from "./components/Cafe.js"
import Mail from "./components/Mail.js"
import Blog from "./components/Blog.js"
import TellMe from "./components/TellMe.js"
import Footer from "./components/Footer.js"
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