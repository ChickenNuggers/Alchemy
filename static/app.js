var app = angular.module('Alchemy', ['ngMaterial', 'ngMdIcons']);

app.config(function($mdThemingProvider) {
	$mdThemingProvider.theme('default')
		.primaryPalette('blue')
		.accentPalette('pink');
});
app.controller("module_1", function($scope, $mdToast) {
	$scope.openToast = function($event) {
		$mdToast.show($mdToast.simple().content("Toast World!").capsule(true).position("top right"));
	};
});
