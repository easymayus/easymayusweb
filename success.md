---
title: 易美教育 | Easymay
layout: default
description: 易美学员勇夺MIT金融录取，连续两年斩获宾大沃顿本科ED录取。
keywords: 易美教育，易美教育集团，数据为驱动，构国际教育咨询，房地产信息咨询，海外置业与财富管理，一体的多维度垂直领域服务商，高端教育咨询子品牌和创新型房产咨询服务平台，丰富的海外教育资源和优秀的海外专业化团队作为核心竞争力，一站式留学解决方案，教育规划，留学申请，职业教育，学习规划，考试培训，房产咨询，美国本土留学咨询公信力第一品牌。
---
<div id="wrapper" class="clearfix">
    <!-- {% include preloader.html %} -->
    {% include navigation.html %}
    <div class="main-content">

        <section id="home" class="divider">
            <div class="container-fluid p-0">
                <a href="https://easymayus.com/articles/cases_399.html"><img width="100%" src="assets/cases/cases.jpg"></a>
                <div id="rev_slider_5_1_wrapper" class="rev_slider_wrapper fullwidthbanner-container" data-alias="test" data-source="gallery" style="margin:0px auto;background:#0c0b09;padding:0px;margin-top:0px;margin-bottom:0px;">
                    <!-- START REVOLUTION SLIDER 5.4.7.2 fullwidth mode -->
                <!-- END REVOLUTION SLIDER -->
                <script> 
                var revapi5, tpj;
                (function () {
                    if (!/loaded|interactive|complete/.test(document.readyState)) document.addEventListener("DOMContentLoaded", onLoad); else onLoad();

                    function onLoad() {
                        if (tpj === undefined) {
                            tpj = jQuery;
                            if ("on" == "on") tpj.noConflict();
                        }
                        if (tpj("#rev_slider_5_1").revolution == undefined) {
                            revslider_showDoubleJqueryError("#rev_slider_5_1");
                        } else {
                            revapi5 = tpj("#rev_slider_5_1").show().revolution({
                                sliderType: "standard",
                                jsFileLocation: "//credentusa.com/wp-content/plugins/revslider/public/assets/js/",
                                sliderLayout: "fullwidth",
                                dottedOverlay: "none",
                                delay: 4000,
                                navigation: {
                                    keyboardNavigation: "on",
                                    keyboard_direction: "horizontal",
                                    mouseScrollNavigation: "off",
                                    mouseScrollReverse: "default",
                                    onHoverStop: "on",
                                    touch: {
                                        touchenabled: "on",
                                        touchOnDesktop: "off",
                                        swipe_threshold: 75,
                                        swipe_min_touches: 1,
                                        swipe_direction: "horizontal",
                                        drag_block_vertical: false
                                    },
                                    arrows: {
                                        style: "hermes",
                                        enable: true,
                                        hide_onmobile: true,
                                        hide_under: 700,
                                        hide_onleave: false,
                                        tmp: '<div class="tp-arr-allwrapper">  <div class="tp-arr-imgholder"></div>  <div class="tp-arr-titleholder"></div> </div>',
                                        left: {h_align: "left", v_align: "center", h_offset: 0, v_offset: 0},
                                        right: {h_align: "right", v_align: "center", h_offset: 0, v_offset: 0}
                                    }
                                },
                                visibilityLevels: [1240, 1024, 778, 480],
                                gridwidth: 1230,
                                gridheight: 650,
                                lazyType: "none",
                                parallax: {
                                    type: "mouse",
                                    origo: "enterpoint",
                                    speed: 400,
                                    speedbg: 0,
                                    speedls: 0,
                                    levels: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 47, 48, 49, 50, 51, 55],
                                },
                                shadow: 0,
                                spinner: "spinner2",
                                stopLoop: "off",
                                stopAfterLoops: -1,
                                stopAtSlide: -1,
                                shuffle: "off",
                                autoHeight: "off",
                                disableProgressBar: "off",
                                hideThumbsOnMobile: "on",
                                hideSliderAtLimit: 0,
                                hideCaptionAtLimit: 0,
                                hideAllCaptionAtLilmit: 0,
                                debugMode: false,
                                fallbacks: {simplifyAll: "off", nextSlideOnWindowFocus: "off", disableFocusListener: false,}
                            });
                        }
                        ; /* END OF revapi call */
                    }; /* END OF ON LOAD FUNCTION */
                }()); /* END OF WRAPPING FUNCTION */ </script>
            </div>
       
       

    <section class="news-bg preload">
      <div class="container">
        <div class="section-content pnews-content">
          <div class="row">
            <div class="col-md-12">
              <!-- Portfolio Filter -->
                <div class="portfolio-filter">
                  <a href="#" class="active filter_all">全部</a>
                  <a href="#" class="filter_science">理工科</a>
                  <a href="#" class="filter_fineart">文商科</a>
                  <a href="#" class="filter_undergrad">本科</a>
                </div>

                <!-- Portfolio Gallery Grid -->
                <div id="casesgrid" class="gallery-isotope default-animation-effect grid-4 gutter-30 clearfix">

                 <!-- success cases display -->
                {% assign rsorted = site.articles | sort:"sequence" %}
                {% assign sorted = rsorted | reverse %}
                {% for story in sorted %}
                {% if story.appear_page contains 'success' %}
                <div class="gallery-item cases {{story.type}} {{story.success_type}}">
                  <img src="{{story.src}}" alt="" title="" height="172px" width="260px">
                  <div class="image-box-details">
                    <h4 class="title">{{story.title}}</h4>
                    <p class="desc">{{story.description}}</p>
                    <a href="{{story.url}}" target="_blank" class="btn btn-theme-colored">查看详情</a>
                  </div>
                </div>
                {% endif %}
                {% endfor %}
                </div>

                <!-- End Portfolio Gallery Grid -->

            </div>
          </div>
        </div>
      </div>
    </section>
    </div>
    {% include footer.html %}
</div>