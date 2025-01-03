# 10-pjt

# 영화 추천 사이트 'FILMAT' 프로젝트 
(24.05.16 ~ 24.05.23 / 2명)

## 프로젝트 배경

**"매일
뭘 먹을지 고민 중인 사람들…**

**맛집
찾아 다니는 사람들…**

**이젠**
영화도 맛집을 찾아야 한다."

선호하는 장르와 영화배우에 맞게 맛있게 영화를 추천해주는 'FILMAT'을 만들어보기로 했습니다.

## 팀 구성 및 역할

#### 김동준(팀장)

- Front-end 담당

- Back-end 보조

- Movie data 생성

- 프로젝트 활용 이미지 생성 (생성형 AI 사용) 및 사이트 로고 생성

#### 임형철(팀원)

- Back-end 담당

- AI Chat-Bot 구현

- Community dumy data 생성 (생성형 AI 사용)

- 발표 자료 작성 및 프로젝트 발표 

## 프로젝트 수행 절차 및 방법

#### Back-end

- 프로젝트 및 앱
  
  - 프로젝트 이름
    
    - final_pjt_back
  
  - 앱 이름
    
    - accounts
    
    - community
    
    - movies

#### Front-end

- 프로젝트 이름
  
  - final_pjt_front

## 프로젝트 수행 결과

- 추천 알고리즘을 통한 맞춤형 영화 리스트 추천

- 영화 목록 캐러셀로 구성 (현재 상영중, 영화 전체, 인기TOP20, 평점TOP20)

- 상세 영화 페이지, 상세 영화 배우 페이지 구현

- 상세 영화 페이지 리뷰 게시판 구현

- 프로필 페이지 구현

- AI chat bot 구현

#### 목표 서비스 구현 정도

기본 기능들에 대해서는 초기 설계했던 내용대로 모두 진행되었으며 상세 영화 리뷰의 댓글 기능과 네이버, 카카오, 구글 로그인 연동은 진행하지 못했습니다.

로그인 연동 기능은 많은 웹사이트에서 사용되는 기능이라 프로젝트 기간 이후에도 학습하여 구현할 필요가 있다고 생각됩니다.

#### 영화 추천 알고리즘에 대한 기술적 설명

기본적으로 선호하는 장르를 선택했을 때 알고리즘이 작동되도록 구현을 하였고 추가적으로 좋아요한 영화배우 정보도 받아서 필터링 후 인기도 및 평점 기준으로 내림차순으로 정렬하여 추천한 영화 리스트를 출력하도록 구성하였습니다. (첨부된 알고리즘 순서도 참고)

# 느낀 점

#### 김동준

- 우선 첫째도 설계, 둘째도 설계, 셋째도 설계인 것을 배웠습니다. 프론트와 백을 나눠서 프로젝트를 진행하면서 설계가 탄탄하지 않아 작업을 진행하는 도중 모델링을 재설계하고 url을 수시로 확인하면서 시간이 더 많이 걸리게 된 것 같습니다. 다음 프로젝트는 설계에 시간을 좀 더 투자하여 기초공사를 튼튼히 한 후에 코딩을 진행할 것 입니다.
  
  협업의 중요성과 협업 시 어떤 방식으로 소통을 진행해야 되는 지 배우게 된 것 같습니다. 막대한 양의 작업이었지만 둘이 나눠서 서로 피드백도 해주고 아이디어도 더 많이 나와서 프로젝트가 더 좋은 방향으로 진행되면서 잘 마무리 할 수 있었던 것 같습니다.
  
  Git을 통해 merge하면서 파일을 동기화하는 방법은 프로젝트를 하면서 배우게 되었지만 기능별로 명확히 구분을 하여 커밋을 하는 방식에 더 익숙해질 필요가 있고 버전관리에 대해서 추가적인 학습이 필요하다고 느꼈습니다.
  
  마지막으로 이번 프로젝트에서는 진행하지 못했지만 기능 구현 및 디자인을 마무리하고 리팩토링을 통해 성능을 더 효율적으로 발휘할 수 있도록 하는 방법들에 대해서도 추가적인 학습이 필요하다고 생각되었습니다.
  
  처음 진행하는 프로젝트라 힘들었지만 만들면서 즐거운 시간을 보낸 것 같습니다. 개발자로 직무를 바꾸는 것에 도전하기를 잘했다고 생각했고 앞으로도 많은 학습과 경험을 통해 사람들을 더 편하고 즐겁게 해줄 수 있는 개발자가 되겠습니다.

#### 임형철

- 이번 프로젝트를 진행하면서 기본기를 다시 다질 수 있었습니다. 다시 한번 기반이 약한 것을 알 수 있었고, job fair 기간에는 복습을 통해 기반을 튼튼하게 다져야 할 것 같습니다.
  Backend에서 모델링과 serializer에서 데이터를 넣는 법을 확실하게 알 수 있었습니다. 하지만 데이터를 받아 올 때 에러가 많이 떠서 모델링을 다시하고, dumy data도 필요한 데이터로 바꾸기 위해 시간을 많이 소모했었습니다. git을 통해 merge하면서 협업을 유연하게 할 수 있는 방법을 배웠습니다.
  마지막으로 소통을 하면서 서로의 의견에 대해 합의점을 찾고 목표를 향해 빠르게 나아갈 수 있어 협업의 중요성을 느낄 수 있었습니다.
