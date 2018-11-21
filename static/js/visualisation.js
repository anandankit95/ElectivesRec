Highcharts.chart('container', {
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Electives Opted in 2018'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: false
            },
            showInLegend: true
        }
    },
    series: [{
        name: 'Electives',
        colorByPoint: true,
        data: [{
            name: 'Advanced Database management system',
            y: 16.66,
            sliced: true,
            selected: true
        }, {
            name: 'Computer Graphics',
            y: 16.66
        }, {
            name: 'Analysis and Design of Algorithms',
            y: 16.66
        }, {
            name: 'Data Analytics',
            y: 16.66
        }, {
            name: 'High Performance Computing Architecture',
            y: 16.66
        }, {
            name: 'Web Tech',
            y: 16.66
        }]
    }]
});
