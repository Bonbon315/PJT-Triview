# ✈Triview-Project

![Triview](https://img.shields.io/badge/Team-Triview-3879ff)
[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)
<br>🛠**Used Framework**<br>
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"><br>

> ⌛**period** 2022.10.31(MON)-2022.11.8(TUE)<br>
> ✨여행 리뷰 사이트 구현<br>

## 📚index

-   📃[Description](#Description)
-   📘[Content](#content)
-   👨‍👩‍👧‍👧[Contributor](#contributor)
-   ✉[Postscript](#Postscript)

### 📃Description

![Triview](tripreview.png)
⭐팀명 트리뷰는 trip+review의 합성어입니다.<br>
<br>
여행지 정보 및 후기 공유 커뮤니티 서비스를 만드는 것이 프로젝트의 목적이였기 때문에 팀명을 정하는 것에 많은 의견이 오갔습니다.<br>
그러다가 여행이라는 의미의 trip과 review를 같이 합쳐보는 것이 어떨까라는 의견이 나왔고, 결국 최종적으로 결정되었습니다.<br>
<br>
✍팀역할 분담에서<br>
<br>
🦄✨팀장 역할과 리뷰 기능 구현은 조본희씨가,<br>
🐨🌿발표자 역할과 리뷰 기능 구현에 유순일씨가,<br>
🐰🥕ppt 작성 역할과 프론트엔드 파트 전반과 디자인에 오채현씨가,<br>
🦝🍏readme 작성 역할과 회원 기능 구현에 권건희씨가,<br>
각각 담당해주셨습니다.<br>
<br>
📘content문단에서 본격적이고 최종적인 기능 구현에 대한 설명을 하기 전에<br>
📃Description문단에서 프로젝트 계획에 대한 내용을 전반적으로 서술하도록 하겠습니다.<br>
<br>
대략적인 팀 구조와 주제가 정해지고 난 후에 유사한 서비스들을 살펴보다가<br>
[마이리얼트립](https://www.myrealtrip.com/), [트립어드바이저](https://www.tripadvisor.co.kr/)를 참고, 분석하게 되었고,<br>
이것을 바탕으로 뼈대를 설계하기로 했습니다.<br>
그리하여 회원관리, 글 작성, 리뷰 확인으로 이루어진 기능의 큰 틀을 잡았습니다.<br>
그 틀을 기반으로 기능 구현과 관리의 편의성을 위해서 결정된 사항들은 아래와 같습니다.

-   DB영역
    -   Accounts
    -   Location
    -   Review
        <br>
-   화면 설계(트립어드바이저 참조)
    -   피그마를 이용하여 와이어 프레임을 생성
    -   메인 홈 화면
    -   리뷰 작성 페이지
    -   여행 정보, 리뷰 확인 페이지

### 📘content
![index](index.png)
<br><br>
❤대문으로 사용되는 index페이지인만큼 디자인 담당자분이 동적인 느낌으로 제작해 주셨습니다.❤<br><br>
![css](ani.png)
💖여기 보이는 네비게이션 바 안의 '여행'에 마우스 포인터를 가져가면 애니메이션 효과도 볼 수 있습니다.💖
<br><br>
![location](location.png)
<br><br>
🧡역시 location 페이지도 깔끔하고 세련되게 제작되어 있습니다.<br>
기능적인 부분은 review담당자분들이 힘써주셨고,<br> 
location db에 등록되어 들어있는 여러 장소들이 바로 나오는 구성으로 되어있습니다.<br>
여기서 장소 등록하기 버튼을 누르면 아래와 같은 화면이 뜹니다. 🧡
<br><br>
![location](글1.png)
<br><br>
💛도시,국가뿐 아니라 드롭다운 형식으로 카테고리도 선택할 수 있는 기능까지 넣었습니다💛
<br><br>
![location](글2.png)
<br><br>
💚이 밑으로는 대표이미지 선택 기능이 있고, 위도,경도를 추가할 수 있는 기능이 있는데 이걸 넣으면...💚
<br><br>
![location](location글.png)
<br><br>
🤍위도,경도를 지정한 것이 지도 위치로 나오게 됩니다.🤍
<br><br>
![location](locationreview2.png)
<br><br>
💜삭제나 수정도 글쓴 유저만 가능하게 해뒀습니다.💜
<br><br>
![location](locationreview.png)
<br><br>
🖤location 페이지 안에는 review 보기와 작성 기능이 있습니다.<br>
review를 보면서 좋아요도 누를 수 있습니다.<br>
좋아요의 비동기처리 기능은 디자인 담당자분께서 힘써주셨습니다.<br>
자기자신과 비회원은 좋아요를 누를수 없게 되어있습니다.<br>
리뷰 작성기능은 저 위에 보이는 리뷰 작성 버튼을 누르면 사용할 수 있습니다.🖤
<br><br>
![location](review.png)
<br><br>
💕여행일자 선택과 여행 유형 선택역시 드롭다운 형식으로 선택하는 기능이 들어가 있습니다!<br>
리뷰의 내용 이외에 이미지선택, 평점 기능도 들어가 있습니다. 그 중 평점 기능의 경우엔....
💕
<br><br>
![location](별점.png)
<br><br>💗총 합쳐서 별점이 나오도록 작동하고 있습니다!💗<br><br>
![account](profile.png)
<br><br>
💙유저프로필의 경우 기본적인 정보를 보여주는 것과 수정과 탈퇴, 팔로우 기능을 지원하고 있습니다.<br>
물론 좋아요와 같이, 자기자신과 가입되지 않은 유저는 할 수 없도록 되어 있습니다.💙
<br><br>
![account](profile-up.png)
<br><br>
💞수정페이지에서는 이와 같은 것들을 수정할 수 있습니다.💞
<br><br>
![account](profile-delete.png)
<br><br>
💝프로필 페이지 맨 밑에는 탈퇴 기능이 있습니다.💝
<br><br>

### 👨‍👩‍👧‍👧contributor

<a href="https://github.com/Bonbon315"><img src="https://avatars.githubusercontent.com/u/108643294?v=4" width="150" height="150"/></a>
<a href="https://github.com/chaehyun-oh"><img src="https://avatars.githubusercontent.com/u/108640873?v=4" width="150" height="150"/></a>
<a href="https://github.com/yoosoonil"><img src="https://avatars.githubusercontent.com/u/97111793?v=4" width="150" height="150"/></a>
<a href="https://github.com/Gkhy"><img src="https://avatars.githubusercontent.com/u/108653266?v=4" width="150" height="150"/></a>
<br>🌳🌷🌼🌻🌷🌼🌻🌷🌼🌻🌷🌼🌻🌷🌼🌻🌷🌼🌻🌷🌼🌻🌷🌼🌻🌷🌼🌻🌷🌼🌻🌷🌳

### ✉Postscript

| 👨‍👩‍👧‍👧조원         | ✏후기                                                                                                                        |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| 조본희🦄       | ✨팀원분들 정말 수고 많으셧습니다! 예비군때문에 중간에 하루 자리에 없었는데도 다들 잘 진행해주셔서 감사합니다!               |
| 유순일🐨       | 🌿부족한 점이 많아서 걸림돌이 되지 않을까 걱정되었지만, 이해해주시고 알려주셔서 프로젝트 잘 마칠 수 있었습니다! 감사합니다~! |
| 오채현🐰       | 🥕팀원분들 모두 맡은 역할을 잘 수행해주시고 적극적으로 프로젝트에 참여해주셔서 금방 끝난 것 같아요. 수고하셨습니다.👍        |
| 권건희🦝&nbsp; | 🍏열정있으시고 실력있으신 분들이랑 프로젝트해서 너무너무 행복했습니다! 많이 배우고 가요, 정말 감사드려요!                     |
