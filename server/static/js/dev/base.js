/**	class UsNav
*	
*/
function UsNav(){}
UsNav.Hello = function(){
	alert('hello');
};
/** class UsTpl
*/
function UsTpl(element){
	this.element = $(element)
	var tplElements = this.element.find("templates");
	this.tpls = tplElements.clone();
	tplElements.remove();
	this.relpaceTableTag = function(str){
		return str.replace(/<tpl-th/g, '<th')
				.replace(/<tpl-tr/g, '<tr')
				.replace(/<tpl-td/g, '<td')
				.replace(/<\/tpl-th>/g, '</th>')
				.replace(/<\/tpl-tr>/g, '</tr>')
				.replace(/<\/tpl-td>/g, '</td>');
	};
	this.setParam = function(tplStr, k, v){
		var regStr = '%'+k+'%';
		return tplStr.replace(new RegExp(regStr, 'g'), v);
	};
	this.applyEachTemplate = function(tplName, params){
		params = params ? params : new Array();
		var p = null;
		var insTag = this.element.find('.applytpl[tpl="'+tplName+'"]');//需要替换的applytpl元素
		var tplStr = this.relpaceTableTag(this.tpls.find('#'+tplName).html());
		var preTpl = '';
		for(var i=0; i<params.length; i++){
			preTpl = tplStr;
			p = params[i];
			for(var key in p){
				preTpl = this.setParam(preTpl, key, p[key]);
			}
			$(insTag).after(preTpl);
		}
	};
	this.applyTemplate = function(tplName){
		var insTag = this.element.find('.applytpl[tpl="'+tplName+'"]');
		var insObj = this.tpls.find('#'+tplName);
		var htmlStr = this.relpaceTableTag($(insObj).html());
		$(insTag).replaceWith(htmlStr);
	};
	this.applyTpls = function() {
		var applyTags = this.element.find(".applytpl");
		for(var i=0; i<applyTags.length; i++){
			this.applyTemplate($(applyTags[i]).attr('tpl'));
		}
	}	
}
function UsForm(){}
UsForm.checkUserName = function(nameStr){

};




(function($){
    $.fn.checkEmpty = function(){

    };



	/* when document load*/
	$(document).ready(function(e) {
        /* handler bindings */
		
    });
	

	/*status page*/
	$('#api_status').ready(function(e) {
		var self = $('#api_status');
		var tpl = new UsTpl(self);
		var sevrUrl = 'http://' + window.location.host + '/api/';
		// tpl.applyTemplate('status-list')
		var tplElement = $(this).find("#status_list")
		if(tplElement.length > 0){
			var tplCtx = tplElement.html();
			var statusElement = tplElement.clone()
			tplElement.html("<span class='loading'>Loading...</span>")
			$.ajax({
				type:'GET', 
				url:'/api/apiadmin/apilist.json',
				success: function(data){
					var rst = eval('('+data+')');
                    if(rst.errnum == 0){
                        var data = rst.data
                        tplElement.html(statusElement.html());
                        for(var index=0; index < data.length; index++){
                            data[index].url = sevrUrl + data[index].url;
                        }
                        tpl.applyEachTemplate('status-list', data);
                        $('.apistatus').each(function(e){
                            var stutsElement = $(this).find('.status');
                            $.ajax({
                                type:"GET",
                                url: $(this).find('.request-url').text()+'.json?mod=debug',
                                success: function(d){
                                    var rst = eval('('+d+')');
                                    if(rst.errnum == 0){
                                        stutsElement.html('正常')
                                    }else{
                                        stutsElement.html(rst.msg)
                                    }
                                },
                                error: function(d){
                                    stutsElement.html('错误')
                                }
                            });

                        });
                    }

				}
			});
		}
	});

	/*login page*/
	$("#admin_login").ready(function(e) {
		$("#username,#userpwd").bind('keyup', function (event) {
		    if (event.keyCode == 13) {
		        $("#loginsubmit").click();
		    }
		});
		$(this).find('#loginsubmit').click(function(e){
			form = $("#loginform");
			$.ajax({
				type:"GET",
				url: '/api/user/login.json',
				data: {'usr': $('#username').val().trim(), 'pwd': hex_sha1($('#userpwd').val().trim())},
				success: function(d){
					var rst = eval('('+d+')');
					if(rst.errnum == 0){
						data = rst.data
						input = document.createElement('input');
						form.append($(input).attr('type', 'hidden').attr('name', 'group').val(data.group));
						form.submit();
						// window.location.href = "/admin?uid="+rst.data.uid;
					}
				},
				error: function(d){
					
				}
			});
		});
	});

    /*dev reg page*/
    $("#dev_reg").ready(function(e) {
        $("#username,#userpwd").bind('keyup', function (event) {
            if (event.keyCode == 13) {
                $("#dev_reg_submit").click();
            }
        });
        $(this).find('#dev_reg_submit').click(function(e){
            form = $("#dev_reg_form");
            form.submit();
//            $.ajax({
//                type:"GET",
//                url: '/api/user/login.json',
//                data: {'usr': $('#username').val().trim(), 'pwd': hex_sha1($('#userpwd').val().trim())},
//                success: function(d){
//                    var rst = eval('('+d+')');
//                    if(rst.errnum == 0){
//                        data = rst.data
//                        input = document.createElement('input');
//                        form.append($(input).attr('type', 'hidden').attr('name', 'group').val(data.group));
//                        form.submit();
//                        // window.location.href = "/admin?uid="+rst.data.uid;
//                    }
//                },
//                error: function(d){
//
//                }
//            });
        });
    });
	
})(jQuery);