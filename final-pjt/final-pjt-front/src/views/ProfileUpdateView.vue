<template>
  <div class="d-flex justify-content-center align-items-center vh-100">
    <div class="card p-4" style="width: 400px;">
      <h1 class="text-center"><span style="font-weight: bold;">{{ route.params.username }}</span> 님</h1>
      <h1 class="text-center mb-4"> 회원 정보 수정</h1>

      <form @submit.prevent="profileUpdate">
        <div class="form-group mb-3">
          <label for="nickname">닉네임</label>
          <input type="text" v-model.trim="nickname" id="nickname" class="form-control" required placeholder="Enter your nickname">
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

const nickname = ref(store.userInfo.nickname)

console.log(route.params.username)

const profileUpdate = function () {
  const payload = {
    nickname: nickname.value,    
  }
  store.profileUpdate(payload)
}


</script>

<style scoped>

</style>