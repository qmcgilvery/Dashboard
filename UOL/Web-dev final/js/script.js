$(document).ready(function () {

    // Sorts leaderboard by "Total" category
    $('#leaderboard').DataTable({
        "order": [[5, "asc"]]
    });
    $('.dataTables_length').addClass('bs-select');

    // Function to set cookie with name, value and expiration date
    function setCookie(cname, cvalue, exdays) {
        const d = new Date();
        d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
        let expires = "expires=" + d.toGMTString();
        document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    }

    // Returns cookie if it exists
    function getCookie(cname) {
        let name = cname + "=";
        let decodedCookie = decodeURIComponent(document.cookie);
        let ca = decodedCookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) === ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) === 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    }

    // Checks if cookie has been set, displays modal and sets cookie if it has not been.
    function checkCookie() {
        let user = getCookie("modal");
        if (!user) {
            $('#myModal').modal('show')
            setCookie("modal", true, 10);
        }
    }

    setTimeout(checkCookie, 5000)
});


