var Post = (function() {
    function postHtml(data) {
        let image = '';
        if (data.image !== undefined && data.image !== null && data.image !== '') {
            image = `<img src='${data.image}' />`;
        } 

        const html = `
            <div class="blog-post">
                <h2 class="blog-post-title">
                <a href="${location.toString()}">${data.title}</a>
                </h2>
                <p class="blog-post-meta">${data.created} by <a href="#">${data.username}</a></p>
                ${image}
                <p>${data.description}</p>
            </div>
        `;

        return html;
    }

    /**
     * @var initPost
     * @description Init the post
     * @var postId {int} Post id
     */
    function initPost(postId) {
        fetch('/api/posts/' + postId)
        .then(response => response.json())
        .then(function(data) {
            const html = postHtml(data);

            document.querySelector('#post').innerHTML = html;
        });
    }

    /**
     * @method createPost
     * @description Create post
     */
    function createPost() {
        const csrfToken = getCookie('csrftoken');
        const id = Math.floor(Math.random() * 1000000).toString();
        const data = {
            'title': 'Title' + id,
            'description': 'Description: ' + id,
            'user': 1,
        };

        fetch('api/posts/', {
            method: 'POST', // or 'PUT'
            body: JSON.stringify(data), // data can be `string` or {object}!
            headers:{
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            }
        }).then(res => res.json())
        .catch(error => console.error('Error:', error))
        .then(function(response) {
            const obj = document.querySelector('#new-posts'); 
            let posts = obj.innerHTML;

            const html = postHtml(response);
            const newHtml = html + posts;
            obj.innerHTML = newHtml;
        });
    }

    /**
     * @method deletePost
     * @description Delete post
     * @param {*} postId 
     */
    function deletePost(postId) {
        if (confirm('¿Desea eliminar el post?')) {
            const csrfToken = getCookie('csrftoken');

            fetch('/api/posts/' + postId, {
                method: 'DELETE', // or 'PUT'
                headers:{
                    'X-CSRFToken': csrfToken
                }
            }).then(res => res.json())
            .catch(error => console.error('Error:', error))
            .then(function(response) {
                window.location.href = '/';
            });
        }
    }

    return {
        initPost: initPost,
        createPost: createPost,
        deletePost: deletePost,
    }
})();