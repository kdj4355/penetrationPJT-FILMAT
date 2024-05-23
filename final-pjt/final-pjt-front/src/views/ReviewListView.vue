<template>
  <div>
    <h2 class="mb-0">리뷰 게시판</h2>
    <!-- 리뷰 생성 버튼 -->
    <div class="d-flex justify-content-end me-2 mb-2">
    <RouterLink v-if="store.isLogin" class="btn btn-success" :to="{ name: 'reviewCreateView' }">
      리뷰 작성하기
    </RouterLink>
    </div>
    
    <!-- 리뷰가 없을 때 메시지 -->
    <div v-if="store.movie.reviews.length === 0" class="text-center mb-3">
      <p>리뷰가 없습니다.</p>
    </div>
    
    <div v-else class="table-responsive rounded" style="background-color: #343a40; padding: 10px; border-radius: 10px;">
      <table class="table table-dark table-hover mb-0" style="border-radius: 10px; overflow: hidden;">
        <thead>
          <tr >
            <th class="text-center" scope="col" style="width: 5%;">글 번호</th>
            <th scope="col" style="width: 2%;"></th>
            <th scope="col" style="width: 40%;">제목</th>
            <th scope="col" style="width: 15%;">평점</th>
            <th scope="col" style="width: 15%;">글쓴이</th>
            <th class="text-center" scope="col" style="width: 8%;">작성일</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="review in store.movie.reviews" :key="review.id">
            <th class="text-center" scope="row">{{ review.id }}</th>
            <td class="text-center" scope="row"></td>
            
            <td><RouterLink class="text-decoration-none text-white font-weight-bold" :to="{ name: 'reviewDetailView', params: { reviewId: review.id }}">
              {{ review.title }}
            </RouterLink></td>
            <td>
              <i v-for="_ in review.rating" class="bi bi-star-fill text-warning"></i>
            </td>
            <td>{{ review.user.nickname }}</td>
            <td class="text-center">{{ formatDate(review.created_at) }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue';
import { RouterLink } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const store = useCounterStore();

// 작성일 형식 변경 함수
const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toISOString().slice(0, 10); // YYYY-MM-DD 형식으로 변환
}
</script>

<style scoped>
body {
  background-color: #1a1a1a;
}

.container {
  background-color: #2c2c2c;
  color: #f8f9fa;
  border-radius: 10px;
  padding: 20px;
}

.table-dark th,
.table-dark td {
  color: #f8f9fa;
}

.table-hover tbody tr:hover {
  background-color: #3a3a3a;
}

.text-light {
  color: #f8f9fa;
}

.text-decoration-none {
  text-decoration: none;
}

.btn-success {
  background-color: #28a745;
  border-color: #28a745;
}

.table-responsive {
  background-color: #343a40;
  padding: 10px;
  border-radius: 10px;
}

.table {
  border-radius: 10px;
  overflow: hidden;
}
</style>
