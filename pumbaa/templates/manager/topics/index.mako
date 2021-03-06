<%inherit file="/manager/base/base.mako"/>
<%block name="where_am_i">
	${parent.where_am_i()}
	<li><a href="${request.current_route_path()}">Topic</a></li>
</%block>
<%block name="panel_title">My Topics</%block>
<ul class="list-inline">
	<li><a href="${request.route_path('forums.topics.compose')}">new topic</a></li>
</ul>
<ul class="list-group">
	% for topic in topics:
    <li class="list-group-item">
    	<a href="${request.route_path('forums.topics.view', title=topic.title, topic_id=topic.id)}">${topic.title}</a>
    </li>
    % endfor
</ul>