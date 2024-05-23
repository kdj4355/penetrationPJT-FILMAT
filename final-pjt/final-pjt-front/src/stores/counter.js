import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const router = useRouter()
  const BASE_URL = 'http://127.0.0.1:8000'  // django api server Base url
  const token = ref(null)                   // 로그인 유저 토큰

  const userInfo = ref(null)                // 로그인 한 유저 정보
  
  const nowPlayingMovies = ref(null)        // 현재 상영중인 영화 목록
  const movies = ref(null)                    // 전체 영화 목록
  const popularityMovies = ref(null)          // 인기 영화 목록
  const voteAverageMovies = ref(null)         // 평점 높은 영화 목록
  const recommendMovies = ref(null)         // 추천 영화 목록

  const movie = ref(null)                   // 영화 디테일 정보
  const review = ref(null)                  // 영화 리뷰 디테일 정보

  const genres = ref(null)                    // 전체 장르 목록
  const actors = ref(null)                    // 전체 영화 배우 목록
  const actor = ref(null)                   // 영화 배우 디테일 정보
  const movieSlideIndex = ref(0)            // 전체 영화 목록 캐러셀 현재 슬라이드 인덱스 상태
  const popularitySlideIndex = ref(0)       // 인기 영화 목록 캐러셀 현재 슬라이드 인덱스 상태
  const voteAverageSlideIndex = ref(0)      // 평점 높은 영화 목록 캐러셀 현재 슬라이드 인덱스 상태
  const nowPlayingMovieSlideIndex = ref(0)  // 현재 상영중인 영화 슬라이드 인덱스 상태
  const recommendMovieSlideIndex = ref(0)

  const TMDB_API_KEY = import.meta.env.VITE_TMDB_API_KEY;

  // 로그인 상태 확인
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })
  

  // 현재 상영중인 영화 목록 조회(TMDB api)
  const getNowPlayingMovies = function () {
    axios({
      method: 'get',
      url : `https://api.themoviedb.org/3/movie/now_playing`,
      params : {
        api_key: TMDB_API_KEY,
        language: 'ko-KR',
        region: 'KR',
        page: 1
      }
    })
    .then((res) => {
      console.log('현재 상영중인 영화 목록 가져오기 성공')
      console.log(res.data.results)
      nowPlayingMovies.value = res.data.results
    })
    .catch((err) => {      
      console.log('영화 목록 가져오기를 실패했습니다.', err)
    })
  }

  // 영화 전체 목록 조회
  const getMovies = function () {
    // 불러온 기록이 있다면 다시 요청하지 않음
    if (movies.value) {
      return
    }

    axios({
      method: 'get',
      url : `${BASE_URL}/api/v1/movie_list/`,
    })
    .then((res) => {
      console.log('전체 영화 목록 가져오기 성공')
      console.log(res.data)
      movies.value = res.data.slice(0, 50)
    })
    .catch((err) => {      
      console.log('전체 영화 목록 가져오기를 실패했습니다.', err)
    })
  }

  // 인기 영화 목록 조회 (상위 20개)
  const getPopularityMovies = function () {
    axios({
      method: 'get',
      url : `${BASE_URL}/api/v1/movie_list/popularity/`,
    })
    .then((res) => {
      console.log('인기 영화 목록 가져오기 성공')
      console.log(res.data)
      popularityMovies.value = res.data
    })
    .catch((err) => {      
      console.log('인기 영화 목록 가져오기를 실패했습니다.', err)
    })
  }

  // 평점 높은 영화 목록 (상위 20개)
  const getVoteAverageMovies = function () {
    axios({
      method: 'get',
      url : `${BASE_URL}/api/v1/movie_list/vote_average/`,
    })
    .then((res) => {
      console.log('평점 높은 영화 목록 가져오기 성공')
      console.log(res.data)
      voteAverageMovies.value = res.data
    })
    .catch((err) => {      
      console.log('영화 목록 가져오기를 실패했습니다.', err)
    })
  }
  
  // 추천 영화 목록
  const getRecommendMovies = function () {
    if (userInfo.value === null ) {
      return
    }

    axios({
      method: 'get',
      url : `${BASE_URL}/api/v1/recommended/`,
      headers : {
        'Authorization': `Token ${token.value}`
      }
    })
    .then((res) => {
      console.log('추천 영화 목록 가져오기 성공')
      console.log(res.data)
      recommendMovies.value = res.data
    })
    .catch((err) => {      
      console.log('영화 목록 가져오기를 실패했습니다.', err)
    })
  }

  // 영화 디테일 정보 조회
  const getMovie = function (movieId) {
    axios({
      method: 'get',
      url : `${BASE_URL}/api/v1/movie_list/${movieId}`,
    })
    .then((res) => {
      console.log('영화 디테일 정보 가져오기 성공')
      console.log(res.data)
      movie.value = res.data
    })
    .catch((err) => {      
      console.log('영화 디테일 정보 가져오기를 실패했습니다.', err)
    })
  }

  // 장르 전체 목록 조회
  const getGenres = function () {
    axios({
      method: 'get',
      url: `${BASE_URL}/api/v1/genre/`,
    })
      .then((res) => {
        console.log('장르 목록 가져오기 성공')
        console.log(res.data)
        genres.value = res.data
      })
      .catch((err) => {      
        console.log('장르 목록 가져오기를 실패했습니다.', err)
      })
  }

  // 영화 배우 전체 목록 조회
  const getActors = function () {
    // 불러온 기록이 있다면 다시 요청하지 않음
    if (actors.value) {
      return
    }

    axios({
      method: 'get',
      url: `${BASE_URL}/api/v1/actor/`,
    })
      .then((res) => {
        console.log('배우 목록 가져오기 성공')
        console.log(res.data)
        actors.value = res.data
      })
      .catch((err) => {      
        console.log('배우 목록 가져오기를 실패했습니다.', err)
      })
  }

  // 영화 배우 디테일 정보 조회
  const getActor = function (actorId) {
    axios({
      method: 'get',
      url: `${BASE_URL}/api/v1/actor/${actorId}/`,
    })
      .then((res) => {
        console.log('영화 배우 디테일 정보 가져오기 성공')
        console.log(res.data)
        actor.value = res.data
      })
      .catch((err) => {      
        console.log('영화 배우 디테일 정보 가져오기를 실패했습니다.', err)
      })
  }

  // 회원가입 
  const signUp = function (payload) {
    const { username, email, password1, password2, nickname } = payload
        
    axios({
      method: 'post',
      url: `${BASE_URL}/dj-rest-auth/registration/`,
      data: {

        username, email, password1, password2, nickname
      }
    })
      .then((res) => {
        console.log('회원가입 성공!')        
        const password = password1
        Login({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
  }
  const getLoginUserInfo = function () {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/profile/my_profile/`,
      headers: {
          Authorization: `Token ${token.value}`
        }
    })
    .then((res) => {
      console.log('로그인 유저 정보 가져오기 성공', res.data)            
      userInfo.value = res.data
    })
    .catch((error) => {
      console.log(error)
    })
  }

  // 회원 로그인
  const Login = function (payload) {
    // 1. 사용자 입력 데이터를 받아
    const { username, password } = payload
    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${BASE_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log('로그인 성공')
        token.value = res.data.key
        router.push({ name: 'home' })
        getLoginUserInfo()  // 로그인 후 유저 정보 가져오기
      })
      
  }
  
  // 회원 로그아웃
  const Logout = function () {   
    if (!token.value) return
    
    axios({
      method: 'post',
      url: `${BASE_URL}/accounts/logout/`,
      headers: {
        'Authorization': `Token ${token.value}`
      }
    })
      .then(() => {
        console.log('로그아웃 성공');
        token.value = null  // 토큰을 빈 값으로 설정  
        userInfo.value = null      
        router.push({ name: 'loginView' });  // 로그인 페이지로 리디렉션
    })
      .catch((err) => {
        console.log('로그아웃 실패:', err);
      })    
  }

  // 캐러셀 현재 슬라이드 인덱스를 설정하는 액션
  const setMovieSlideIndex = function (index) {
    movieSlideIndex.value = index;
  }

  const setPopularitySlideIndex = function (index) {
    popularitySlideIndex.value = index;
  }

  const setVoteAverageIndex = function (index) {
    voteAverageSlideIndex.value = index;
  }
  
  const setNowPlayingIndex = function (index) {
    nowPlayingMovieSlideIndex.value = index;
  }

  const setRecommendIndex = function (index) {
    recommendMovieSlideIndex.value = index;
  }

  const likeMovie = function (movieId) {
    axios({
      method: 'post',
      url: `${BASE_URL}/api/v1/movie_list/${movieId}/like/`,
      headers: {
        'Authorization': `Token ${token.value}`
      }
    })
      .then((res) => {
        console.log(`${movieId} 영화를 좋아요 목록에 등록하였습니다.`)
      })
      .catch((err) => {
        console.log('좋아요 목록에 등록 실패하였습니다.')
      })
  }
  const getReviewDetail = function (reviewId) {
    axios({
      method: 'get',
      url: `${BASE_URL}/api/v1/community/review/${reviewId}`    
    })
      .then((res) => {
        console.log('리뷰 상세 정보를 가져왔습니다.', res.data)
        review.value = res.data
      })
      .catch((err) => {
        console.log('리뷰 상세 정보 가져오기를 실패했습니다.', err)
      })
  }

  const goback = function () {
    router.go(-1)
  }

  const profileUpdate = function (payload) {
    const { nickname } = payload
    console.log(nickname)
    axios({
      method: 'put',
      url: `${BASE_URL}/api/v1/profile/my_profile/`,
      data: {
        nickname },
      headers: {
        'Authorization': `Token ${token.value}`      
      }
    })
      .then((res) => {
        console.log('회원정보 수정 성공', res.data)
        getLoginUserInfo()
        router.replace({ name : 'profileView' })
      })
      .catch((err) => {
        console.log('회원정보 수정 실패', err)
      })
  }

  const passwordChange = function (payload) {
    const { password1, password2 } = payload
    axios({
      method: 'post',
      url: `${BASE_URL}/dj-rest-auth/password/change/`,
      data: {
        new_password1 : password1,
        new_password2 : password2
      },
      headers: {
        'Authorization': `Token ${token.value}`      
      }
    })
      .then((res) => {
        console.log('비밀번호 변경 성공', res.data)
        Logout()
      })
      .catch((err) => {
        console.log('비밀번호 변경 실패', err)
      })
  }
  return { 
    BASE_URL, TMDB_API_KEY,
    getNowPlayingMovies, getMovies, getPopularityMovies, getVoteAverageMovies, getMovie, getRecommendMovies,    
    getGenres, 
    getActors, getActor,
    nowPlayingMovies, movies, popularityMovies, voteAverageMovies, movie, recommendMovies,
    genres, 
    actors, actor,
    token, 
    isLogin, 
    signUp, 
    Login, 
    Logout,
    movieSlideIndex, popularitySlideIndex, voteAverageSlideIndex, nowPlayingMovieSlideIndex, recommendMovieSlideIndex,
    setMovieSlideIndex, setPopularitySlideIndex, setVoteAverageIndex, setNowPlayingIndex, setRecommendIndex,
    likeMovie, 
    userInfo, getLoginUserInfo,
    getReviewDetail, review,
    goback,    
    profileUpdate, passwordChange
  }
}, { persist: true })
