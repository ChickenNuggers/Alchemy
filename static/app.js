var app = angular.module('Alchemy', ['ngMaterial', 'ngMdIcons']);

app.config(function($mdThemingProvider) {
	$mdThemingProvider.theme('default')
		.primaryPalette('blue')
		.accentPalette('pink');
});
app.controller("introduction", function($scope, $mdToast, $mdDialog) {
	$scope.openToast = function($event) {
		$mdToast.show($mdToast.simple().content("Toast World!").capsule(true).position("top right"));
	};
	$scope.showAlert = function($event) {
		$mdDialog.show($mdDialog.alert()
			.title('Title')
			.content('You can put a description here')
			.ok('Close')
		);
	};

});

