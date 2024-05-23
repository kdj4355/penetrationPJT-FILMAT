<template>
  <div
    v-if="movies"
    id="movieCarouselNow"
    class="carousel slide"
    data-bs-ride="carousel"
    data-bs-interval="4000"
  >
    <div class="carousel-inner">
      <div
        class="carousel-item"
        v-for="(movieGroup, index) in movieGroups"
        :key="index"
        :class="{ active: index === currentSlideIndex }"
      >
        <div class="d-flex justify-content-center">
          <MovieCard
            v-for="movie in movieGroup"
            :key="movie.id"
            :movie="movie"
          />
        </div>
      </div>
    </div>
    <button
      class="carousel-control-prev"
      type="button"
      data-bs-target="#movieCarouselNow"
      data-bs-slide="prev"
    >
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">이전</span>
    </button>
    <button
      class="carousel-control-next"
      type="button"
      data-bs-target="#movieCarouselNow"
      data-bs-slide="next"
    >
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">다음</span>
    </button>
  </div>
</template>

<script setup>
import { onMounted, computed, nextTick } from "vue";
import MovieCard from "@/components/MovieComponent/MovieItemComponent/MovieCard.vue";
import { useCounterStore } from "@/stores/counter";
import { Carousel } from "bootstrap";

const props = defineProps({
  movies: Array,
});

const store = useCounterStore();

const currentSlideIndex = computed(() => store.nowPlayingMovieSlideIndex);

const movieGroups = computed(() => {
  let groups = [];
  for (let i = 0; i < props.movies.length; i += 5) {
    groups.push(props.movies.slice(i, i + 5));
  }
  return groups;
});

// 컴포넌트가 마운트되었을 때 실행
onMounted(async () => {
  await nextTick()

  const carouselElement = document.querySelector("#movieCarouselNow");
  const bootstrapCarousel = new Carousel(carouselElement, {
    wrap: true,
    pause: false,
  });

  // 저장된 슬라이드 인덱스로 이동
  bootstrapCarousel.to(currentSlideIndex.value);

  // 슬라이드 이벤트 리스너 추가
  carouselElement.addEventListener("slid.bs.carousel", (event) => {
    store.setNowPlayingIndex(event.to);
  });
});
</script>

<style scoped>
.carousel-control-prev,
.carousel-control-next {
  width: 5%; /* Adjust as needed */
}

.carousel-control-prev {
  left: -5%; /* Adjust to position the button outside the carousel */
}

.carousel-control-next {
  right: -5%; /* Adjust to position the button outside the carousel */
}
</style>