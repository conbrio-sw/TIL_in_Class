<template>
  <div>
    <nav-bar :isLogin="isLogin" :userInfo="userInfo"></nav-bar>
    <router-view @call-parent-loginSuccess="loginSuccess"></router-view>
  </div>
</template>

<script>
import NavBar from "@/components/NavBar.vue";
export default {
  components: { NavBar },
  data() {
    return {
      isLogin: false,
      userInfo: {},
    };
  },
  methods: {
    loginSuccess: function (userInfo) {
      this.userInfo = userInfo;
      this.isLogin = true;
    },
  },
};
</script>

<style></style>
