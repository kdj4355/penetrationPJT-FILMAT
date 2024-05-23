<template>
  <div class="container mt-5">
    <h2 class="mb-4">리뷰 수정</h2>
    <form @submit.prevent="updateReview" class="row g-3">
      <div class="col-md-6">
        <label for="reviewTitle" class="form-label">제목</label>
        <input v-model="reviewTitle" type="text" class="form-control" id="reviewTitle" required>
      </div>
      <div class="col-md-12">
        <label for="reviewContent" class="form-label">리뷰 내용</label>
        <textarea v-model="reviewContent" class="form-control" id="reviewContent" rows="5" required></textarea>
      </div>
      <div class="col-12">
        <label class="form-label">별점</label>
        <div class="d-flex align-items-center">
          <span v-for="rating in 5" :key="rating" class="me-2">
            <input type="radio" :id="'rating-' + rating" v-model="selectedRating" :value="rating" required>
            <label :for="'rating-' + rating" class="star-label" role="button">{{ rating }}점</label>
          </span>
        </div>
      </div>
      <div class="col-12 d-flex justify-content-end">
        <button type="submit" class="btn btn-info me-2">수정하기</button>
        <button @click="store.goback" class="btn btn-primary">뒤로가기</button>
      </div>
    </form>
    
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const route = useRoute();
const router = useRouter();
const store = useCounterStore();
const reviewId = route.params.reviewId;
const reviewTitle = ref('');
const reviewContent = ref('');
const selectedRating = ref('');

// 리뷰 정보 가져오기
axios.get(`${store.BASE_URL}/api/v1/community/review/${reviewId}/`)
  .then(response => {
    const reviewData = response.data;
    reviewTitle.value = reviewData.title;
    reviewContent.value = reviewData.content;
    selectedRating.value = reviewData.rating;
  })
  .catch(error => {
    console.error('Error fetching review:', error);
  });

const updateReview = () => {
  axios.put(`${store.BASE_URL}/api/v1/community/review/${reviewId}/`, {
    title: reviewTitle.value,
    content: reviewContent.value,
    rating: selectedRating.value,
  }, {
    headers: {
      Authorization: `Token ${store.token}`
    }
  })
  .then(response => {
    console.log('리뷰 수정 완료', response.data);
    router.replace({ name: 'reviewDetailView', params: { id: route.params.id, reviewId: reviewId }});
  })
  .catch(error => {
    console.error('Error updating review:', error)
    window.alert('본인의 리뷰만 수정 가능합니다.')
    router.push({ name : 'reviewListView', params : { id: route.params.id }})   
  });
};
</script>

<style scoped>
.star-label {
  cursor: pointer;
  color: white; /* 텍스트 색상을 흰색으로 설정 */
}
</style>