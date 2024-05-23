<template>
  <div v-if="store.movie" class="container mt-5">
    <div class="d-flex align-items-center mb-3">
      <h1 class="me-3">{{ store.movie.title }}</h1>
      <!-- 좋아요 버튼 -->
      <button
        v-if="store.isLogin"
        @click="toggleLike"
        class="heart-button"
        style="background-color: transparent; border: none"
      >
        <i
          style="font-size: 2rem"
          :class="[
            'bi',
            isLiked ? 'bi-suit-heart-fill' : 'bi-suit-heart',
            'text-danger',
            'heart-icon',
          ]"
        ></i>
      </button>
      
      <button @click="store.goback" class="ms-auto btn btn-light">
        영화 목록으로 돌아가기
      </button>
    </div>
    <p v-if="store.isLogin">
      {{
        likeCount
          ? `${likeCount}명이 이 영화를 좋아합니다`
          : "좋아요가 없습니다."
      }}
    </p>

    <div class="d-flex">
      <p v-for="genre in movieGenres" class="genre-button">
        {{ genre }}
      </p>
    </div>

    <div class="row mt-4">
      <div class="col-md-3">
        <img
          :src="'https://image.tmdb.org/t/p/w500' + store.movie.poster_path"
          alt="Movie Poster"
          class="img-fluid"
          style="
            width: 100%;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
          "
        />
      </div>
      <div class="col-md-9">
        <div
          class="p-3"
          style="
            background-color: #000000;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
          "
        >
          <h3 class="mb-3">
            개봉일 :
            <span style="font-weight: normal">{{
              store.movie.released_date
            }}</span>
          </h3>
          <h3 class="mb-3">
            인기도 :
            <span style="font-weight: normal">{{
              store.movie.popularity.toFixed(0)
            }}</span>
          </h3>
          <h3 class="mb-3">
            평점 :
            <span style="font-weight: normal"
              >{{ store.movie.vote_average.toFixed(1) }} 점</span
            >
          </h3>
          <p>
            {{ store.movie.overview ? store.movie.overview : "..." }}
          </p>
        </div>
      </div>
    </div>

    <div v-if="store.movie.actors.length">
      <hr class="border-top border-5 my-4" />

      <h3>출연 배우</h3>
      <div class="d-flex flex-wrap">
        <ActorCard v-for="actor in store.movie.actors" :actor="actor" />
      </div>
    </div>

    <hr class="border-top border-5 my-4" />

    <!-- 유튜브 영상 띄우기 -->
    <h2>예고편</h2>
    <iframe
      width="100%"
      height="500"
      :src="'https://www.youtube.com/embed/' + videoId"
      frameborder="0"
      allowfullscreen
    ></iframe>

    <hr class="border-top border-5 my-4" />

    <!-- 리뷰 목록 -->
    <RouterView />
  </div>
  <div v-else class="container mt-5">영화정보가 없습니다.</div>
</template>

<script setup>
import { onMounted, onBeforeUnmount, watch, ref, nextTick } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRoute } from "vue-router";
import axios from "axios";
import { RouterView } from "vue-router";
import ActorCard from "@/components/ActorComponent/ActorCard.vue";

const videoId = ref(null);
const store = useCounterStore();
const route = useRoute();

const movieGenres = ref([]);

const isLiked = ref(false);
const likeCount = ref(0);

const toggleLike = function () {
  axios({
    method: "post",
    url: `http://127.0.0.1:8000/api/v1/movie_list/${store.movie.id}/like/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      const { liked, liked_count } = res.data;
      console.log("좋아요 성공", res);
      store.getLoginUserInfo(); // 좋아요 누르고 로그인 유저 정보 갱신
      isLiked.value = liked;
      likeCount.value = liked_count;
    })
    .catch((err) => {
      console.log("좋아요 실패", err);
    });
};

const initializeLikeStatus = () => {
  if (store.userInfo === null ) {
    return
  }
  if (store.movie && store.movie.like_users) {
    if (store.movie.like_users.includes(store.userInfo.id)) {
      isLiked.value = true;
    } else {
      isLiked.value = false;
    }
    console.log("좋아요 상태 업데이트");
    likeCount.value = store.movie.like_users.length;
  }
};

watch(
  () => store.movie,
  (newMovie) => {
    if (newMovie) {
      initializeLikeStatus();
      axios({
        method: "get",
        url: `https://api.themoviedb.org/3/movie/${store.movie.id}/videos`,
        params: {
          api_key: store.TMDB_API_KEY,
          language: "ko-KR",
        },
      })
        .then((res) => {
          console.log("비디오 아이디 가져오기 성공", res.data);
          videoId.value = res.data.results[0].key;
        })
        .catch((err) => {
          console.log(err);
        });
      store.movie.genres.forEach((genreId) => {
        const foundGenre = store.genres.find((genre) => genre.id === genreId);
        if (foundGenre) {
          movieGenres.value.push(foundGenre.name);
        }
      });
      console.log(movieGenres.value);
    }
  }
);

onMounted(() => {  
  store.getMovie(route.params.id);
});

onBeforeUnmount(() => {
  store.movie = null;
});
</script>

<style scoped>
.genre-button {
  display: inline-block;
  padding: 0.5rem 1rem;
  margin: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 0.25rem;
}
</style>
