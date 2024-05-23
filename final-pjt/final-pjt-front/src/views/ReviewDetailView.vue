<template>
  <div v-if="store.review">
    <div class="d-flex align-items-center mb-2">
      <h3 class="me-3">{{ store.review.title }}</h3>
      <button
        v-if="store.isLogin && store.review.user.id !== store.userInfo.id"
        @click="toggleLike"
        class="heart-button"
        style="background-color: transparent; border: none"
      >
        <i
          style="font-size: 2rem"
          :class="[
            'bi',
            reviewIsLiked ? 'bi-suit-heart-fill' : 'bi-suit-heart',
            'text-danger',
            'heart-icon',
          ]"
        ></i>
      </button>
      <div class="d-flex align-items-center" style="margin-left: auto">
        <i
          class="d-flex align-items-center bi bi-person-badge"
          style="font-size: 1.5rem"
        ></i>
        <h4 class="ms-1 m-0">{{ store.review.user.nickname }}</h4>
      </div>
    </div>
    <p v-if="store.isLogin">
      {{
        reviewLikeCount
          ? `${reviewLikeCount}명이 이 리뷰를 좋아합니다`
          : "좋아요가 없습니다."
      }}
    </p>
    {{ formatDate(store.review.created_at) }}
    <div class="mb-2">
      <i
        v-for="_ in store.review.rating"
        class="bi bi-star-fill text-warning"
      ></i>
    </div>

    <h4 class="">{{ store.review.content }}</h4>

    <div class="d-flex justify-content-end">
      <RouterLink
        v-if="store.review.user.id === store.userInfo.id"
        class="btn btn-info me-2"
        :to="{
          name: 'reviewUpdateView',
          params: { reviewId: store.review.id },
        }"
      >
        리뷰 수정
      </RouterLink>
      <button
        v-if="store.review.user.id === store.userInfo.id"
        @click="deleteReview"
        class="btn btn-danger me-2"
      >
        리뷰 삭제
      </button>
      <button @click="store.goback" class="btn btn-primary">뒤로가기</button>
    </div>

    <!-- 리뷰 댓글 -->
    <RouterView />
  </div>
</template>

<script setup>
import { useCounterStore } from "@/stores/counter";
import { useRoute, useRouter } from "vue-router";
import { ref, onMounted, watch, onUnmounted } from "vue";
import axios from "axios";

const route = useRoute();
const router = useRouter();
const store = useCounterStore();

// 작성일 형식 변경 함수
const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toISOString().slice(0, 10); // YYYY-MM-DD 형식으로 변환
}

onMounted(() => {
  store.getReviewDetail(route.params.reviewId);
});
onUnmounted(() => {
  store.review = null;
});

const reviewIsLiked = ref(false);
const reviewLikeCount = ref(0);

const toggleLike = function () {
  axios({
    method: "post",
    url: `http://127.0.0.1:8000/api/v1/community/review/${store.review.id}/like/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      const { liked, liked_count } = res.data;
      console.log("좋아요 성공", res);
      store.getLoginUserInfo(); // 좋아요 누르고 로그인 유저 정보 갱신
      reviewIsLiked.value = liked;
      reviewLikeCount.value = liked_count;
    })
    .catch((err) => {
      console.log("좋아요 실패", err);
    });
};

const initializeLikeStatusReview = () => {
  if (store.review && store.review.like_users) {
    if (store.review.like_users.includes(store.userInfo.id)) {
      reviewIsLiked.value = true;
    } else {
      reviewIsLiked.value = false;
    }
    console.log("리뷰 좋아요 상태 업데이트");
    reviewLikeCount.value = store.review.like_users.length;
  }
};

onMounted(() => {
  store.getMovie(route.params.id);
});

watch(
  () => store.review,
  (newReview) => {
    if (newReview) {
      initializeLikeStatusReview();
    }
  }
);

const deleteReview = function () {
  axios({
    method: "delete",
    url: `http://127.0.0.1:8000/api/v1/community/review/${store.review.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log("리뷰 삭제 완료", res);
      store.getMovie(route.params.id);
      store.getLoginUserInfo();
      router.push({ name: "reviewListView", params: { id: store.movie.id } });
    })
    .catch((err) => {
      console.log("리뷰 삭제 실패", err);
      window.alert("본인의 리뷰만 삭제 가능합니다.");
    });
};
</script>

<style scoped></style>
