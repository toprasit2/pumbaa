<%inherit file="/base/base_home.mako"/>

<%block name="title">
	Change Feed URL
</%block>

<%block name="where_am_i">
${parent.where_am_i()}
<li><a href="${request.current_route_path()}">Change Feed URL</a></li>
</%block>
<h1>Change Feed URL</h1>

Current blog rss url : #################
<form action="${request.current_route_path()}" method="post">
	% for field in form:
		<% css_class = 'form-group' %>
    	% if field.errors:
    	<% css_class += ' has-error' %>
    	% endif
    <div class="${css_class}">
    	${field.label(class_="control-label")}
    	% if field.errors:
    	<span class="text-danger">${field.errors[0]}</span>
    	% elif field.flags.required:
    	<span style="color: red;">*</span>
    	% endif
    	${field(class_='form-control', placeholder='Enter '+field.label.text.lower())}
  	</div>
	% endfor
	<button type="submit" class="btn btn-primary">Change blog RSS URL</button>
</form>