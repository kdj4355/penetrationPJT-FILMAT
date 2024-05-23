<template>
  <div class="container mt-5">
    <div v-if="store.actor && actorInfo" >
      <div class="d-flex align-items-center mb-3">
        <h1 class="me-3">{{ store.actor.name }}</h1>
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
          배우 목록으로 돌아가기
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
        <div class="row mt-4">
          <div class="col-md-3">
            <img
              :src="
                'https://image.tmdb.org/t/p/w500' + store.actor.profile_path
              "
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
                인기도 :
                <span style="font-weight: normal">{{
                  store.actor.popularity.toFixed(0)
                }}</span>
              </h3>

              <h3 class="mb-3">
                생년월일 : 
                <span style="font-weight: normal">{{
                  actorInfo.birthday
                }}</span>
              </h3>

              <h3 class="mb-3">
                출생지 : 
                <span style="font-weight: normal">{{
                  actorInfo.place_of_birth
                }}</span>
              </h3>
            </div>
          </div>
        </div>
      </div>

      <div v-if="store.actor.movie.length">
        <hr class="border-top border-5 my-4" />
        <h3>출연 영화</h3>
        <div class="d-flex flex-wrap">
          <MovieCard v-for="movie in store.actor.movie" :movie="movie" />
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeMount, onBeforeUnmount, watch } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRoute } from "vue-router";
import MovieCard from "@/components/MovieComponent/MovieItemComponent/MovieCard.vue";
import axios from "axios";

const store = useCounterStore();
const route = useRoute();

const isLiked = ref(false);
const likeCount = ref(0);

const actorInfo = ref(null)

const toggleLike = function () {
  axios({
    method: "post",
    url: `http://127.0.0.1:8000/api/v1/actor/${store.actor.id}/like/`,
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
  if (store.userInfo === null) {
    return
  }
  
  if (store.actor && store.actor.like_users) {
    if (store.actor.like_users.includes(store.userInfo.id)) {
      isLiked.value = true;
    } else {
      isLiked.value = false;
    }
    console.log("좋아요 상태 업데이트");
    likeCount.value = store.actor.like_users.length;
  }
};

watch(
  () => store.actor,
  (newActor) => {
    if (newActor) {
      initializeLikeStatus();
      axios({
        method: "get",
        url: `https://api.themoviedb.org/3/person/${store.actor.id}`,
        params: {
          api_key: store.TMDB_API_KEY,
          language: "ko-KR",
        },
      })
        .then((res) => {
          console.log("배우 TMDB 정보 가져오기 성공", res.data);
          actorInfo.value = res.data
        })
        .catch((err) => {
          console.log(err);
        });
     
    }
  }
);

onMounted(() => {
  store.getActor(route.params.id)  
});

onBeforeUnmount(() => {
  store.actor = null;
});
</script>

<style scoped>
</style>
