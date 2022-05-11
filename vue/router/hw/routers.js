import NavBar from "./components/NavBar.js"
import Half from "./components/Half.js"
import Pink from "./components/Pink.js"
import TellMe from "./components/TellMe.js"
import Footer from "./components/Footer.js"
export default new VueRouter({
    routes: [
        {
            path: "/",
            components: {
                NavBar: NavBar,
                default: Half,
                Footer: Footer,
            } 
        },
        {
            path: "/half",
            name: "Half",
            components: {
                NavBar: NavBar,
                default: Half,
                Footer: Footer,
            } 
        },
        {
            path: "/pink",
            name: "Pink",
            components: {
                NavBar: NavBar,
                default: Pink,
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