<template>
  <div>
    <div class="mb-5">
      <h1 class="mb-3">상영 중인 영화</h1>
      <NowPlayingMovieList :movies="store.nowPlayingMovies" />
    </div>

    <div v-if="store.isLogin && store.recommendMovies" class="mb-5">
      <h1 class="mb-2">
        <span class="text-warning" style="font-weight: 800;">{{ store.userInfo.nickname }}</span
        >님을 위한 추천 영화
      </h1>
      <RecommendMovieList
        v-if="store.recommendMovies.length"
        :movies="store.recommendMovies"
      />

      <RouterLink
        style="text-decoration: none; color: white"   
        :to="{ name: 'profileView' }"
        v-else
      >
        <h4>
          FILMAT에서 영화를 추천 받기 위해서
          <span style="color: red">선호하는 장르</span>를 선택해주세요
        </h4>
      </RouterLink>
    </div>

    <div class="mb-5">
      <h1 class="mb-3"><span style="color: rgb(0, 225, 255); font-weight: 800;">FILMAT</span> 영화</h1>
      <MovieList :movies="store.movies" />
    </div>

    <div class="mb-5">
      <h1 class="mb-3">인기 영화 <span style="color: red; font-weight: 800;">TOP</span> 20</h1>
      <PopularityMovieList :movies="store.popularityMovies" />
    </div>

    <div class="mb-5">
      <h1 class="mb-3">평점 높은 영화 <span style="color: red; font-weight: 800;">TOP</span> 20</h1>
      <VoteAverageMovieList :movies="store.voteAverageMovies" />
    </div>
  </div>
</template>

<script setup>
import MovieList from "@/components/MovieComponent/MovieList.vue";
import PopularityMovieList from "@/components/MovieComponent/PopularityMovieList.vue";
import VoteAverageMovieList from "@/components/MovieComponent/VoteAverageMovieList.vue";
import NowPlayingMovieList from "@/components/MovieComponent/NowPlayingMovieList.vue";
import RecommendMovieList from "@/components/MovieComponent/RecommendMovieList.vue";
import { onMounted } from "vue";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();

onMounted(() => {
  store.getNowPlayingMovies();
  store.getRecommendMovies();
  store.getMovies();
  store.getPopularityMovies();
  store.getVoteAverageMovies();
  store.getGenres();
});
</script>
