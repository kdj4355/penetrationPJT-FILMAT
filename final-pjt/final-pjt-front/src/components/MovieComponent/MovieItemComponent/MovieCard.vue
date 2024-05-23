<template>
  <div v-if="movie">
    <div class="card mx-1 mb-1 border-dark" style="width: 19rem; position: relative;">
      <RouterLink :to="{ name: 'movieDetailView', params: { id: movie.id } }" >
        <img height="450px" :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" class="card-img-top" alt="...">
      </RouterLink>
      <p v-if="topRanking" class="top-ranking">{{ topRanking }}</p>
    </div>      
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router';

defineProps({
  movie: Object,
  topRanking: Number
})

</script>

<style scoped>
.top-ranking {
  position: absolute;
  bottom: -50px;
  left: -35px;
  
  padding: 5px 10px;
  border-radius: 5px;
  font-weight:900;
  font-size: 120px;
  
  font-style: italic;

  color: white;
  text-shadow: 
  
  0 0 5px #000000,     
  0 0 10px #000000, 
  0 0 15px black
    
}
</style>