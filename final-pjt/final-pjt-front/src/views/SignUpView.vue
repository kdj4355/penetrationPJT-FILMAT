<template>
  <div class="d-flex justify-content-center align-items-center vh-100">
    <div class="card p-4" style="width: 400px;">
      <h1 class="text-center mb-4">회원가입</h1>
      <form @submit.prevent="signUp">
        <div class="form-group mb-3">
          <label for="username">아이디</label>
          <input type="text" v-model.trim="username" id="username" class="form-control" required placeholder="아이디를 입력해주세요.">
        </div>
        <div class="form-group mb-3">
          <label for="email">이메일</label>
          <input type="email" v-model.trim="email" id="email" class="form-control" required placeholder="이메일을 입력해주세요.">
        </div>
        <div class="form-group mb-3">
          <label for="password1">비밀번호</label>
          <input type="password" v-model.trim="password1" id="password1" class="form-control" required placeholder="비밀번호를 입력해주세요.">
        </div>
        <div class="form-group mb-3">
          <label for="password2">비밀번호 확인</label>
          <input type="password" v-model.trim="password2" id="password2" class="form-control" required placeholder="비밀번호를 확인해주세요.">
          <div v-if="password1 !== '' && password1 !== password2" class="text-danger">비밀번호가 일치하지 않습니다.</div>
        </div>
        <div class="form-group mb-3">
          <label for="nickname">닉네임</label>
          <input type="text" v-model.trim="nickname" id="nickname" class="form-control" required placeholder="닉네임을 입력해주세요.">
        </div>
        <button type="submit" class="btn btn-warning w-100 ">가입하기</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
const store = useCounterStore()

onMounted(() => {
  store.getGenres()
})

const username = ref(null)
const email = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const nickname = ref(null)

const signUp = function () {
  const payload = {
    username: username.value,
    email: email.value,
    password1: password1.value,
    password2: password2.value,
    nickname: nickname.value
  }
  store.signUp(payload)
}


</script>

<style scoped>

</style>