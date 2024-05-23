<template>
  <div class="d-flex justify-content-center align-items-center vh-100">
    <div class="card p-4" style="width: 400px">
      <h1 class="text-center mb-4">로그인</h1>
      <form @submit.prevent="Login">
        <div class="form-group mb-3">
          <label for="username">ID</label>
          <input
            type="text"
            id="username"
            v-model="username"
            class="form-control"
            placeholder="아이디를 입력해주세요."
          />
        </div>
        <div class="form-group mb-4">
          <label for="password">PASSWORD</label>
          <input
            type="password"
            id="password"
            v-model="password"
            class="form-control"
            placeholder="비밀번호를 입력해주세요."
          />
        </div>
        <button type="submit" class="btn btn-warning w-100">로그인</button>
        <div class="d-flex justify-content-center">
          <RouterLink
            :to="{ name: 'signUpView' }"
            class="btn btn-link text-center"
            style="              
              color: black;
              font-weight: 700;              
              text-decoration: none;
              width: auto;
              padding: 0;
              margin-top: 10px;
              text-align: center;
            "
          >
            회원가입
          </RouterLink>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import { RouterLink } from "vue-router";
const store = useCounterStore();

const username = ref(null);
const password = ref(null);

const Login = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.Login(payload);
};
</script>

<style scoped></style>
