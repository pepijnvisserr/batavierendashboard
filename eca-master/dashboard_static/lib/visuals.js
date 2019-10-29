$(document).ready(function(){
    $("#visuals div").addClass("invisible");
    $(".Wordcloud").removeClass("invisible");
    
    $("#btn_cloud").click(function(){        
            $("#visuals div").addClass("invisible");
            $(".Wordcloud").removeClass("invisible");
            $("*li.nav-item a").removeClass("active");
            $(this).addClass("active");
    });
    
    $("#btn_geo").click(function(){
            $("#visuals div").addClass("invisible");
            $(".Geolocation").removeClass("invisible");
            $("*li.nav-item a").removeClass("active");
            $(this).addClass("active");
    });
    
    $("#btn_graph").click(function(){
            $("#visuals div").addClass("invisible");
            $(".Graph").removeClass("invisible");
            $(".Graph div").removeClass("invisible");
            $("*li.nav-item a").removeClass("active");
            $(this).addClass("active");
    });
    
    $("#darkmode").click(function(){
            $("*").toggleClass("darkmode");
    });
});
