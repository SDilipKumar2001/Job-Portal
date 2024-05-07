
// ADD ROW 
$(document).on('click', '.row-add', function() {
    console.log('a')
    var $tr = $(this).closest('.tr_clone');
    var $clone = $tr.clone();
    console.log($clone);
    $clone.find(':text').val('');
    $tr.after($clone);
});

// DELETE ROW
$(document).on('click','.del-row',function(){
    var tbl=$('#exp_tbl >tbody >tr').length;
    console.log(tbl)
    if (tbl > 1){
        $(this).closest('tr').remove()
    }
    
})
/opt/inventory14/odoo-custom-addons/hospital_system_management/static/src/website.js
       
        // console.log(x.rowIndex)
    //     // var row = table.deleteRow(rowCount-1);
    //     document.getElementById("exp_tbl").deleteRow(0);
    // }
// }

// ELIMINATE THE SPECIAL CHARACTERS FROM TYPING
function checkSpcialChar(event){
    if(!((event.keyCode >= 65) && (event.keyCode <= 90) || (event.keyCode >= 97) && (event.keyCode <= 122) || (event.keyCode >= 48) && (event.keyCode <= 57))){
       event.returnValue = false;
       return;
    }
    event.returnValue = true;
 }



//  function cal() {
//     var from_field = document.getElementById('from_field').value;
//     var to_field = document.getElementById('to_field').value;
  
//     try {
//       document.getElementById('years').innerHTML = '';
  
//     //   var years = getDateDifference(new Date(from_field), new Date(to_field));
//       document.getElementById("years").value=GetDays(new Date(from_field), new Date(to_field));
//     //   if (years && !isNaN(years.years)) {
//     //     document.getElementById('years').innerHTML =
//     //       years.years + ' year' + (years.years == 1 ? ' ' : 's ') +
//     //       years.months + ' month' + (years.months == 1 ? ' ' : 's ') + 'and ' +
//     //       years.days + ' day' + (years.days == 1 ? '' : 's');
//     //   }
//     } catch (e) {
//       console.error(e);
//     }
//   }
  
//   function getDateDifference(startDate, endDate) {
//     if (startDate > endDate) {
//       console.error('Start date must be before end date');
//       return null;
//     }
//     var startYear = startDate.getFullYear();
//     var startMonth = startDate.getMonth();
//     var startDay = startDate.getDate();
  
//     var endYear = endDate.getFullYear();
//     var endMonth = endDate.getMonth();
//     var endDay = endDate.getDate();
  
//     var february = (endYear % 4 == 0 && endYear % 100 != 0) || endYear % 400 == 0 ? 29 : 28;
//     var daysOfMonth = [31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
  
//     var startDateNotPassedInEndYear = (endMonth < startMonth) || endMonth == startMonth && endDay < startDay;
//     var years = endYear - startYear - (startDateNotPassedInEndYear ? 1 : 0);
  
//     var months = (12 + endMonth - startMonth - (endDay < startDay ? 1 : 0)) % 12;
  
//     // (12 + ...) % 12 makes sure index is always between 0 and 11
//     var days = startDay <= endDay ? endDay - startDay : daysOfMonth[(12 + endMonth - 1) % 12] - startDay + endDay;
  
//     return years + "y" +" "+ months + "m" +" "+ days + "d";
//   }
//  function GetDays(){
//     var to = new Date(document.getElementById("to_field").value);
//     var from = new Date(document.getElementById("from_field").value);
//     var time =Math.floor(to.getTime() - from.getTime());
//     var day = 1000 * 60 * 60 * 24;
//     var days = Math.floor(diff/day);
//     var months = Math.floor(days/31);
//     var years = Math.floor(months/12);
//     return years + "y" +" "+ months + "m" +" "+ days + "d";
// }


//  function cal(){
//     if(document.getElementById("to_field")){
//     document.getElementById("years").value=GetDays();
//         }  
//     }
// function GetDays(){
//     var to = new Date(document.getElementById("to_field").value);
//     var from = new Date(document.getElementById("from_field").value);
//     var time =(to.getTime() - from.getTime()) / 1000;
//     var year  = Math.abs(Math.round((time/(60 * 60 * 24))/365.25));
//     var month = Math.abs(Math.round(time/(60 * 60 * 24 * 7 * 4)));
//     var days = Math.abs(Math.round(time/(3600 * 24)));
//     return year + "y" +" "+ month + "m" +" "+ days + "d";
// }




//  function cal(){
//     if(document.getElementById("to_field")){
//     document.getElementById("years").value=GetDays();
//         }  
//     }


    // function finch(){
    //     var numberOfDays = document.getElementById("sample").value;
    //     var years = Math.floor(numberOfDays / 365);
    //     var months = Math.floor(numberOfDays % 365 / 30);
    //     var days = Math.floor(numberOfDays % 365 % 30);
    //     return years + "y" +" "+ months + "m" +" "+ days + "d";
    // }

    // function testing() {
    
    //     document.getElementById("years").value = finch()
    // }


    //  <script>
// 		    function dateDifference(actualDate, value) {
//             // Calculate time between two dates:
//             const date1 = actualDate; // the date you already commented/ posted
//             const date2 = new Date(); // today
//             let r = {}; // object for clarity
//             let message;
//             const diffInSeconds = Math.abs(date2 - date1) / 1000;
//             const days = Math.floor(diffInSeconds / 60 / 60 / 24);
//             const hours = Math.floor(diffInSeconds / 60 / 60 % 24);
//             const minutes = Math.floor(diffInSeconds / 60 % 60);
//             const seconds = Math.floor(diffInSeconds % 60);
//             const milliseconds =
//             Math.round((diffInSeconds - Math.floor( diffInSeconds)) * 1000);
//             const months = Math.floor(days / 31);
//             const years = Math.floor(months / 12);
            
//             /* Below object is useful if you want to show difference in detailed context */
//             // if you want to return an object instead of a message
//             r = {
//             years: years,
//             months: months,
//             days: days,
//             hours: hours,
//             minutes: minutes,
//             seconds: seconds,
//             milliseconds: milliseconds
//             };
            
//                 /* If you want to display difference either in any one of the data in above object 'r'.*/
                
//                 // check if difference is in years or months
//                 if (years === 0 && months === 0) {
//                 // show in days if no years / months
//                     if (days > 0) {
//                         if (days === 1) {
//                         message = days + ' day';
//                         } else { 
//                             message = days + ' days ' ;
//                         }
//                     } else if (hours > 0) {
                            
//                         // show in hours if no years / months / days
//                         if (hours === 1) {
//                             message = hours + ' hour';
//                         } else {
//                             message = hours + ' hours'; 
//                         }
//                     } else {
//                     // show in minutes if no years / months / days / hours
//                         if (minutes === 1) {
//                         message = minutes + ' minute';
//                         } else { 
//                             message = minutes + ' minutes ' ; 
//                          }
//                     }
//                 } else if (years === 0 && months > 0) {
//                     // show in months if no years
//                     if (months === 1) {
//                         message = months + ' month';
//                     } else {
//                             message = months + ' months ' ;
                            
//                     }
//                 } else if (years > 0) {
//                     // show in years if years exist
//                     if (years === 1) {
//                     message = years + ' year';
//                     } else {
//                         message = years + ' years ' ;
                        
//                     }
//                 }
                
//                 // To display either an object or a message in the view
//                 if (value === true) {
//                     return r;
//                 }
//                 return message;
//             }
            
//             function contentUpdate() {
//                 // play with the postedDate as you  wish to check this function
//             const postedDate = new Date('July 30 2018 12:08');
            
//             // context
//             document.getElementById('context').innerHTML = `For example, consider a user X commented/posted something on SoloLearn Forum on <strong>${postedDate}</strong>`;
            
//             // result in the form of a message
//             const message = dateDifference(postedDate, false);
//             document.getElementById('message').innerHTML = `<p>Difference between <strong>${new Date()}</strong> and the posted time of user X comment/post can be displayed as "Posted <strong>${message}</strong> ago"</p>`;
            
//             // result in the form of a detailed object
//             const objectDate = dateDifference(postedDate, true);
//             document.getElementById('object').innerHTML = `<p>Difference between now and the posted time of user X comment/post in detail is "<strong>${objectDate.years}</strong> years, <strong>${objectDate.months}</strong> months, <strong>${objectDate.days}</strong> days, <strong>${objectDate.hours}</strong> hours, <strong>${objectDate.minutes}</strong> minutes, <strong>${objectDate.seconds}</strong> seconds, <strong>${objectDate.milliseconds}</strong> milliseconds ago"</p>`;
//             }
            
            
//             // to update content every one second
//             setInterval(contentUpdate, 1000);
            
//             // to update the content for the first time
//             contentUpdate();
// 		</script> 






//  function GetDays(){
//      var dropdt = new Date(document.getElementById("to_field").value);
//      var pickdt = new Date(document.getElementById("from_field").value);
//      return parseInt((dropdt - pickdt) / (24 * 3600 * 1000));
//  }
 
//   function cal(){
//      if(document.getElementById("to_field")){
//      document.getElementById("years").value=GetDays();
//          }  
//      }

//  var m1 = moment('2/22/2013','M/D/YYYY');
//  var m2 = moment('4/5/2014','M/D/YYYY');
//  var diff = moment.preciseDiff(m1, m2);
//  console.log(diff);
//  https://stackoverflow.com/questions/26063882/how-to-get-difference-between-2-dates-in-years-months-and-days-using-moment-js
//  https://www.tutsmake.com/javascript-difference-between-two-dates-in-years-months-days/


//     function diff_year_month_day(dt1, dt2) 
//     {
//  dt1 = new Date(document.getElementById("to_field").value);
//  dt2 = new Date(document.getElementById("from_field").value);
//  var time =(dt2.getTime() - dt1.getTime()) / 1000;
//  var year  = Math.abs(Math.round((time/(60 * 60 * 24))/365.25));
//  var month = Math.abs(Math.round(time/(60 * 60 * 24 * 7 * 4)));
//  var days = Math.abs(Math.round(time/(3600 * 24)));
//  return year +'Y'+" "+ month + 'M' +" "+days + 'D';
//     }
//     function call(){
//         if(document.getElementById("to_field")){
//         document.getElementById("years").value=diff_year_month_day();
//                                                 } 
//                     }

