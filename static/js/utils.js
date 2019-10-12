$(document).ready(function(){

	function getCrsfCookie(name){
		var cookieValue = null;
		if (document.cookie && document.cookie !== ''){
			var cookies = document.cookie.split(';')
			for (var index = 0; index < cookies.length; index++){
				var cookie = jQuery.trim(cookies[index]);
				if (cookie.substring(0, name.length + 1) === (name + "=")){
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	var csrftoken = getCrsfCookie('csrftoken');

	$('#add-new-post').on('click', function(){
		article_id = $(this).attr('article-id');
		comment = $('textarea').val();
		if (comment.length){
			data = {
				comment: comment,
				article_id: article_id,
				csrfmiddlewaretoken: csrftoken
			}
			$.ajax({
				type: "POST",
				url: create_comment_url,
				data: data,
				success: function(data){
					counter = parseInt($('#comments-count').html());
					$('#comments-count').html(counter + 1);
					$('textarea').val('');
					$('.comments').prepend(data);
					$('#show-message').trigger('click');
				}
			});
		}
	});

	$('.hot-new-item').hover(function(){
		image_to_set = $(this).attr('image_path');
		$('#hot-image').attr('src', image_to_set);
	});

});