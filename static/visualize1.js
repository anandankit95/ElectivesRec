$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				fname : $('#first-name').val(),
				lname : $('#last-name').val(),
				s1s1 : $('#sem1_subject1').val(),
				s1s2 : $('#sem1_subject2').val(),
				s1s3 : $('#sem1_subject3').val(),
				s1s4 : $('#sem1_subject4').val(),
				s1s5 : $('#sem1_subject5').val(),
				s2s1 : $('#sem2_subject1').val(),
				s2s2 : $('#sem2_subject2').val(),
				s2s3 : $('#sem2_subject3').val(),
				s2s4 : $('#sem2_subject4').val(),
				s2s5 : $('#sem2_subject5').val(),
				s3s1 : $('#sem3_subject1').val(),
				s3s2 : $('#sem3_subject2').val(),
				s3s3 : $('#sem3_subject3').val(),
				s3s4 : $('#sem3_subject4').val(),
				s3s5 : $('#sem3_subject5').val(),
				s4s1 : $('#sem4_subject1').val(),
				s4s2 : $('#sem4_subject2').val(),
				s4s3 : $('#sem4_subject3').val(),
				s4s4 : $('#sem4_subject4').val(),
				s4s5 : $('#sem4_subject5').val()				
				
			},
			type : 'POST',
			url : '/elective'
		})
		.done(function(data) {

			$("#res").text(data);
<<<<<<< HEAD
			var parsed = JSON.parse(data);
			$(function () {
					$('#container').highcharts({
					chart: {	
						    	renderTo : 'container',
							plotBackgroundColor: null,
							plotBorderWidth: null,
							plotShadow: false,
							type: 'pie'
						    },
						    title: {
							text: 'Recommendation'
						    },
						    tooltip: {
							pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
						    },
						    plotOptions: {
							pie: {
							    allowPointSelect: true,
							    cursor: 'pointer',
							    dataLabels: {
								enabled: true,
								format: '<b>{point.name}</b>: {point.percentage:.1f} %',
								style: {
								    color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black'
								}
							    }
							}
						    },
						    series: [{
							name: 'Brands',
							colorByPoint: true,
							data: [{
							    name: "subject1",
							    y: 61.41
							}, {
							    name: 'subject2',
							    y: 11.84
							}, {
							    name: 'subject3',
							    y: 10.85
							}, {
							    name: 'subject4',
							    y: 2.61
							}]
						    }]


});
});
		event.preventDefault();

	});

});
