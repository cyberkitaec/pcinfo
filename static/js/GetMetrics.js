$(document).ready(function(){
    setInterval(function (){
        let metrics_number = $('#metrics_number').val()
        if (jQuery.isEmptyObject(metrics_number)){
            metrics_number = 10
        }
        console.log(metrics_number)
        $.ajax({
            url: `../api/metrics/limit/${metrics_number}`,
            type: 'GET',
            datatype: 'json',
            success: function (data){
                console.log(metrics_number)
                $('#metrics_data').empty();
                $.each(data, function (index, el){
                    $('table').find(
                        'tbody').append(
                            `<tr><td class="border border-slate-300">${el.cpu_usage}</td>
<td class="border border-slate-300">${el.memory_usage}</td></tr>`)
                })

            }
        })
    }, 1000)
});