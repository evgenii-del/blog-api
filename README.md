## Blog API

### How to start a project?

You have to clone the git repository

`git clone https://github.com/evgenii-del/blog-api.git`

Open the directory with the git repository and write the command:

`docker-compose up`

Congratulations! The project is running!

### How to use API?

https://newsboard.herokuapp.com/api/v1/posts/

All posts: GET `https://newsboard.herokuapp.com/api/v1/posts/`

Create new post: POST `https://newsboard.herokuapp.com/api/v1/posts/`

Update post: PUT `https://newsboard.herokuapp.com/api/v1/posts/<id of post>/`

Delete post: DELETE `https://newsboard.herokuapp.com/api/v1/posts/<id of post>/`

Create new comment: POST `https://newsboard.herokuapp.com/api/v1/comments/`

Update comment: PUT `https://newsboard.herokuapp.com/api/v1/comments/<id of comment>/`

Delete comment: DELETE `https://newsboard.herokuapp.com/api/v1/comments/<id of comment>/`

Vote: POST `https://newsboard.herokuapp.com/api/v1/posts/<id of post>/upvotes/`