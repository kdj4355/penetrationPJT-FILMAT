<template>
  <div class="container mt-5">
    <h2 class="mb-4">리뷰 작성</h2>
    <form @submit.prevent="createReview" class="row g-3">
      <div class="col-md-6">
        <label for="reviewTitle" class="form-label">리뷰 제목</label>
        <input
          v-model="reviewTitle"
          type="text"
          class="form-control"
          id="reviewTitle"
          required
        />
      </div>
      <div class="col-md-12">
        <label for="reviewContent" class="form-label">리뷰 내용</label>
        <textarea
          v-model="reviewContent"
          class="form-control"
          id="reviewContent"
          rows="5"
          required
        ></textarea>
      </div>
      <div class="col-12">
        <label class="form-label">별점</label>
        <div class="d-flex align-items-center">
          <span v-for="rating in 5" :key="rating" class="me-4">
            <input
              class="me-1"
              type="radio"
              :id="'rating-' + rating"
              v-model="selectedRating"
              :value="rating"
              required
            />
            <label :for="'rating-' + rating" class="star-label" role="button"
              >{{ rating }} 점</label
            >
          </span>
        </div>
      </div>
      <div class="col-12 d-flex justify-content-end">
        <button type="submit" class="btn btn-success me-2">작성하기</button>
        <button @click="store.goback" class="btn btn-primary">뒤로가기</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { useCounterStore } from "@/stores/counter";
import { useRoute, useRouter } from "vue-router";

const route = useRoute();
const router = useRouter();
const store = useCounterStore();
const reviewTitle = ref("");
const reviewContent = ref("");
const selectedRating = ref("");

console.log(route.params.id);

const createReview = () => {
  console.log(
    reviewTitle.value,
    reviewContent.value,
    selectedRating.value,
    route.params.id
  );
  if (!selectedRating.value) {
    alert("별점을 선택해주세요.");
    return;
  }

  axios({
    method: "post",
    url: `${store.BASE_URL}/api/v1/community/review/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
    data: {
      title: reviewTitle.value,
      content: reviewContent.value,
      rating: selectedRating.value,
      movie: route.params.id,
    },
  })
    .then((res) => {
      console.log("리뷰 생성 완료", res.data);
      store.getMovie(route.params.id);
      store.getLoginUserInfo();
      router.push({ name: "reviewListView", params: { id: route.params.id } });
    })
    .catch((err) => {
      console.log("리뷰 생성 실패", err);
    });
};
</script>

<style scoped>
.star-label {
  cursor: pointer;
  color: white; /* 텍스트 색상을 흰색으로 설정 */
}
</style>
