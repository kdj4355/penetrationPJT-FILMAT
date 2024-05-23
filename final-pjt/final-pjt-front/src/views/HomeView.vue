<template>
  <div class="background-container rounded">
    <div class="overlay"></div>
    <div class="content">
      
      <h1 class="hometitle">FIL<span style="color: rgb(250, 216, 25);">M</span>AT</h1>
      <RouterLink class="link" :to="{ name: 'movieView'}">영화</RouterLink>
      <RouterLink class="link" :to="{ name: 'actorListView'}">영화 배우</RouterLink>
      <RouterLink class="link" :to="{ name: 'airecommendView'}"
        >AI에게 영화 추천 받기</RouterLink
      >
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from "vue-router";
</script>

<style scoped>

.hometitle {
  font-size: 300px;
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  
  font-weight: 800;
  color: #ffffffd7; /* 글자 색상 설정 */
  
  text-shadow: 
  
  0 0 5px #000000,     
  0 0 10px #000000, 
  0 0 15px black,
  0 0 20px black,  
  0 0 30px rgb(0, 0, 0),  
  0 0 50px rgb(0, 0, 0)
}


.background-container {
  position: relative; /* 자식 요소의 절대 위치를 설정하기 위해 상대 위치로 설정 */
  background-image: url("/filmatBackGround4.jpg"); /* 배경 이미지 경로 */
  background-size: cover; /* 배경 이미지가 컨테이너를 덮도록 설정 */
  background-position: center; /* 배경 이미지가 중앙에 위치하도록 설정 */
  background-repeat: no-repeat; /* 배경 이미지가 반복되지 않도록 설정 */
  width: 100%; /* 필요에 따라 조정 */
  height: 100vh; /* 필요에 따라 조정 */
  display: flex; /* 배치 조정을 위한 Flexbox 설정 */
  justify-content: center; /* 자식 요소들을 수직 중앙에 배치 */
  align-items: center; /* 자식 요소들을 수평 중앙에 배치 */
  color: rgba(255, 255, 255, 0.911); /* 텍스트 색상 설정 */
}

.overlay {
  margin-left: auto;
  margin-right: auto;
  position: absolute; /* 배경 오버레이를 배경 이미지 위에 덮기 위해 절대 위치로 설정 */
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  background-color: rgba(0, 0, 0, 0.678); /* 반투명한 검정색 오버레이 */
  z-index: 1; /* 오버레이를 다른 내용 앞에 위치시키기 위한 설정 */
}

.content {
  position: relative; /* content 요소를 상대 위치로 설정 */
  z-index: 2; /* 오버레이 위에 위치시키기 위한 설정 */
  display: flex; /* Flexbox 설정 */
  flex-direction: column; /* 자식 요소들을 수직 방향으로 정렬 */
  align-items: center; /* 자식 요소들을 수평 중앙에 배치 */
}

.link {
  margin: 10px; /* 링크 간 간격 설정 */
  font-size: 40px; /* 텍스트 크기 설정 */
  font-weight: 500;
  text-decoration: none; /* 텍스트 밑줄 제거 */
  color: inherit; /* 부모 요소의 색상 상속 */
  text-shadow: 
  
  0 0 5px #000000,    
  0 0 10px #000000, 
  0 0 15px black,
  0 0 20px black,  
  0 0 30px rgb(0, 0, 0),  
  0 0 50px rgb(0, 0, 0)
}
</style>
