import { createRouter, createWebHistory } from 'vue-router'
import MovieView from '@/views/MovieView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ActorListView from '@/views/ActorListView.vue'
import ActorDetailView from '@/views/ActorDetailView.vue'
import ReviewListView from '@/views/ReviewListView.vue'
import ReviewDetailView from '@/views/ReviewDetailView.vue'
import ReviewCreateView from '@/views/ReviewCreateView.vue'
import ReviewUpdateView from '@/views/ReviewUpdateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'
import ProfileView from '@/views/ProfileView.vue'
import ProfileUpdateView from '@/views/ProfileUpdateView.vue'
import PasswordChangeView from '@/views/PasswordChangeView.vue'
import AiRecommendView from '@/views/AiRecommendView.vue'
import { useCounterStore } from '@/stores/counter'
import HomeView from '@/views/HomeView.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    // 첫 화면
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    // 영화 페이지(서브홈)
    {
      path: '/movie',
      name: 'movieView',
      component: MovieView,      
    },   
    // 영화 상세 페이지
    {
      path: '/movie/:id',
      name: 'movieDetailView',
      redirect: { name: 'reviewListView' },
      component: MovieDetailView,      
      children: [
        // 영화 리뷰 게시글 전체
        {
          path: '',
          name: 'reviewListView',
          component: ReviewListView
        },
        // 영화 리뷰 게시글 생성 페이지
        {
          path: '/movie/:id/review/create',
          name: 'reviewCreateView',
          component: ReviewCreateView
        },
        // 영화 리뷰 게시글 수정 페이지
        {
          path: '/movie/:id/review/:reviewId/update',
          name: 'reviewUpdateView',
          component: ReviewUpdateView
        },
        // 영화 리뷰 상세 페이지
        {
          path: '/movie/:id/review/:reviewId',
          name: 'reviewDetailView',
          component: ReviewDetailView,   
        },
      ]
    },
    // 영화 배우 목록 페이지
    {
      path: '/actor',
      name: 'actorListView',
      component: ActorListView
    },
    // 영화 배우 상세 페이지
    {
      path: '/actor/:id',
      name: 'actorDetailView',
      component: ActorDetailView
    },

    // 회원 가입 페이지
    {
      path: '/signup',
      name: 'signUpView',
      component: SignUpView
    },
    // 로그인 페이지
    {
      path: '/login',
      name: 'loginView',
      component: LoginView
    },
    // 프로필 페이지
    {
      path: '/profile',
      name: 'profileView',
      component: ProfileView
    },
    {
      path: '/profile/:username/update',
      name: 'profileUpdateView',      
      component: ProfileUpdateView
    },
    {
      path: '/profile/:username/passwordchange',
      name: 'passwordChangeView',      
      component: PasswordChangeView
    },
    // AI 영화 추천(chat bot) 페이지
    {
      path: '/airecommend',
      name: 'airecommendView',
      component: AiRecommendView
    },
  ]
})

router.beforeEach((to, from) => {
  const store = useCounterStore()

  // 인증되지 않은 사용자는 프로필 페이지에 접근할 수 없음
  if (to.name === 'profileView' && store.isLogin === false) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }

  // 인증된 사용자는 회원가입과 로그인 페이지에 접근할 수 없음
  if ((to.name === 'signUpView' || to.name === 'loginView') && (store.isLogin === true)) {
    window.alert('이미 로그인이 되어있습니다.')
    return { name: 'movieView'}
  }
})


export default router
