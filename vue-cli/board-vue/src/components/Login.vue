<template>
  <div class="container">
    <div class="mt-5 mb-3 d-flex justify-content-center">
      <h1 class="display-4">삐따기 세상</h1>
    </div>
    <div class="mb-3">
      <h2>Login</h2>
    </div>
    <div class="mb-3">
      <label for="userEmail" class="form-label">Email</label>
      <input
        type="email"
        class="form-control"
        id="userEmail"
        name="userEmail"
        v-model="userEmail"
      />
    </div>
    <div class="mb-3">
      <label for="userPassword" class="form-label">제목</label>
      <input
        type="password"
        class="form-control"
        id="userPassword"
        name="userPassword"
        v-model="userPassword"
      />
    </div>
    <div>
      <button @click="login" class="btn btn-primary">로그인</button>
      <!-- <a href="/register" class="btn btn-success">회원가입</a> -->
      <!-- eclipse 와 다른 부분 -->
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import VueAlertify from "vue-alertify";
Vue.use(VueAlertify);
import http from "@/common/axios.js";
export default {
  data() {
    return {
      userEmail: "hong@gildong.com",
      userPassword: "1234",
    };
  },
  methods: {
    login: async function () {
      try {
        let response = await http.post("/login", {
          userEmail: this.userEmail,
          userPassword: this.userPassword,
        });
        let { data } = response;
        //console.log(data);
        this.$emit("call-parent-loginSuccess", {
          userName: data.userName,
          userProfileImageUrl: data.userProfileImageUrl,
        });
        this.$router.push("/board");
      } catch (error) {
        console.error(error);
        if (error.response.status == "404") {
          this.$alertify.error("이메일 또는 비밀번호를 확인하세요.");
        } else {
          this.$alertify.error("서버 오류");
        }
      }
    },
  },
};
</script>

<style></style>
