$(document).ready(function(){
    $cloud     = $(".Wordcloud").html();
    $geo    = $(".Geolocation").html();
    $graph     = $(".Graph").html();
    $("#visuals").html($cloud);
    
    $("#btn_cloud").click(function(){        
            $("#visuals").html($cloud);
            $("*li.nav-item a").removeClass("active");
            $(this).addClass("active");
    });
    
    $("#btn_geo").click(function(){
            $("#visuals").html($geo);
            $("*li.nav-item a").removeClass("active");
            $(this).addClass("active");
    });
    
    $("#btn_graph").click(function(){
            $("#visuals").html($graph);
            $("*li.nav-item a").removeClass("active");
            $(this).addClass("active");
    });
    
    $("#darkmode").click(function(){
            $("*").toggleClass("darkmode");
    });
});
