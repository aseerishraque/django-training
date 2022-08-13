from django.shortcuts import render, redirect
from blog.models import Post
from blog.forms import PostForm


def post_list(request, *args, **kwargs):
    posts = Post.objects.all()
    response = {
        'posts' : posts
    }
    return render(request, 'blog/list.html', response)
    # return reverse('blog:post_list', current_app=request.resolver_match.namespace)

def post_details(request, post_id, *args, **kwargs):
    post = Post.objects.get(id=post_id)
    response = {
        'post' : post,
    }
    return  render(request, 'blog/post_details.html', response)

def create_post(request, *args, **kwargs):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            # clean_data = form.cleaned_data
            #
            # # Will be fetched from auth
            # author_id = 1
            # title = clean_data['title']
            # body = clean_data.get('body', None)
            # status = clean_data.get('status', 'draft')
            # post = Post.objects.create(title=title, body=body, status=status, author_id=author_id)
            form.save()
            return redirect('blog:post_details', form.instance.id)
    else:
        form = PostForm()
        response = {
            'post_form': form,
            'operation_type': 'create'
        }
        return render(request, 'blog/create_form.html', response)

def update_post(request, post_id, *args, **kwargs):
    post_obj = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post_obj)
        if form.is_valid():
            # clean_data = form.cleaned_data
            #
            # author_id = 1
            # title = clean_data['title']
            # body = clean_data.get('body', None)
            # status = clean_data.get('status', 'draft')
            # post = post_obj.update(title=title, body=body, status=status, author_id=author_id)
            form.save()
            return redirect('blog:post_details', post_id)
    else:
        post_data = post_obj
        post_data = {
            'title':post_data.title,
            'body':post_data.body,
            'status':post_data.status
        }
        form = PostForm(post_data)
        response = {
            'post_form' : form,
            'operation_type' : 'update'
        }
        return render(request, 'blog/create_form.html', response)



