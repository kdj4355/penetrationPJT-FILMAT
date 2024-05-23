<template>
  <div v-if="store.actors">
    <h1>영화배우 목록</h1>
    <div class="d-flex flex-wrap">
      <ActorCard
        v-for="actor in store.actors"
        :actor="actor"
        />
    </div>
  </div>
</template>

<script setup>
import ActorCard from '@/components/ActorComponent/ActorCard.vue'
import { useCounterStore } from '@/stores/counter';
import { onMounted } from 'vue';

const store = useCounterStore()

onMounted(() => {
  store.getActors()
})
</script>

<style scoped>

</style>