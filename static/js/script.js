// <!-- Image bind when create region-->
$(document).ready(() => {
    $("#fileImage").change(function () {
        const file = this.files[0];
        if (file) {
            let reader = new FileReader();
            reader.onload = function (event) {
                $("#imgPreview")
                    .attr("src", event.target.result);
            };
            reader.readAsDataURL(file);
        }
        else {
            var img = "media/region_image/default.jpg";
            $("#imgPreview").attr("src", img);
        }
    });
});

// <!-- Form validation -->
function validateForm() {
    let image_data = document.forms["formCreate"]["imgPreview"].value;
    if (image_data == "") {
        alert("Should upload image");
        return false;
    }
    let region_code_data = document.forms["formCreate"]["txtRegionCode"].value;
    if (region_code_data == "") {
        alert("Region code must be filled out");
        return false;
    }
    if (isNaN(region_code_data)){
        alert("Region code must be integer field");
        return false;
    }
    let region_name_data = document.forms["formCreate"]["txtRegionName"].value;
    if (region_name_data == "") {
        alert("Region name must be filled out");
        return false;
    }
    if (!isNaN(region_name_data)){
        alert("Region name must not be numeric");
        return false;
    }
    let country_data = document.forms["formCreate"]["ddlCountry"].value;
    if (country_data == "0") {
        alert("Country should be selected");
        return false;
    }
}

// <!-- Bind data for edit -->
function edit(ID) {
    $('#formCreateID').attr('action', 'disabled')
    $('#imgPreview').attr('value', 'disabled')
    $('#txtRegionCode').attr('value', 'disabled')
    $('#txtRegionName').attr('value', 'disabled')
    $('#ddlCountry').attr('value', 'disabled')
    $('#btnSave').attr('style', 'display: None;');
    $('#btnUpdate').attr('style', 'disabled')
    $.ajax({
        url: 'http://127.0.0.1:8000/api/api_region/' + ID + '/',
        method: 'GET',
        data: '',
        dataType: 'json',
    }).done(function (data) {
        console.log(data);
        if (data.image == "" || data.image == null) {
            $('#fileImage').prop('required', true);
        } else {
            $('#fileImage').prop('required', false);
        } console.log(data.image)
        $('#imgPreview').attr('src', data.image)
        $('#txtRegionCode').val(data.code)
        $('#txtRegionName').val(data.name)
        $('#ddlCountry').val(data.country)
        console.log(data);
        $('#formCreateID').attr('action', '/update/' + ID + '/');
    });
}

// <!-- messages -->
$(document).ready(function () {
    window.setTimeout(function () {
        $(".alert").fadeTo(1000, 0).slideUp(1000, function () {
            $(this).remove();
        });
    }, 2000);
});

