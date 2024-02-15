# AI COVER LETTER

## DEVELOPERS:

KP Gomez
Jacob Bassett

## DESCRIPTION:

This is a web application deployed to Vercel that enables users to structure coverletter queries to ChatGPT. A user will be able to add previous resumes and coverletters to a prompt along with a job description, so that ChatGPT can generate a first draft coverletter for that job in the voice of the user.

## TESTS:

To generate new tokens
```
POST /api/token/ HTTP/1.1
Accept: */*
User-Agent: Thunder Client (https://www.thunderclient.com)
Content-Type: application/x-www-form-urlencoded
Host: localhost:8000
Content-Length: 37

password=1234&email=admin%40email.com
```

To refresh token.
```
POST /api/register/ HTTP/1.1
Accept: */*
User-Agent: Thunder Client (https://www.thunderclient.com)
Content-Type: application/json
Host: localhost:8000
Content-Length: 104

{ 
"first_name":"test1",
"second_name":"test1",
"password":"strongpassword",
"email":"test1@email.com"
}
```