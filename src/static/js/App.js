'use strict';
 2 
 3 //(1)
 4 var Blog = angular.module("Blog", ["ui.bootstrap", "ngCookies"], function ($interpolateProvider) {
 5         $interpolateProvider.startSymbol("{[{");
 6         $interpolateProvider.endSymbol("}]}");
 7     }
 8 );
 9 
10 //(2)
11 Blog.run(function ($http, $cookies) {
12     $http.defaults.headers.common['X-CSRFToken'] = $cookies['csrftoken'];
13 })
14 
15 //(3)
16 Blog.config(function ($routeProvider) {
17     $routeProvider
18         .when("/", {
19             templateUrl: "static/js/app/views/feed.html",
20             controller: "FeedController",
21             resolve: {
22                 posts: function (PostService) {
23                     return PostService.list();
24                 }
25             }
26         })
27         .when("/post/:id", {
28             templateUrl: "static/js/app/views/view.html",
29             controller: "PostController",
30             resolve: {
31                 post: function ($route, PostService) {
32                     var postId = $route.current.params.id
33                     return PostService.get(postId);
34                 }
35             }
36         })
37         .otherwise({
38             redirectTo: '/'
39         })
40 })