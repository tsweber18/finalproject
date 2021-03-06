
var ship1string=`Congratulations to `+aname+`! Due to the expedience in applying (rather than us having to draft them), they've been selected to serve on a Maelstrom-class
    battleship out on the new battlefront against the disgusting, revolting, and ferocious Tyranid swarm!  It's a very prestigious post, but they've selected to take out the
    `+aship+`, which is a hearty vessel that will take them far and wide.  They'll see and obliterate worlds far less beautiful and useful than `+aworld+`.  Don't worry,
    they're just a bunch of bugs. They're ugly and don't have feelings.  Thanks again for your service, `+aname+`!  Now hurry up and get out there before they get us first!`;

var ship2string= bname+`! Get all the social contact that you can, because you've been assigned to the long and luxurious bout of loneliness that comes with outer space patrol!
    You'll be on your faithful Rifter-class frigate called the `+bname+`, and it will be your only source of company for the next few months.  Or years.  Don't worry, the
    on-board voice isn't too robotic anymore and can talk about such exciting topics as advanced math and plot coursing.  You'll likely never communicate with a human while you're
    out there unless something bad is happening.  I hope you didn't like it much on `+bworld+`, because on their return, they'll like it a lot more!`;
    
var ship3string=`We're hoping that `+cname+` is a lover of industry, because he's out to get us the much needed resources that our expanding civilization requires.  Having long since
    depleted the most useful resources on `+cworld+`, it was decided that all those joining the Imperial Navy from there should be sent to get...well...more!  They'll be on a hardy
    but totally vulnerable Retriever-class mining vessel called the `+cship+`, looking out in the scattered and lonely asteroid belts for things that will make us rich and make them
    a great contributor to our success.  Thanks for your level of commitment to refining and manufacturing, `+cname+`!`;

function ship1(){
    document.getElementById('storyOutput').innerHTML = ship1string;
}

function ship2(){
    document.getElementById('storyOutput').innerHTML = ship2string;
}

function ship3(){
    document.getElementById('storyOutput').innerHTML = ship3string;
}