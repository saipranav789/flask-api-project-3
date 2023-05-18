# CS515 WEBFORM FLASK SERVER

## Team Members :

> Sai Bandla CWID: 20011577
> Sagar Patnaik CWID: 20009862
> Rachana Zha CWID: 20016163

## Stevens login:

> sbandla@stevens.edu

## Github Repo:

> GITHUB REPO LINK : https://github.com/saipranav789/flask-api-project-3.git


## Hours Spent on project:

> 18 Hours

## How we tested our code:

> We tested our code using postman and by giving many different type of requests to our endpoints to test the various different extensions we have implemented.

## any bugs or issues we could not resolve:

> None we were able to resolve all issues

## an example of a difficult issue or bug and how you resolved

> A issue i resolved while making this project figuring out how to get the shell scripts to work.

## Baseline conditionality

Endpoint #1: Create a post (POST /post)
A POST request to /post should have a body consisting of a JSON object with a string-valued field called msg.

On success, returns a JSON object with at least three fields:

id: An integer
key: A long, unique random string (used to later delete the post)
timestamp: An ISO 8601 timestamp in UTC
On error, returns a JSON object with a field err that holds a string describing the error and a status 400 (indicating 'bad request').

Endpoint #2: Read a post (GET /post/{{id}})
A GET request to /post/{{id}} looks up the given integer id.

On success, returns a JSON object with at least three fields:

id: An integer
timestamp: An ISO 8601 timestamp in UTC
msg: A string
On error, returns a JSON object with a field err that holds a string describing the error and a status 404 (indicating 'not found').

Endpoint #3: Delete a post (DELETE /post/{{id}}/delete/{{key}})
A DELETE request to /post/{{id}}/delete/{{key}} is meant to delete the post with id.

On success, returns a JSON object with at least three fields:

id: An integer
key: A long, unique random string (used to later delete the post)
timestamp: An ISO 8601 timestamp in UTC
On error, returns a JSON object with a field err that holds a string describing the error and a status 404 (indicating 'not found') or 403 (indicating 'forbidden').


## a list of extensions I have chosen to implement, with appropriate detail on them for the CAs to evaluate them

Extensions

## 1. Users and user keys

This extension adds a notion of user with a private user key.

Posts can be associated with a user by providing the user id and corresponding user key when creating the post.
Information about a post associated with a user should return the associated user id.
If a user created a post, it should be sufficient to provide the user’s key to delete the post.
There should be some way to create users.


## 2. User profiles (needs user)

This extension adds metadata to users.

User creation must specify a unique piece of metadata (e.g., username or email).
There should be an API endpoint to retrieve a given user’s metadata given their id or unique metadata.
There should be an API endpoint to edit a given user’s metadata (requires the user’s key).
When returning information about a post associated with a user, include the user’s unique metadata.


## 3. Date- and time-based range queries

This extension adds an API endpoint to search for posts based on a date/time.

Search with a starting date and time, an ending date and time, or both.
The endpoint should return a list of post information (e.g., id, message, timestamp, user).


## 4. Moderator role

This extension adds an "admin" role, which allows designated users to view all posts with their associated keys. This feature can be useful for monitoring the content of the platform, as well as managing and moderating posts.

Implementation Details:
The implementation of the admin role is done through the /admin endpoint, which is a GET request. Only users with the admin key can access this endpoint.
The admin key is defined as a global variable in the code:

> admin_key = "adminKey"


## 5. Persistence

> This extension is implemented using a file system to store the data posted to the server. Using the file system will retain the data in the files in the form of JSON data. When the server is restarted we will have retained all the data in files thus resulting in no data loss.


TEST CASES:


url : http://127.0.0.1:5000/post
request type :POST
in msg body : 
msg--required
user name , user id and user key--optional

1)http://127.0.0.1:5000/post
{
    "msg":"Hello1"
}

{
    "id": 27,
    "key": "9abf68bfa5d58959b021d2b47c36b5a9",
    "msg": "Hello1",
    "timestamp": "2023-05-02T02:06:49.795983",
    "user": "default",
    "user_id": null
}

2)
{
    "msg":"Hello2"
}
{
    "id": 27,
    "key": "9abf68bfa5d58959b021d2b47c36b5a9",
    "msg": "Hello1",
    "timestamp": "2023-05-02T02:06:49.795983",
    "user": "default",
    "user_id": null
}

3)

{
    "msg":"Hello2"
}



{
    "id": 28,
    "key": "ab5ef9793877bbd361e2c2814ed08a1d",
    "msg": "Hello2",
    "timestamp": "2023-05-02T02:07:28.976367",
    "user": "default",
    "user_id": null
}


4)Error
{
"msg":""
}
{
    "err": "Message field is missing or not a string"
}

5)
{

}

{
    "err": "Message field is missing or not a string"
}

6)
{
    "msg":"Helloo"
}

{
    "id": 29,
    "key": "839d5177d4639336ccee1933d52754fa",
    "msg": "Helloo",
    "timestamp": "2023-05-02T02:08:01.053655",
    "user": "default",
    "user_id": null
}

7){
    "msg":"Hellooo"
}

{
    "id": 30,
    "key": "bb5a4cb08b6c3512d816c6b0d1775451",
    "msg": "Hellooo",
    "timestamp": "2023-05-02T02:08:49.017123",
    "user": "default",
    "user_id": null
}


8)
{
    "msg":"Hellooo"
}
{
    "id": 31,
    "key": "3d3c754cc8b2c924f7de2bc12b12cbcd",
    "msg": "Hellooo",
    "timestamp": "2023-05-02T02:08:59.368765",
    "user": "default",
    "user_id": null
}

9){
    "msg":"Hellooo"
}

{
    "id": 32,
    "key": "72a7cbd50a116ee6406acad1dd8445b3",
    "msg": "Hellooo",
    "timestamp": "2023-05-02T02:09:37.484870",
    "user": "default",
    "user_id": null
}


10){
    "msg":"Hellooo"
}
{
    "id": 33,
    "key": "1e5f25f9249174122f02f0315ebd8a15",
    "msg": "Hellooo",
    "timestamp": "2023-05-02T02:09:52.537777",
    "user": "default",
    "user_id": null
}


============================================================================================================

get post by id

url : http://127.0.0.1:5000/post/provide post id here
request type :GET
in msg body : 
nothing required




1.)
http://127.0.0.1:5000/post/1

{
    "id": 1,
    "msg": "Hey one",
    "timestamp": "2023-05-01T23:56:54.001570",
    "user": "default",
    "user_id": null
}

2.)
http://127.0.0.1:5000/post/88

{
    "err": "Post not found"
}

3)http://127.0.0.1:5000/post/0
{
    "err": "Post not found"
}

4)http://127.0.0.1:5000/post/29

{
    "id": 29,
    "msg": "Helloo",
    "timestamp": "2023-05-02T02:08:01.053655",
    "user": "default",
    "user_id": null
}

5.)http://127.0.0.1:5000/post/30
{
    "id": 30,
    "msg": "Hellooo",
    "timestamp": "2023-05-02T02:08:49.017123",
    "user": "default",
    "user_id": null
}

6)http://127.0.0.1:5000/post/31
{
    "id": 31,
    "msg": "Hellooo",
    "timestamp": "2023-05-02T02:08:59.368765",
    "user": "default",
    "user_id": null
}

7)http://127.0.0.1:5000/post/3144

{
    "err": "Post not found"
}

8)http://127.0.0.1:5000/post/0989765
{
    "err": "Post not found"
}

9)http://127.0.0.1:5000/post/28
{
    "id": 28,
    "msg": "Hello2",
    "timestamp": "2023-05-02T02:07:28.976367",
    "user": "default",
    "user_id": null
}

10)http://127.0.0.1:5000/post/27
{
    "id": 27,
    "msg": "Hello1",
    "timestamp": "2023-05-02T02:06:49.795983",
    "user": "default",
    "user_id": null
}
===============================================================================================================================================================================================================

CREATE USER

url : http://127.0.0.1:5000/createUser
request type : POST
in msg body : 
nothing required

Type: POST 

1.)
http://127.0.0.1:5000/createUser

{
    "user_id": 1,
    "user_key": "50759d9cfa20ebd26b4f21d430f81549"
}    

2.)http://127.0.0.1:5000/createUser
{
    "user_id": 3,
    "user_key": "98684645a1de2c4eb50012fa2c1b0ad0"
}
3.)http://127.0.0.1:5000/createUser

{
    "user_id": 4,
    "user_key": "1551f0cfb25dce23107983316317b6ae"
}

4.)http://127.0.0.1:5000/createUser
{
    "user_id": 5,
    "user_key": "24e08b4ed2c3c8da232be52e3d20d93f"
}
5.)http://127.0.0.1:5000/createUser
{
    "user_id": 6,
    "user_key": "fd2183d19e931a5875b6433ea8d8363f"
}
6.)http://127.0.0.1:5000/createUser
{
    "user_id": 7,
    "user_key": "470c0f4782b9f11c3811f164e2b2afa2"
}
7.)http://127.0.0.1:5000/createUser
{
    "user_id": 8,
    "user_key": "1151310dc82fa8d24c731c5ec8e1f873"
}
8.)http://127.0.0.1:5000/createUser
{
    "user_id": 9,
    "user_key": "9a78aaf696b98889e9129b5df3bf798f"
}
9.)http://127.0.0.1:5000/createUser
{
    "user_id": 10,
    "user_key": "6a1014e7128c0704627b7eab7f8d66f2"
}
{
    "user_id": 11,
    "user_key": "8ca101d2c3e4e8a8c1601abcbdbf760f"
}
{
    "user_id": 12,
    "user_key": "c9ffa50c9b6d3cee1238fe27b81f5a78"
}
{
    "user_id": 13,
    "user_key": "6180fdebd29154e227ea2e4012b798ae"
}
{
    "user_id": 14,
    "user_key": "6972b96cc3207dc984608ed8d6cc6b38"
}
{
    "user_id": 15,
    "user_key": "4b2a15d4ad068ef0142ffd6fb6d58791"
}
{
    "user_id": 16,
    "user_key": "59300d86b5a475daad985501cae3f945"
}
{
    "user_id": 17,
    "user_key": "2a15597f57deb274ad5b83481dc79dc3"
}
{
    "user_id": 18,
    "user_key": "3b0ead6a26cb45a1debf3f908cad5c50"
}
{
    "user_id": 19,
    "user_key": "59f3f28e7dd9ec15b6ce665b8228089a"
}
{
    "user_id": 20,
    "user_key": "3a7f9fed8351be72f9d20a115ce100f5"
}

======================================================================================================================================================================================

get posts_by_user

url : http://127.0.0.1:5000/createUser
request type : GET
in msg body : user_key required

http://127.0.0.1:5000/posts_by_user

1)
{
    "userd":848451212
}
{
    "err": "User key is missing or not a string"
}


2)
{
    "user_key":"6a1014e7128c0704627b7eab7f8d66f2"
}
[
    {
        "id": 34,
        "msg": "Hellooo",
        "timestamp": "2023-05-02T02:15:08.064467",
        "user": "default",
        "user_id": 10
    },
    {
        "id": 35,
        "msg": "Hellooo msg 2",
        "timestamp": "2023-05-02T02:15:22.714307",
        "user": "default",
        "user_id": 10
    },
    {
        "id": 36,
        "msg": "Hellooo msg 3",
        "timestamp": "2023-05-02T02:15:32.283274",
        "user": "default",
        "user_id": 10
    },
    {
        "id": 37,
        "msg": "Hellooo msg 3",
        "timestamp": "2023-05-02T02:34:54.660130",
        "user": "default",
        "user_id": 10
    },
    {
        "id": 38,
        "msg": "Hellooo msg 3",
        "timestamp": "2023-05-02T02:34:55.476273",
        "user": "default",
        "user_id": 10
    }
]

3)

{
    "user_key":"50759d9cfa20ebd26b4f21d430f81549"
}
[
    {
        "id": 21,
        "msg": "Hello",
        "timestamp": "2023-05-02T01:51:01.760568",
        "user": "default",
        "user_id": 1
    }
]

4)
{
    "user_key":"50759d9cfa20ebd26b4f21d430f815492"
}

{
    "err": "Incorrect user key entered"
}

5)
{

}
{
    "err": "User is missing or not a string"
}

==========================================================================================================

delete :
type:delete

DELETE

url : http://127.0.0.1:5000/post/post_id/delete/key or user key
request type : DELETE
in msg body : nothing required
in url : post id and post key or user key or admin key required
in msg body : nothing required


url: 

1.)wrong post id
http://127.0.0.1:5000/post/34/delete/6a1014e7128c0704627b7eab7f8d66f

{
    "err": "Post not found"
}

2) wrong key

http://127.0.0.1:5000/post/33/delete/6a1014e7128c0704627b7eab7f8d66f
{
    "err": "incorrect key"
}


3)http://127.0.0.1:5000/post/33/delete/6a1014e7128c0704627b7eab7f8d66f2
output :
{
    "id": 33,
    "key": "1e5f25f9249174122f02f0315ebd8a15",
    "msg": "Hellooo",
    "timestamp": "2023-05-02T02:09:52.537777",
    "user": "default",
    "user_id": null
}

4)http://127.0.0.1:5000/post/32/delete/6a1014e7128c0704627b7eab7f8d66f2
{
    "id": 32,
    "key": "72a7cbd50a116ee6406acad1dd8445b3",
    "msg": "Hellooo",
    "timestamp": "2023-05-02T02:09:37.484870",
    "user": "default",
    "user_id": null
}

5)http://127.0.0.1:5000/post/31/delete/6a1014e7128c0704627b7eab7f8d66f2
{
    "id": 31,
    "key": "3d3c754cc8b2c924f7de2bc12b12cbcd",
    "msg": "Hellooo",
    "timestamp": "2023-05-02T02:08:59.368765",
    "user": "default",
    "user_id": null
}


==============================================================================================================================================

/admin:
type : GET

url : http://127.0.0.1:5000/post/post_id/delete/adminKey
url fields required - post id and adminkey
msg body : nothing required

1.)delete using admin key:

http://127.0.0.1:5000/post/30/delete/adminKey

{
    "id": 30,
    "key": "bb5a4cb08b6c3512d816c6b0d1775451",
    "msg": "Hellooo",
    "timestamp": "2023-05-02T02:08:49.017123",
    "user": "default",
    "user_id": null
}

2) View all posts:
[
    {
        "id": 1,
        "key": "2f70524db5ed35632285e8383a02266b",
        "msg": "Hey one",
        "timestamp": "2023-05-01T23:56:54.001570",
        "user": "default",
        "user_id": null,
        "user_key": null
    },
    {
        "id": 2,
        "key": "83026866db1dc75f5038cf33b3173d4e",
        "msg": "Hey two",
        "timestamp": "2023-05-01T23:57:31.113452",
        "user": "default",
        "user_id": null,
        "user_key": null
    },
    {
        "id": 3,
        "key": "b27fb757e0822c8cfe5e839eb92f4169",
        "msg": "Hey 3",
        "timestamp": "2023-05-01T23:58:11.864497",
        "user": "default",
        "user_id": null,
        "user_key": null
    },
    {
        "id": 4,
        "key": "d14bd5344b50c65d790c2fa282423066",
        "msg": "hey",
        "timestamp": "2023-05-02T00:04:46.588800",
        "user": "default",
        "user_id": null,
        "user_key": null
    },
    {
        "id": 5,
        "key": "d9c97eb7cd14fe7fedb651de59eb7e78",
        "msg": "This is a demo post",
        "timestamp": "2023-05-02T00:08:22.023926",
        "user": "default",
        "user_id": null,
        "user_key": null
    },
    {
        "id": 6,
        "key": "8346bfa287df8c468c24a53660747cf0",
        "msg": "This is a demo post",
        "timestamp": "2023-05-02T00:16:13.804881",
        "user": "default",
        "user_id": null,
        "user_key": null
    },
    {
        "id": 7,
        "key": "d6c4f4af99ff3744b2e22f3326fbbaa7",
        "msg": "This is a demo post",
        "timestamp": "2023-05-02T00:27:24.323687",
        "user": "default",
        "user_id": null,
        "user_key": "12342635"
    },
    {
        "id": 8,
        "key": "949517b55188c2d36d8b989f46e7fa1d",
        "msg": "This is a demo post",
        "timestamp": "2023-05-02T00:27:50.029000",
        "user": "default",
        "user_id": 23,
        "user_key": "12342635"
    },
    {
        "id": 9,
        "key": "876bbf569109f4cc422dafb71b7f8ad4",
        "msg": "This is a demo post",
        "timestamp": "2023-05-02T00:29:12.756097",
        "user": "default",
        "user_id": 23,
        "user_key": "12342635"
    },
    {
        "id": 10,
        "key": "3e4f8c6ee09a87b1d92f5ffce3cd5e28",
        "msg": "This is a demo post",
        "timestamp": "2023-05-02T00:29:16.949288",
        "user": "default",
        "user_id": 23,
        "user_key": "12342635"
    },
    {
        "id": 11,
        "key": "bcc91c90edc0db9f040627f1d4406a8b",
        "msg": "This is a demo post",
        "timestamp": "2023-05-02T00:30:52.099321",
        "user": "default",
        "user_id": 23,
        "user_key": "12342635"
    },
    {
        "id": 12,
        "key": "3faf058b1e9976a7f10cc41836119dc5",
        "msg": "This is a demo post",
        "timestamp": "2023-05-02T00:31:18.475610",
        "user": "default",
        "user_id": 23,
        "user_key": "12342635"
    },
    {
        "id": 13,
        "key": "c002dbd26e45213cb49aa1552caa7c99",
        "msg": "This is a demo post",
        "timestamp": "2023-05-02T00:31:55.795090",
        "user": "default",
        "user_id": 23,
        "user_key": "12342635"
    },
    {
        "id": 14,
        "key": "51de3fdc79d01c4aa51ab10df35db819",
        "msg": "hello",
        "timestamp": "2023-05-02T00:57:14.885728",
        "user": "default",
        "user_id": null,
        "user_key": null
    },
    {
        "id": 15,
        "key": "8877d2b80b7065af6e6c0e0abd2d556e",
        "msg": "hello",
        "timestamp": "2023-05-02T01:07:19.902546",
        "user": "default",
        "user_id": 4,
        "user_key": "376473"
    },
    {
        "id": 16,
        "key": "c8ee7d12ccdd5e93fd42748a960fe095",
        "msg": "hello",
        "timestamp": "2023-05-02T01:15:01.592800",
        "user": "default",
        "user_id": 4,
        "user_key": "376473"
    },
    {
        "id": 17,
        "key": "4d07f2e0d11c13c716f039e23be98b44",
        "msg": "hello",
        "timestamp": "2023-05-02T01:17:19.703355",
        "user": "default",
        "user_id": 4,
        "user_key": "376473"
    },
    {
        "id": 18,
        "key": "38b4c59b87c572168ac031d54d34b03d",
        "msg": "hello",
        "timestamp": "2023-05-02T01:17:41.040424",
        "user": "default",
        "user_id": 4,
        "user_key": "376473"
    },
    {
        "id": 19,
        "key": "9ab880b601323de878fc11b4b9beb93f",
        "msg": "hello123",
        "timestamp": "2023-05-02T01:22:53.004640",
        "user": "default",
        "user_id": null,
        "user_key": null
    },
    {
        "id": 20,
        "key": "5e79aa7b53612ff878681a9a6800d07f",
        "msg": "hello1234",
        "timestamp": "2023-05-02T01:24:23.541754",
        "user": "default",
        "user_id": null,
        "user_key": null
    },
    {
        "id": 21,
        "key": "4df6f043102e937ea0a045908cd848cd",
        "msg": "Hello",
        "timestamp": "2023-05-02T01:51:01.760568",
        "user": "default",
        "user_id": 1,
        "user_key": "50759d9cfa20ebd26b4f21d430f81549"
    },
    {
        "id": 22,
        "key": "a462de5da4d4e35f22825696702d7048",
        "msg": "Hello",
        "timestamp": "2023-05-02T01:51:47.792468",
        "user": "default",
        "user_id": 3,
        "user_key": "98684645a1de2c4eb50012fa2c1b0ad0"
    },
    {
        "id": 23,
        "key": "a37e7a2e94c997881cfd53ea81f8e3c0",
        "msg": "Hello123",
        "timestamp": "2023-05-02T01:57:23.040212",
        "user": "default",
        "user_id": 5,
        "user_key": "24e08b4ed2c3c8da232be52e3d20d93f"
    },
    {
        "id": 24,
        "key": "a1f48c7b3f5682a56604ee7279943468",
        "msg": "Hello123",
        "timestamp": "2023-05-02T01:58:40.354600",
        "user": "default",
        "user_id": 5,
        "user_key": "24e08b4ed2c3c8da232be52e3d20d93f"
    },
    {
        "id": 25,
        "key": "c661e522771234f219fd56d8c7f89a0d",
        "msg": "Hello123",
        "timestamp": "2023-05-02T01:59:58.407851",
        "user": "default",
        "user_id": 5,
        "user_key": "24e08b4ed2c3c8da232be52e3d20d93f"
    },
    {
        "id": 26,
        "key": "025fbad35e254d8cb1dc0fc9d0a2693f",
        "msg": "Hello123",
        "timestamp": "2023-05-02T02:05:26.825426",
        "user": "default",
        "user_id": 5,
        "user_key": "24e08b4ed2c3c8da232be52e3d20d93f"
    },
    {
        "id": 27,
        "key": "9abf68bfa5d58959b021d2b47c36b5a9",
        "msg": "Hello1",
        "timestamp": "2023-05-02T02:06:49.795983",
        "user": "default",
        "user_id": null,
        "user_key": null
    },
    {
        "id": 28,
        "key": "ab5ef9793877bbd361e2c2814ed08a1d",
        "msg": "Hello2",
        "timestamp": "2023-05-02T02:07:28.976367",
        "user": "default",
        "user_id": null,
        "user_key": null
    },
    {
        "id": 29,
        "key": "839d5177d4639336ccee1933d52754fa",
        "msg": "Helloo",
        "timestamp": "2023-05-02T02:08:01.053655",
        "user": "default",
        "user_id": null,
        "user_key": null
    },
    {
        "id": 35,
        "key": "de1ee511c40c1fd27b7e07cd52edbcc5",
        "msg": "Hellooo msg 2",
        "timestamp": "2023-05-02T02:15:22.714307",
        "user": "default",
        "user_id": 10,
        "user_key": "6a1014e7128c0704627b7eab7f8d66f2"
    },
    {
        "id": 36,
        "key": "68706c0f0b679ef36301ec889191cef7",
        "msg": "Hellooo msg 3",
        "timestamp": "2023-05-02T02:15:32.283274",
        "user": "default",
        "user_id": 10,
        "user_key": "6a1014e7128c0704627b7eab7f8d66f2"
    },
    {
        "id": 37,
        "key": "5c1e5dc3f5c5a7fe1ecbe129e29e3ef2",
        "msg": "Hellooo msg 3",
        "timestamp": "2023-05-02T02:34:54.660130",
        "user": "default",
        "user_id": 10,
        "user_key": "6a1014e7128c0704627b7eab7f8d66f2"
    },
    {
        "id": 38,
        "key": "bcd09ac7b63efaf6341d4290a70dccd1",
        "msg": "Hellooo msg 3",
        "timestamp": "2023-05-02T02:34:55.476273",
        "user": "default",
        "user_id": 10,
        "user_key": "6a1014e7128c0704627b7eab7f8d66f2"
    }
]


==============================================================================================================================================================================================================================================

get posts by date
Type :Get

URL : http://localhost:5000/posts_by_date?start=2023-05-01T23:56:54.001570&end=2023-05-02T00:04:46.588800
[
    {
        "id": 1,
        "msg": "Hey one",
        "timestamp": "2023-05-01T23:56:54.001570",
        "user": "default",
        "user_id": null
    },
    {
        "id": 2,
        "msg": "Hey two",
        "timestamp": "2023-05-01T23:57:31.113452",
        "user": "default",
        "user_id": null
    },
    {
        "id": 3,
        "msg": "Hey 3",
        "timestamp": "2023-05-01T23:58:11.864497",
        "user": "default",
        "user_id": null
    }
]

2)
if start date comes after end date :
http://localhost:5000/posts_by_date?start=2023-05-02T00:04:46.588800&end=2023-05-01T23:56:54.001570
Error: 'start' time cannot be after 'end' time


3)
http://localhost:5000/posts_by_date?start=2023-05-02T01:17:41.040424&end=2023-05-02T01:57:23.040212
[
    {
        "id": 18,
        "msg": "hello",
        "timestamp": "2023-05-02T01:17:41.040424",
        "user": "default",
        "user_id": 4
    },
    {
        "id": 19,
        "msg": "hello123",
        "timestamp": "2023-05-02T01:22:53.004640",
        "user": "default",
        "user_id": null
    },
    {
        "id": 20,
        "msg": "hello1234",
        "timestamp": "2023-05-02T01:24:23.541754",
        "user": "default",
        "user_id": null
    },
    {
        "id": 21,
        "msg": "Hello",
        "timestamp": "2023-05-02T01:51:01.760568",
        "user": "default",
        "user_id": 1
    },
    {
        "id": 22,
        "msg": "Hello",
        "timestamp": "2023-05-02T01:51:47.792468",
        "user": "default",
        "user_id": 3
    }
]


============================================================================================================================================================================================================================================================================================================================================================================

wrong path provided : 

url : http://localhost:5000/pos
{
    "error": "Not found"
}


url : http://localhost:5000/positive
{
    "error": "Not found"
}
