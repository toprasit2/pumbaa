'''
Created on Oct 11, 2013

@author: boatkrap
'''
def admin_include(config):
    config.add_route('admin.forums.index', '/forums')
    config.add_route('admin.forums.create', '/forums/create')
    config.add_route('admin.forums.edit', '/forums/edit/{forum_id}')
    config.add_route('admin.forums.delete', '/forums/delete/{forum_id}')
    
    config.add_route('admin.users.index', '/users')
    config.add_route('admin.users.add_role', '/users/{user_id}/roles/{role_id}')

def manager_include(config):
    config.add_route('manager.users.approve', '/users/approve')
    config.add_route('manager.users.do_approve', '/users/approve/{user_id}')
    
    config.add_route('manager.topics.index', '/topics')
    config.add_route('manager.topics.change_status', '/topics/{topic_id}/status/{status}')
    config.add_route('manager.topics.problem', '/topics/problem')
    
    config.add_route('manager.pages.index', '/pages')
    config.add_route('manager.pages.edit', '/pages/edit/{topic_id}')
    config.add_route('manager.pages.compose', '/pages/new_page')

def forums_include(config):
    
    config.add_route('forums.tags.index', '/topics/tags')
    config.add_route('forums.tags.list_contents', '/topics/tags/{name}')

    config.add_route('forums.comments.comment', '/topics/{topic_id}/comment')
    config.add_route('forums.comments.replies', '/topics/{topic_id}/comment/${comment_id}')
    
    config.add_route('forums.topics.index', '/topics')
    config.add_route('forums.topics.compose', '/topics/compose')
    config.add_route('forums.topics.view', '/topics/{topic_id}/{title}')

    # feed
    config.add_route('forums.feeds', '/feeds.xml')
    config.add_route('forums.feeds.forums', '/feeds/{forum_name}.xml')
    
    config.add_route('forums.view', '/{name}')
    
    
    
def add_routes(config):
    config.add_route('index', '/')
    
    # account routes
    config.add_route('register', '/register')
    config.add_route('home', '/home')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('accounts.change_password', '/accounts/change_password')
    config.add_route('accounts.change_username', '/accounts/change_username')

    # add admin route
    config.add_route('admin.index', '/admin')
    config.include(admin_include, route_prefix='/admin')
    
    # add manager route
    config.add_route('manager.index', '/manager')
    config.include(manager_include, route_prefix='/manager')
    
    # add forums
    config.add_route('forums.index', '/forums')
    config.include(forums_include, route_prefix='/forums')
    
    # pages
    config.add_route('pages.index', '/pages')
    config.add_route('pages.view', '/pages/{title}')
    
    
    config.add_static_view('public', 'public', cache_max_age=3600)
    