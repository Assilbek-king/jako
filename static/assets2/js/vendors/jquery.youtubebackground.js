"function"!=typeof Object.create&&(Object.create=function(e){function t(){}return t.prototype=e,new t}),function(e,t,o){var i=function(o){"undefined"==typeof YT&&void 0===t.loadingPlayer?(t.loadingPlayer=!0,t.dfd=e.Deferred(),t.onYouTubeIframeAPIReady=function(){t.onYouTubeIframeAPIReady=null,t.dfd.resolve("done"),o()}):"object"==typeof YT?o():t.dfd.done((function(e){o()}))};YTPlayer={player:null,defaults:{ratio:16/9,videoId:"LSmgKRx5pBo",mute:!0,repeat:!0,width:e(t).width(),playButtonClass:"YTPlayer-play",pauseButtonClass:"YTPlayer-pause",muteButtonClass:"YTPlayer-mute",volumeUpClass:"YTPlayer-volume-up",volumeDownClass:"YTPlayer-volume-down",start:0,pauseOnScroll:!1,fitToBackground:!0,playerVars:{iv_load_policy:3,modestbranding:1,autoplay:1,controls:0,showinfo:0,wmode:"opaque",branding:0,autohide:0},events:null},init:function(a,n){var l,r,s,d=this;return d.userOptions=n,d.$body=e("body"),d.$node=e(a),d.$window=e(t),d.defaults.events={onReady:function(e){d.onPlayerReady(e),d.options.pauseOnScroll&&d.pauseOnScroll(),"function"==typeof d.options.callback&&d.options.callback.call(this)},onStateChange:function(e){1===e.data?(d.$node.find("img").fadeOut(400),d.$node.addClass("loaded")):0===e.data&&d.options.repeat&&d.player.seekTo(d.options.start)}},d.options=e.extend(!0,{},d.defaults,d.userOptions),d.options.height=Math.ceil(d.options.width/d.options.ratio),d.ID=(new Date).getTime(),d.holderID="YTPlayer-ID-"+d.ID,d.options.fitToBackground?d.createBackgroundVideo():d.createContainerVideo(),d.$window.on("resize.YTplayer"+d.ID,(function(){d.resize(d)})),l=d.onYouTubeIframeAPIReady.bind(d),r=o.createElement("script"),s=o.getElementsByTagName("head")[0],"file://"==t.location.origin?r.src="http://www.youtube.com/iframe_api":r.src="//www.youtube.com/iframe_api",s.appendChild(r),s=null,r=null,i(l),d.resize(d),d},pauseOnScroll:function(){var e=this;e.$window.on("scroll.YTplayer"+e.ID,(function(){1===e.player.getPlayerState()&&e.player.pauseVideo()})),e.$window.scrollStopped((function(){2===e.player.getPlayerState()&&e.player.playVideo()}))},createContainerVideo:function(){var t=e('<div id="ytplayer-container'+this.ID+'" >                                    <div id="'+this.holderID+'" class="ytplayer-player-inline"></div>                                     </div>                                     <div id="ytplayer-shield" class="ytplayer-shield"></div>');this.$node.append(t),this.$YTPlayerString=t,t=null},createBackgroundVideo:function(){var t=e('<div id="ytplayer-container'+this.ID+'" class="ytplayer-container background">                                    <div id="'+this.holderID+'" class="ytplayer-player"></div>                                    </div>                                    <div id="ytplayer-shield" class="ytplayer-shield"></div>');this.$node.append(t),this.$YTPlayerString=t,t=null},resize:function(o){var i=e(t);o.options.fitToBackground||(i=o.$node);var a,n,l=i.width(),r=i.height(),s=e("#"+o.holderID);l/o.options.ratio<r?(a=Math.ceil(r*o.options.ratio),s.width(a).height(r).css({left:(l-a)/2,top:0})):(n=Math.ceil(l/o.options.ratio),s.width(l).height(n).css({left:0,top:(r-n)/2})),s=null,i=null},onYouTubeIframeAPIReady:function(){this.player=new t.YT.Player(this.holderID,this.options)},onPlayerReady:function(e){this.options.mute&&e.target.mute(),e.target.playVideo()},getPlayer:function(){return this.player},destroy:function(){this.$node.removeData("yt-init").removeData("ytPlayer").removeClass("loaded"),this.$YTPlayerString.remove(),e(t).off("resize.YTplayer"+this.ID),e(t).off("scroll.YTplayer"+this.ID),this.$body=null,this.$node=null,this.$YTPlayerString=null,this.player.destroy(),this.player=null}},e.fn.scrollStopped=function(t){var o=e(this),i=this;o.scroll((function(){o.data("scrollTimeout")&&clearTimeout(o.data("scrollTimeout")),o.data("scrollTimeout",setTimeout(t,250,i))}))},e.fn.YTPlayer=function(t){return this.each((function(){e(this).data("yt-init",!0);var o=Object.create(YTPlayer);o.init(this,t),e.data(this,"ytPlayer",o)}))}}(jQuery,window,document);