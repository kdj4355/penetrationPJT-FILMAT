<template>
  <div v-if="store.userInfo" class="container mt-5">
    <div class="d-flex align-items-center">
      <h1>
        <span style="color: rgb(250, 216, 25); font-weight: bold">{{
          store.userInfo.nickname
        }}</span
        >님의 프로필
      </h1>
      <i
        class="ms-2 d-flex align-items-center bi bi-person-badge"
        style="font-size: 2.5rem"
      ></i>
    </div>

    <!-- <h3>팔로우 : {{ store.userInfo.followers.length }} 명</h3>
    <h3>팔로잉 : {{ store.userInfo.followings.length }} 명</h3> -->

    <hr class="border-top border-5 my-4" />
    <h3>
      좋아하는 장르
      <!-- <span class="me-3" v-for="genre in store.userInfo.like_genres">{{ genre.name }}</span> -->
    </h3>
    <SelectGenre />
    <hr class="border-top border-5" />
    <h3>좋아하는 영화</h3>
    <div class="d-flex flex-wrap" v-if="store.userInfo.like_movies.length">
      <MovieCard
        v-for="movie in store.userInfo.like_movies"
        :key="movie.id"
        :movie="movie"
      />
    </div>
    <div v-else>좋아요를 누른 영화가 없습니다.</div>

    <hr class="border-top border-5" />
    <h3>좋아하는 영화배우</h3>
    <div class="d-flex flex-wrap" v-if="store.userInfo.like_actors.length">
      <ActorCard
        v-for="actor in store.userInfo.like_actors"
        :key="actor.id"
        :actor="actor"
      />
    </div>
    <div v-else><p>좋아요를 누른 배우가 없습니다.</p></div>

    <hr class="border-top border-5" />

    <div>
      <h3>리뷰 목록</h3>
      <div v-if="store.userInfo.reviews.length">
        <div v-for="review in store.userInfo.reviews">
          <p>글 번호 : {{ review.id }}</p>
          <p>리뷰 제목 : {{ review.title }}</p>
          <p>리뷰 내용 : {{ review.content }}</p>
          <p>리뷰 생성일 : {{ formatDate(review.created_at) }}</p>
          <hr />
        </div>
      </div>
      <div v-else>
        <p>작성한 리뷰가 없습니다.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import MovieCard from "@/components/MovieComponent/MovieItemComponent/MovieCard.vue";
import ActorCard from "@/components/ActorComponent/ActorCard.vue";
import SelectGenre from "@/components/MovieComponent/SelectGenre.vue";
import { RouterLink } from "vue-router";

const store = useCounterStore();

// 작성일 형식 변경 함수
const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toISOString().slice(0, 10); // YYYY-MM-DD 형식으로 변환
};
</script>

<style scoped></style>
