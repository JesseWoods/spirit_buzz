function prepareDocument(){
    jQuery("#submit_review").click(addProductReview);
    jQuery("#review_form").hide();
    jQuery("#add_review").click(slideToggleReviewForm);
    jQuery("#add_review").addClass('visible');
    jQuery("#cancel_review").click(slideToggleReviewForm);
    jQuery("#same_as_billing").click(sameAsBilling);
    jQuery("form#search").submit(function(){
        text = jQuery("#id_q").val();
        if (text == ""){
            alert("Please enter a search term.");
            return false;
        }
    });

}
function sameAsBilling(){
    document.getElementById("id_shipping_name").value=  document.getElementById("id_billing_name").value;
    document.getElementById("id_shipping_address_1").value=  document.getElementById("id_billing_address_1").value;
    document.getElementById("id_shipping_address_2").value=  document.getElementById("id_billing_address_2").value;
    document.getElementById("id_shipping_city").value=  document.getElementById("id_billing_city").value;
    document.getElementById("id_shipping_state").value=  document.getElementById("id_billing_state").value;
    document.getElementById("id_shipping_zip").value=  document.getElementById("id_billing_zip").value;
    document.getElementById("id_shipping_country").value=  document.getElementById("id_billing_country").value;
}
function slideToggleReviewForm(){
    jQuery("#review_form").slideToggle();
    jQuery("#add_review").slideToggle();
}
function addProductReview(){

    var review = {
        title: jQuery("#id_title").val(),
        content: jQuery("#id_content").val(),
        rating: jQuery("#id_rating").val(),
        slug: jQuery("#id_slug").val(),
    };



    $.getJSON('/review/product/add/', review, function(response){
            jQuery("#review_errors").empty();

            if(response.success == "True"){
                jQuery("#submit_review").attr('disabled', 'disabled');
                jQuery("#no_reviews").empty();
                jQuery("#reviews").prepend(response.html).slideDown();
                new_review = jQuery("#reviews").children(":first");
                new_review.addClass("new_review");
                jQuery("#review_form").slideToggle();
            }
            else{
                jQuery("#review_errors").append(response.html);
            }
        });

}


jQuery(document).ready(prepareDocument);