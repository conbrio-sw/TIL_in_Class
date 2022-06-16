
import Vue from "vue"; // defalut module
import VueRouter from "vue-router"; // installed module

Vue.use(VueRouter);

import MainPage from "@//components/MainPage";
import AddressSelect from "@/components/address/AddressSelect";

export default new VueRouter({
   routes: [
      {
         path: "/",
         component: MainPage,
      },

  {
     name: "AddressSelect",
     path: "/addressSelect",
     component: AddressSelect,
  },
   ],
});