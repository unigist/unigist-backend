from django.shortcuts import redirect, render


def index(request):
    return render(request, 'root.html')

def user_template(request):
    return render(request, 'users/users-doc.html')


def post_template(request):
    context = {}

    context['endpoints'] = [
        {
            'name': 'Get posts',
            'method': 'GET',
            'path': '/posts/',
            'path_desc': 'Get all posts',
            'type': 'Request body',
            'type_fields': [
                {'name': 'Null', 'desc': 'There is no need for a body.'},
            ],
            'example':
"""
    const options = {method: 'GET'};
    fetch('http://localhost:8000/api/v1/posts/', options)
        .then(response => response.json())
        .then(response => console.log(response))
        .catch(err => console.error(err));'""",

            'resp_type': 'Respons body',
            'resp_attrs': [
                {'name': 'data', 'desc': ' (Array) containing the list of all posts'},
            ]
        },
        {
            'name': 'Get post',
            'method': 'GET',
            'path': '/posts/',
            'path_desc': 'Get details of a single posts',
            'type': 'Request body',
            'type_fields': [
                {'name': 'Null', 'desc': 'There is no need for a body.'},
            ],
            'example':
"""
    const options = {method: 'GET'};
    fetch('http://localhost:8000/api/v1/posts/nigase-this-is-insomnia-testttiting-one', options)
        .then(response => response.json())
        .then(response => console.log(response))
        .catch(err => console.error(err));'""",

            'resp_type': 'Respons body',
            'resp_attrs': [
            {'name': 'id', 'desc': ' (int) id of the post'},
            {'name': 'author', 'desc': ' (int) id of the author'},
            {'name': 'title', 'desc': ' (string) post title'},
            {'name': 'body', 'desc': ' (string) post body'},
            {'name': 'slug', 'desc': ' (string) post slug, used for single routing'},
            {'name': 'date_published', 'desc': ' (time string) when post was poblised'},
            {'name': 'date_created', 'desc': ' (time string) when post was created'},
        ]
        },
        {
            'name': 'Create a Post',
            'method': 'POST',
            'path': '/posts/create',
            'path_desc': 'Create a new post, this endpoint is secure thus requires the users token',
            'type': 'Request Header',
            'type_fields': [
                {'name': 'Authentication', 'desc': '(string, required) - The authentication token obtained from logging in'},
            ],
            'example':
"""
const options = {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        Authorization: 'Token 6620d1a563694cd3da86912f9ae9bda4bf8e07b7'
    },
    body: '{"title":"This is insomnia testttiting one","body":"What? this is the body","author":27}'
};

fetch('http://localhost:8000/api/v1/posts/create', options)
    .then(response => response.json())
    .then(response => console.log(response))
    .catch(err => console.error(err));""",

            'resp_type': 'Response body',
            'resp_attrs': [
            {'name': 'success', 'desc': ' (String) - a success message or failure'},
            {'name': 'data', 'desc': ' (Dictionary) - contains the post created'},

        ]
        },

    ]
    return render(request, 'posts/posts-doc.html', context=context)
