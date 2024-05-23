<template>
  <div class="mb-3">
    <div v-if="actor">
      <div ref="actorCard" class="card mx-1 border-dark" style="width: 15.5rem; position: relative; background-color: black;">
        <RouterLink :to="{ name: 'actorDetailView', params: { id: actor.id } }">
          <img
            :src="'https://image.tmdb.org/t/p/w500' + actor.profile_path"
            class="card-img-top"
            alt="..."
            style="height: 350px; object-fit: cover;"
          />
          <div class="card-body text-center">
            <h5 class="card-title">{{ actor.name }}</h5>
          </div>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  actor: Object
})

</script>

<style scoped>
.card-body {
  padding: 10px;
}

.card-title {
  font-size: 1.25rem;
  font-weight: bold;
  margin: 0;
  color: white; /* 배우 이름을 흰색으로 변경 */
}

.card-body {
  background-color: black; /* 카드 배경을 검은색으로 변경 */
}

a {
  text-decoration: none; /* 링크 밑줄 제거 */
}

a:hover {
  text-decoration: none; /* 링크 호버 시에도 밑줄 제거 */
  color: inherit; /* 호버 시에도 색상 변경 방지 */
}
</style>