<template>
  <div class="body bg-black text-white">
    <header>
      <nav class="navbar navbar-expand-sm fixed-top bg-black w-100 px-4" style="height: 70px;">
        <div class="container-fluid">
          <RouterLink
            class="navbar-brand text-white"
            aria-current="page"
            :to="{ name: 'home' }"
          >
            <img class="rounded" src="/logo1.png" alt="" width="110px">
          </RouterLink>

          <button
            class="navbar-toggler"
            type="button"
            @click="toggleNavbar"
            aria-controls="navbarNav"
            :aria-expanded="isNavbarExpanded"
            aria-label="Toggle navigation"
          >
            <span class="navbar-toggler-icon"></span>
          </button>

          <div :class="['collapse', 'navbar-collapse', { show: isNavbarExpanded }]" id="navbarNav">
            <ul class="navbar-nav me-auto">
              <li class="nav-item">
                <RouterLink
                  class="nav-link text-white"
                  aria-current="page"
                  :to="{ name: 'movieView' }"
                >영화</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink
                  class="nav-link text-white"
                  aria-current="page"
                  :to="{ name: 'actorListView' }"
                >배우</RouterLink>
              </li>
              <li class="nav-item">
                <RouterLink
                  class="nav-link text-white"
                  aria-current="page"
                  :to="{ name: 'airecommendView' }"
                >AI 추천</RouterLink>
              </li>
            </ul>
            <ul class="navbar-nav ms-auto">
              <li v-if="!store.isLogin" class="nav-item">
                <RouterLink class="nav-link text-white" :to="{ name: 'signUpView' }">회원가입</RouterLink>
              </li>
              <li v-if="!store.isLogin" class="nav-item">
                <RouterLink class="nav-link text-white" :to="{ name: 'loginView' }">로그인</RouterLink>
              </li>
              <li v-if="store.isLogin && store.userInfo" class="nav-item d-flex">
                <span class="my-auto me-3">{{ store.userInfo.nickname }}</span>
                <button class="btn btn-outline-light rounded-circle d-flex align-items-center justify-content-center p-0" id="profileDropdown" data-bs-toggle="dropdown" aria-expanded="false" style="width: 40px; height: 40px">
                  <i class="bi bi-person"></i>
                </button>
                <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="profileDropdown">
                  <li>
                    <RouterLink class="dropdown-item" :to="{ name: 'profileView' }">프로필</RouterLink>
                  </li>
                  <li>
                    <RouterLink class="dropdown-item" :to="{ name: 'profileUpdateView', params: { username: store.userInfo.username }}">회원정보 수정</RouterLink>
                  </li>
                  <li>
                    <RouterLink class="dropdown-item" :to="{ name: 'passwordChangeView', params: { username: store.userInfo.username }}">비밀번호 변경</RouterLink>
                  </li>
                  <li>
                    <button class="dropdown-item" @click="Logout">로그아웃</button>
                  </li>
                </ul>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </header>

    <main class="container" :style="mainStyle" style="max-width: 1600px; margin-top: 70px">
      <RouterView/>
    </main>

    <footer class="footer bg-dark text-light py-5 mt-5">
      <div class="container">
        <div class="row">
          <div class="col-md-4 mb-4">
            <h5 class="text-uppercase mb-3">사이트 정보</h5>
            <p>영화 추천 서비스</p>
            <p>
              최신 영화 정보와 추천 알고리즘을 통해 다양한 영화를 소개합니다.
            </p>
          </div>
          <div class="col-md-4 mb-4">
            <h5 class="text-uppercase mb-3">문의 및 지원</h5>
            <p>문의사항이나 피드백은 언제든지 환영합니다.</p>
            <p>              
              <div>김동준 팀장 kdj4355@naver.com</div>
              <div>임형철 팀원 dlagudcjf789@naver.com</div>
            </p>
          </div>
          <div class="col-md-4">
            <h5 class="text-uppercase mb-3">저작권 정보</h5>
            <p>&copy; 2024 FILMAT Company. All rights reserved.</p>
          </div>
        </div>
        <hr class="my-4" />
        <div class="row">
          <div class="col-md-6 mb-3 mb-md-0">
            <a @click.prevent="alert" href="">개인정보 처리방침</a>
          </div>
          <div class="col-md-6">
            <a @click.prevent="alert" href="">서비스 약관</a>
          </div>
        </div>
      </div>
    </footer>
  </div>

</template>

<script setup>
import { ref, computed, onMounted, nextTick } from 'vue';
import { useRouter, RouterLink, RouterView } from "vue-router";
import { useCounterStore } from "@/stores/counter";

const store = useCounterStore();
const router = useRouter();

const isNavbarExpanded = ref(false);

const toggleNavbar = () => {
  isNavbarExpanded.value = !isNavbarExpanded.value;
};

const mainStyle = computed(() => ({
  marginTop: isNavbarExpanded.value ? '200px' : '0px'  // 이 값을 navbar의 높이에 맞게 조정하세요.
}));

const Logout = function () {
  store.Logout();
};

const alert = function () {
  window.alert('준비중입니다.')
}

</script>

<style scoped>
.body {
  font-family: "Noto Sans KR", sans-serif;
  font-optical-sizing: auto;
  font-weight: weight;
  font-style: normal;
}

.btn-outline-light {
  border: none;
  padding: 0.5rem;
  font-size: 1.25rem;
}

.btn-outline-light:hover {
  background-color: white;
}
</style>
