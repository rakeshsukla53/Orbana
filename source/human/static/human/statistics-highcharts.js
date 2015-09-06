(function (H) {
        function deferRender (proceed) {
            var series = this, 
                $renderTo = $(this.chart.container.parentNode);
         
            // It is appeared, render it
            if ($renderTo.is(':appeared')) {
                proceed.call(series);
                
            // It is not appeared, halt renering until appear
            } else  {
                $renderTo.appear(); // Initialize appear plugin
                $renderTo.on('appear', function () {
                    proceed.call(series);
                });
            }
        };
        
        H.wrap(H.Series.prototype, 'render', deferRender);
}(Highcharts));

$(function () {
// Set up the chart
chart = new Highcharts.Chart({
    chart: {
        renderTo: 'container1',
        type: 'column',
        margin: 75,
        options3d: {
            enabled: true,
            alpha: 5,
            beta: 5,
            depth: 50,
            viewDistance: 25
        },
        backgroundColor:'rgba(255, 255, 255, 0.01)',
    },

    title: {
        text: 'What defines a news story?',
        style: {
                color: "#006699",
                fontSize: "5vw",
                fontFamily: 'FFDINMED',

            }
    },
    plotOptions: {
        column: {
            depth: 25
        },
        series: {
            animation: {
                duration: 10000
            }
        },
    }, 
    yAxis: [{
                gridLineWidth: 1,
                minorGridLineWidth: 0,
                title: {

                    text: "Responses (in %)"
                }

            }],
    xAxis: [{
        gridLineWidth: 1,
        minorGridLineWidth: 0,
        categories: ['Facts', 'Unbiased Representation', 'Means of connectivity', 'Passtime', 'Waste', 'Not Routine', 'Other']
    }],
    exporting:{
        enabled: false
    },
    series: [{
        showInLegend: false,
        data: [
        {y: 59.2, color: '#93C7F6'},
        {y: 60, color: '#1C5D99'}, 
        {y: 15.2, color: '#3BB9B9'}, 
        {y: 27.2, color: '#2E7FC8'}, 
        {y: 6.4, color: 'red'}, 
        {y: 18.4, color: '#595FE4'}, 
        {y: 12, color: '#625959'}],
        name: "Definition of news"
    }]
});

function showValues() {
    $('#R0-value').html(chart.options.chart.options3d.alpha);
    $('#R1-value').html(chart.options.chart.options3d.beta);
}

showValues();
});

$(function () {
    $('#container2').highcharts({
        chart: {
            type: 'pie',
            options3d: {
                enabled: true,
                alpha: 45
            },
            backgroundColor:'rgba(255, 255, 255, 0.01)',

        },
        title: {
            text: 'Why is today\'s news not cool enough?',
            style: {
                    color: "#006699",
                    fontSize: "5vw",
                    fontFamily: 'FFDINMED',
             }
        },
        plotOptions: {
            pie: {
                depth: 45,
                 dataLabels: {
                        enabled: false
                },
                showInLegend: true,
            }
        },  
        exporting:{
            enabled: false
        },
        series: [{
            name: 'Existing News Channels',
            data: [
                ['Time Consuming', 32.8],
                ['Replacement by Social Media', 66.4],
                ['Insignificant Information', 34.4],
                ['Relatively Inaccessible', 1.6],
                ['Uniteresting Journalism', 26.4],
                ['One Directional Journalism', 22.4],
                ['Other', 14.4]
            ]
        }]
    });
});
    
$(function () {
    $('#container3').highcharts({
        chart: {
            type: 'bar',
            backgroundColor:'rgba(255, 255, 255, 0.01)',
        },
        title: {
            text: 'How can we turn tables?',
            style: {
                color: "#006699",
                fontSize: "5vw",
                fontFamily: 'FFDINMED',

            }
        },
        xAxis: {
            categories: ['Concise Articles', 'Two Directional Journalism', 'Passionate Journalists', 'Entertaining', 'Part of Routine'],            
            gridLineWidth: 1,
            minorGridLineWidth: 0,
            title: {
                text: 'Approaches'
            }
        },
        yAxis: {
            min: 0,            
            gridLineWidth: 1,
            minorGridLineWidth: 0,
            title: {
                text: 'Responses (percentage)',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        exporting:{
            enabled: false
        },
        tooltip: {
            valueSuffix: '%'
        },
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: true
                }
            }
        },
        credits: {
            enabled: false
        },
        series: [{

            showInLegend: false,
            name: 'Turning Tables',
            data: [
            {y:52,color: 'red' }, 
            {y:33.6,color: '#1C5D99'}, 
            {y:28.8, color: '#3BB9B9'},
            {y:25.6, color: '#595FE4'},
            {y:68, color: '#625959'}
            ]
        }]
    });
});