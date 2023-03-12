/*!
 * Name    : Just Another Parallax [Jarallax]
 * Version : 1.1.0
 * Author  : _nK http://nkdev.info
 * GitHub  : https://github.com/nk-o/jarallax
 */
!function(e){"use strict";"function"==typeof define&&define.amd?define(["jquery"],e):"undefined"!=typeof exports?module.exports=e(require("jquery")):e(jQuery)}((function(e){Date.now||(Date.now=function(){return(new Date).getTime()}),window.requestAnimationFrame||function(){"use strict";for(var e=["webkit","moz"],t=0;t<e.length&&!window.requestAnimationFrame;++t){var n=e[t];window.requestAnimationFrame=window[n+"RequestAnimationFrame"],window.cancelAnimationFrame=window[n+"CancelAnimationFrame"]||window[n+"CancelRequestAnimationFrame"]}if(/iP(ad|hone|od).*OS 6/.test(window.navigator.userAgent)||!window.requestAnimationFrame||!window.cancelAnimationFrame){var i=0;window.requestAnimationFrame=function(e){var t=Date.now(),n=Math.max(i+16,t);return setTimeout((function(){e(i=n)}),n-t)},window.cancelAnimationFrame=clearTimeout}}();var t,n,i=function(){for(var e="transform WebkitTransform MozTransform OTransform msTransform".split(" "),t=document.createElement("div"),n=0;n<e.length;n++)if(t&&void 0!==t.style[e[n]])return e[n];return!1}(),a=function(){if(!window.getComputedStyle)return!1;var e,t=document.createElement("p"),n={webkitTransform:"-webkit-transform",OTransform:"-o-transform",msTransform:"-ms-transform",MozTransform:"-moz-transform",transform:"transform"};for(var i in(document.body||document.documentElement).insertBefore(t,null),n)void 0!==t.style[i]&&(t.style[i]="translate3d(1px,1px,1px)",e=window.getComputedStyle(t).getPropertyValue(n[i]));return(document.body||document.documentElement).removeChild(t),void 0!==e&&e.length>0&&"none"!==e}(),o=navigator.userAgent.toLowerCase().indexOf("android")>-1,r=!!window.opera,l=[],m=(t=0,function(n,i){var a,m=this;m.$item=e(n),m.defaults={speed:.5,imgSrc:null,imgWidth:null,imgHeight:null,enableTransform:!0,zIndex:-100},a=m.$item.data("jarallax")||{},m.options=e.extend({},m.defaults,a,i),m.options.speed=Math.min(1,Math.max(0,parseFloat(m.options.speed))),m.instanceID=t++,m.image={src:m.options.imgSrc||null,$container:null,$item:null,width:m.options.imgWidth||null,height:m.options.imgHeight||null,useImgTag:o||r},m.initImg()&&(m.init(),l.push(m))});m.prototype.initImg=function(){var e=this;return null===e.image.src&&(e.image.src=e.$item.css("background-image").replace(/^url\(['"]?/g,"").replace(/['"]?\)$/g,"")),!(!e.image.src||"none"===e.image.src)},m.prototype.init=function(){var t=this,n={position:"absolute",top:0,left:0,width:"100%",height:"100%",overflow:"hidden","pointer-events":"none",transition:"transform linear -1ms, -webkit-transform linear -1ms"},a={position:"fixed"};function o(){t.coverImage(),t.clipContainer(),t.onScroll(!0),t.$item.data("jarallax-original-styles",t.$item.attr("style")),setTimeout((function(){t.$item.css({"background-image":"none","background-attachment":"scroll","background-size":"auto"})}),0)}t.image.$container=e("<div>").css(n).css({visibility:"hidden","z-index":t.options.zIndex}).attr("id","jarallax-container-"+t.instanceID).prependTo(t.$item),t.image.useImgTag&&i?(t.image.$item=e("<img>").attr("src",t.image.src),a=e.extend({"max-width":"none"},n,a)):(t.image.$item=e("<div>"),a=e.extend({"background-position":"50% 50%","background-repeat":"no-repeat no-repeat","background-image":'url("'+t.image.src+'")'},n,a)),t.image.$item.css(a).prependTo(t.image.$container),t.image.width&&t.image.height?o():t.getImageSize(t.image.src,(function(e,n){t.image.width=e,t.image.height=n,o()}))},m.prototype.destroy=function(){for(var t=this,n=0,i=l.length;n<i;n++)if(l[n].instanceID===t.instanceID){l.splice(n,1);break}e("head #jarallax-clip-"+t.instanceID).remove(),t.$item.attr("style",t.$item.data("jarallax-original-styles")),t.$item.removeData("jarallax-original-styles"),t.image.$container.remove(),delete t.$item[0].jarallax},m.prototype.round=function(e){return Math.floor(100*e)/100},m.prototype.getImageSize=function(e,t){if(!e||!t)return!1;var n=new Image;n.onload=function(){t(n.width,n.height)},n.src=e},m.prototype.clipContainer=function(){var t=this,n=t.image.$container.outerWidth(!0),i=t.image.$container.outerHeight(!0),a=e("head #jarallax-clip-"+t.instanceID);a.length||(e("head").append('<style type="text/css" id="jarallax-clip-'+t.instanceID+'"></style>'),a=e("head #jarallax-clip-"+t.instanceID));var o=["#jarallax-container-"+t.instanceID+" {","   clip: rect(0px "+n+"px "+i+"px 0);","   clip: rect(0px, "+n+"px, "+i+"px, 0);","}"].join("\n");a[0].styleSheet?a[0].styleSheet.cssText=o:a.html(o)},m.prototype.coverImage=function(){var t=this;if(t.image.width&&t.image.height){var n,a,o=t.image.$container.outerWidth(!0),r=t.image.$container.outerHeight(!0),l=e(window).outerWidth(!0),m=e(window).outerHeight(!0),s=t.image.width,d=t.image.height,c={width:Math.max(l,o)*Math.max(t.options.speed,1),height:Math.max(m,r)*Math.max(t.options.speed,1)};c.width/c.height>s/d?(n=c.width,a=c.width*d/s):(n=c.height*s/d,a=c.height),t.image.useImgTag&&i?(c.width=t.round(n),c.height=t.round(a),c.marginLeft=t.round(-(n-o)/2),c.marginTop=t.round(-(a-r)/2)):c.backgroundSize=t.round(n)+"px "+t.round(a)+"px",t.image.$item.css(c)}},m.prototype.onScroll=function(t){var n=this;if(n.image.width&&n.image.height){var o=e(window).scrollTop(),r=e(window).scrollLeft(),l=(e(window).width(),e(window).height()),m=n.$item.offset().top,s=n.$item.offset().left,d=n.$item.outerHeight(!0),c={visibility:"visible",backgroundPosition:"50% 50%"};if(!(!t&&(m+d<o||m>o+l))){var u=-(o-m)*n.options.speed,g=-(r-s)*n.options.speed;u=n.round(u),g=n.round(g),i&&n.options.enableTransform?(c.transform="translateY("+u+"px) translateX("+g+"px)",a&&(c.transform="translate3d("+g+"px, "+u+"px, 0)")):c.backgroundPosition=g+"px "+u+"px",n.image.$item.css(c)}}},e(window).on("scroll.jarallax",(function(){window.requestAnimationFrame((function(){for(var e=0,t=l.length;e<t;e++)l[e].onScroll()}))})),e(window).on("resize.jarallax orientationchange.jarallax load.jarallax",(function(){clearTimeout(n),n=setTimeout((function(){window.requestAnimationFrame((function(){for(var e=0,t=l.length;e<t;e++){var n=l[e];n.coverImage(),n.clipContainer(),n.onScroll()}}))}),100)}));var s=e.fn.jarallax;e.fn.jarallax=function(){for(var e,t=this,n=arguments[0],i=Array.prototype.slice.call(arguments,1),a=t.length,o=0;o<a;o++)if("object"==typeof n||void 0===n?t[o].jarallax||(t[o].jarallax=new m(t[o],n)):e=t[o].jarallax?t[o].jarallax[n].apply(t[o].jarallax,i):void 0,void 0!==e)return e;return this},e.fn.jarallax.noConflict=function(){return e.fn.jarallax=s,this},e(document).on("ready.data-jarallax",(function(){e("[data-jarallax]").jarallax()}))}));