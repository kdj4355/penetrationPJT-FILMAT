<template>
  <div class="d-flex justify-content-center align-items-center vh-100">
    <div class="card p-4" style="width: 400px;">
      <h1 class="text-center"><span style="font-weight: bold;">{{ route.params.username }}</span> 님</h1>
      <h1 class="text-center mb-4"> 회원 비밀번호 변경</h1>
      <form @submit.prevent="passwordChange">        
        <div class="form-group mb-3">
          <label for="password1">새 비밀번호</label>
          <input type="password" v-model.trim="password1" id="password1" class="form-control" required placeholder="Enter your password">
        </div>
        <div class="form-group mb-3">
          <label for="password2">새 비밀번호 확인</label>
          <input type="password" v-model.trim="password2" id="password2" class="form-control" required placeholder="Confirm your password">
          <div v-if="password1 !== '' && password1 !== password2" class="text-danger">비밀번호가 일치하지 않습니다.</div>
        </div>
        
        <button type="submit" class="btn btn-warning w-100">수정하기</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { useRoute } from 'vue-router'

const store = useCounterStore()
const route = useRoute()

onMounted(() => {
  store.getGenres()
})


const password1 = ref(null)
const password2 = ref(null)

const passwordChange = function () {
  const payload = {    
    password1: password1.value,
    password2: password2.value,    
  }
  store.passwordChange(payload)
}


</script>

<style scoped>

</style>