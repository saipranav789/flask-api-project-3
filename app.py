from flask import Flask, request, jsonify
import secrets
import datetime
import threading
import json

app = Flask(__name__)

# File names for storing posts and users
POSTS_FILE = "posts.json"
USERS_FILE = "users.json"

# Lock object to manage access to global state
lock = threading.Lock()

# Admin key for deleting any posts.
admin_key = "adminUserKey--NONE"


# TODO :if required define posts and users list here

@app.post('/post')
def create_post():
    # Checking if request data is a valid JSON object
    if not request.is_json:
        return jsonify({'err': 'Invalid request data'}), 400

    # Getting the message from the request body
    msg = request.json.get('msg')

    # Getting user info
    user_name = request.json.get('user')

    if user_name is None:
        user_name = "default"

    # Checking if message is present and is a string
    if not msg or not isinstance(msg, str):
        return jsonify({'err': 'Message field is missing or not a string'}), 400

    with lock:
        # Loading posts from file
        try:
            with open(POSTS_FILE, "r") as f:
                posts = json.load(f)
        except FileNotFoundError:
            posts = []

        # Generating unique post ID
        post_id = len(posts) + 1

        # Generating a unique key for the post
        key = secrets.token_hex(16)

        try:
            with open(USERS_FILE, "r") as f:
                users = json.load(f)
        except FileNotFoundError:
            users = []

        # Setting values to null for default case.
        user_id = request.json.get('user_id')
        user_key = request.json.get('user_key')

        # Checking if message is present and is a string
        if not user_id or not isinstance(user_id, int):
            user_id = None

        # Checking if message is present and is a string
        if not user_key or not isinstance(user_key, str):
            user_key = None

        if user_id is not None and users == []:
            return jsonify({'err': 'No users created yet'}), 404
        elif user_id is not None:
            for user in users:
                if user_id == user['user_id']:
                    json_user_key = user['user_key']
                    if json_user_key != user_key:
                        return jsonify({'err': 'incorrect user key'}), 404

        # Getting current timestamp
        timestamp = datetime.datetime.utcnow().replace().isoformat()

        # Creating the post object
        post = {
            'id': post_id,
            'key': key,
            'timestamp': timestamp,
            'msg': msg,
            'user': user_name,
            'user_id': user_id,
            'user_key': user_key
        }

        # Saving the post object in the file
        posts.append(post)
        post_copy = {k: v for k, v in post.items() if k != 'user_key'}

        with open(POSTS_FILE, "w") as f:
            json.dump(posts, f)

        # Returning the post object as JSON with 200 status code (created)
        return jsonify(post_copy), 200


@app.get('/post/<int:post_id>')
def get_post(post_id):
    with lock:
        # Loading posts from file
        try:
            with open(POSTS_FILE, "r") as f:
                posts = json.load(f)
        except FileNotFoundError:
            return jsonify({'err': 'Post not found'}), 404

        # Checking if post exists
        if post_id < 1 or post_id > len(posts):
            return jsonify({'err': 'Post not found'}), 404

        for post in posts:
            if post['id'] == post_id:
                filtered_post = {k: v for k, v in post.items() if k not in ('user_key', 'key')}

        # Returning the post object copy as JSON
        return jsonify(filtered_post)


@app.get('/posts_by_user')
def get_post_by_user():
    with lock:
        # Loading posts from file
        is_user_key = 0
        all_posts = []
        try:
            with open(POSTS_FILE, "r") as f:
                posts = json.load(f)
        except FileNotFoundError:
            return jsonify({'err': 'Post not found'}), 404

        user_key = request.json.get('user_key')

        if not user_key or not isinstance(user_key, str):
            return jsonify({'err': 'User is missing or not a string'}), 400

        # fetch all posts under a particular user key and exclude 'user_key' and 'key' fields
        for post in posts:
            if post['user_key'] == user_key:
                is_user_key = 1
                filtered_post = {k: v for k, v in post.items() if k not in ('user_key', 'key')}
                all_posts.append(filtered_post)

        if is_user_key == 0:
            return jsonify({'err': 'Incorrect user key entered'}), 404

        # Returning the post object copy as JSON
        return jsonify(all_posts)


@app.delete('/post/<int:post_id>/delete/<key>')
def delete_post(post_id, key):
    with lock:
        # Reading the posts data from the file
        with open(POSTS_FILE, 'r') as f:
            posts = json.load(f)

        is_post_id = 0
        is_key = 0

        # Checking if post exists

        for post in posts:
            if post['id'] == post_id:
                is_post_id = 1
                break
        if is_post_id != 1:
            return jsonify({'err': 'Post not found'}), 404

        for post in posts:
            if post['key'] == key:
                is_key = 1
                break
            elif post['user_key'] == key:
                is_key = 1
                break

        if is_key != 1 and key != "adminUserKey--"+key:
            return jsonify({'err': 'incorrect key'}), 404

        # Getting the post object from the dictionary
        id_to_delete = post_id
        key_to_delete = key
        i = 0
        for post in posts:
            if post['id'] == id_to_delete:
                deleted_post = post
                del posts[i]
                break
            else:
                i = i + 1
        # Deleting the post object from the dictionary
        # del posts[str(post_id)]

        # Writing the updated posts data back to the file
        with open(POSTS_FILE, 'w') as f:
            json.dump(posts, f)

        post_copy = {k: v for k, v in post.items() if k != 'user_key'}

        # Returning the deleted post object as JSON
        return jsonify(post_copy)


@app.get('/admin')
def admin():
    with lock:
        global admin_key
        with open(POSTS_FILE, 'r') as f:
            posts = json.load(f)

        # Creating a copy of the posts dictionary
        posts_copy = posts.copy()

        # Fetching user id from message body.
        user_key = request.json.get('user_key')

        # Checking if message is present and is a string
        if not user_key or not isinstance(user_key, str):
            user_key = None

        if user_key is not None:
            admin_key = "adminUserKey--"+user_key

        # Returning the modified posts dictionary as JSON
        return jsonify(posts_copy)


@app.get('/posts_by_date')
def get_posts_by_date():
    with lock:
        start = request.args.get('start')
        end = request.args.get('end')

        if start:
            start = datetime.datetime.fromisoformat(start)
        if end:
            end = datetime.datetime.fromisoformat(end)

        if start and end and start > end:
            return "Error: 'start' time cannot be after 'end' time", 400

        with open(POSTS_FILE, 'r') as f:
            posts = json.load(f)

        filtered_posts = []
        for post in posts:
            timestamp = datetime.datetime.fromisoformat(post['timestamp'])

            if start and timestamp < start:
                continue
            if end and timestamp >= end:
                continue

            filtered_post = {k: v for k, v in post.items() if k not in ('user_key', 'key')}
            filtered_posts.append(filtered_post)

        return jsonify(filtered_posts)


@app.post('/createUser')
def create_user():
    # Checking if request data is a valid JSON object
    if not request.is_json:
        return jsonify({'err': 'Invalid request data'}), 400

    with lock:
        # Loading users from file
        try:
            with open(USERS_FILE, "r") as f:
                users = json.load(f)
        except FileNotFoundError:
            users = []

        # Generating unique user ID
        user_id = len(users) + 1

        # Generating a unique key for the user
        user_key = secrets.token_hex(16)

        # Creating the user object
        user = {
            'user_id': user_id,
            'user_key': user_key,
        }

        # Saving the user object in the file
        users.append(user)
        with open(USERS_FILE, "w") as f:
            json.dump(users, f)

        # Returning the user object as JSON with 200 status code (created)
        return jsonify(user), 200


@app.route('/<path:path>')
def catch_all(path):
    return jsonify({'error': 'Not found'}), 404


if __name__ == '__main__':
    app.run(debug=False)