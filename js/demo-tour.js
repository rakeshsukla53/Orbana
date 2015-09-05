"use strict";



$(function(){

    // Instance the tour
    var tour = new Tour({
        storage: false,
        steps: [
         {
          element: "#tour-step-1",
          title: "Orbona? Ohana?",
          content: "According to the Romans, Orbona was the goddess of children and orphans, and would grant new children to parents for a second chance.",
          placement: "right"
         },
            {
          element: "#tour-step-2",
          title: "Activity Location",
          content: "The general area of activity, determined by referencing area codes.",
          placement: "right"
        },
        {
          element: "#tour-step-3",
          title: "Local Statistics",
          content: "Wondering when and where human trafficking is? We'll let you know right here.",
          placement: "top"
        },
        {
          element: "#tour-step-4",
          title: "Data Visualization",
          content: "We've made understanding several thousand sets of data easier on the eyes and the mind.",
          placement: "top"
        },
        {
          element: "#tour-step-5",
          title: "Social Awareness",
          content: "Listen into local conversations so you're always informed. Click on the Square above to contact organizations and representatives directly.",
          placement: "left"
        },
        {
          element: "#tour-step-6",
          title: "In Depth",
          content: "If you want to go deeper, we have enough data to satisfy even the most curious.",
          placement: "top"
        }
    ]});

    // Initialize the tour
    tour.init();


    $(".start-tour").on("click",function(){        
        tour.start();
    });    
        
});