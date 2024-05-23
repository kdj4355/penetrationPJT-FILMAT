<template>
  <div>
    <!-- <h1>선호하는 장르를 선택해주세요</h1> -->
    <div v-if="store.genres" class="d-flex flex-wrap">
      <div v-if="selectedGenres">
        <button
          class="m-1 btn btn-outline-warning text-white"
          v-for="genre in store.genres"
          :key="genre.id"
          :class="{ 'active': selectedGenres.includes(genre.id) }"
          @click="toggleGenre(genre.id)"
          data-bs-toggle="button"
        >
          {{ genre.name }}
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';
import { useCounterStore } from '@/stores/counter';
import axios from 'axios';

const store = useCounterStore();
let selectedGenres = ref(null);

const toggleGenre = (genreId) => {
  axios({
    method: 'post',
    url: `${store.BASE_URL}/api/v1/genre/${genreId}/like/`,
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
    .then((res) => {
      console.log(res)
      store.getLoginUserInfo();
    })
    .catch((err) => {
      console.log(err)
    })

};

onMounted(() => {
  store.getGenres();
  store.getLoginUserInfo();
});

watch(
  () => store.userInfo.like_genres,
  (newLikeGenres) => {
    if (newLikeGenres) {
      selectedGenres.value = newLikeGenres.map(genre => genre.id);
      console.log('선택된 장르 갱신 완료', selectedGenres.value)
    }
  }
);
</script>

<style scoped>

</style>