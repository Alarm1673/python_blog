/*导航当前页高亮*/

var obj=null;
var As=document.getElementById('topnav').getElementsByTagName('a');
obj = As[1];
for(i=1;i<As.length;i++){if(window.location.href.indexOf(As[i].href)>=0)
obj=As[i];}
obj.id='topnav_current'

/*浏览评论排行*/
window.onload = function ()
{
  var oLi = document.getElementById("tab").getElementsByTagName("li");
  var oUl = document.getElementById("ms-main").getElementsByTagName("div");

  for(var i = 0; i < oLi.length; i++)
  {
    oLi[i].index = i;
    oLi[i].onmouseover = function ()
    {
      for(var n = 0; n < oLi.length; n++) oLi[n].className="";
      this.className = "cur";
      for(var n = 0; n < oUl.length; n++) oUl[n].style.display = "none";
      oUl[this.index].style.display = "block"
    }
  }
}

/*回到顶部*/
$(function(){
    showScroll();
    function showScroll(){
        $(window).scroll( function() {
            var scrollValue=$(window).scrollTop();
            scrollValue > 100 ? $('div[class=scroll]').fadeIn():$('div[class=scroll]').fadeOut();
        } );
        $('#scroll').click(function(){
            $("html,body").animate({scrollTop:0},200);
        });
    }
})

$(function () {
    $("#musicPlayer").simplemusic({
        autoplay: false,
        urls: ["http://qzone.haoduoge.com/music3/2015-02-02/1422858039.mp3","http://qzone.haoduoge.com/music3/2015-02-02/1422858039.mp3"]
    });
});
