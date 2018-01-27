const bundle = []
const bannerMap = {}
const voteMap = {}

function updateTimer(remaining, maximum) {
    var timeStr = formatTime(remaining);
    remaining /= maximum
    var i = 0;

    $("#timer").children("div").each(function() {
        var width = Math.min(remaining, (i+1) * .1);
        remaining -= width;
        $(this).width((width * 100) + "%");

        if(remaining == 0) {
            $(this).html(timeStr);
        } else {
            $(this).html("");
        }
        i++;
    });
}

function formatTime(seconds) {
    var minutes = Math.floor(seconds / 60);
    seconds %= 60;

    return minutes + ":" + seconds;
}

function createBanner(id, song) {
    return bannerMap[id] = $("<div class=banner></div>")
        .css("background-image", "url(" + song["artist_image"] + ")")
        .append("<div class=bar></div>")
        .append($("<img class=albumart>").attr("src", song["cover_url"]))
        .append($("<div class=details-wrapper></div>")
            .append($("<div class=songtitle></div>").html(song["title"]))
            .append($("<div class=artist></div>").html(song["artist"])))
        
        .click(function() {
            castVote(id);
        });
}

function getVote(id) {
    return id in voteMap ? voteMap[id] : 0;
}

function castVote(id) {
    if(!(id in bundle)) {
        console.log("Song not in current bundle")
    }

    if(!(id in voteMap)) {
        voteMap[id] = 0;
    }
    ++voteMap[id];

    updateBanners();
}

function getVoteCount() {
    var count = 0;

    for(id in voteMap) {
        count += voteMap[id];
    }
    return count;
}

function getMaxVote() {
    var max = 0;

    for(id in voteMap) {
        if(voteMap[id] > max) {
            max = voteMap[id];
        }
    }
    return max;
}

function updateBanners() {
    var totalVotes = getVoteCount();

    for(id in bannerMap) {
        var banner = bannerMap[id];
        var percentage = voteMap[id] / totalVotes * 100;
        var width = voteMap[id] / getMaxVote() * 100

        banner.find(".bar").width(percentage + "%")
            .attr("data-percent", Math.round(percentage));
    }
}

function grabBundle(bundle) {
    bundle = $(bundle);

    $.getJSON("/api/v1/club/", function(data) {
        bundle.empty();

        for(var key in data["songs"]) {
            var song = data["songs"][key];

            bundle.append(createBanner(key, song));
        }
    })
}
