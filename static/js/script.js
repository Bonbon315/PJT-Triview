'use strict';

const likeBtns = document.querySelectorAll('.like-btn');
// const likeIcon = document.querySelector('.like-icon');
const reviewLike = function (e) {
    axios({
        method: 'get',
        url: `/reviews/like/${e.target.dataset.reviewId}/`
    })
        .then(response => {
            if (response.data.isLiked === true) {
                e.target.children[0].classList.add('bi-hand-thumbs-up-fill');
                e.target.children[0].classList.remove('bi-hand-thumbs-up');
                e.target.classList.remove('btnW');
            } else {
                e.target.children[0].classList.add('bi-hand-thumbs-up');
                e.target.children[0].classList.remove('bi-hand-thumbs-up-fill');
                e.target.classList.add('btnW');
            }
            const likeCount = e.target.children[1]
            likeCount.innerText = response.data.likeCount;
        })
}
likeBtns.forEach(likeBtn => {
    likeBtn.addEventListener('click', reviewLike);
});

const form = document.querySelector('#follow-form');
form.addEventListener('submit', function (e) {
    e.preventDefault();
    const userId = e.target.dataset.userId;
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    axios({
        method: 'POST',
        url: `/accounts/${userId}/follow/`,
        headers: { 'X-CSRFToken': csrftoken, }
    })
        .then(response => {
            const isFollow = response.data.isFollow;
            const followBtn = document.querySelector('#follow-btn');
            if (isFollow === true) {
                followBtn.innerText = 'unfollow'
                followBtn.classList.add('btnW');
            } else {
                followBtn.innerText = 'follow'
                followBtn.classList.remove('btnW');

            }
            const followersCount = document.querySelector('#followers-count');
            const followingsCount = document.querySelector('#followings-count');
            const followersCountValue = response.data.followers_count;
            const followingsCountValue = response.data.followings_count;
            followersCount.innerText = followersCountValue;
            followingsCount.innerText = followingsCountValue;
        })
});



