function horseRace(input) {

    let horses = input.shift().split("|");

    
    for (let command of input) {
        if (command === "Finish") {
            console.log(horses.join("->"));
            console.log(`The winner is: ${horses[Object.keys(horses).length - 1]}`);
            break;
        }

        let [action, arg1, arg2] = command.split(" ");

        switch (action) {
            case "Retake":
                retake(arg1, arg2);
                break;
            case "Trouble":
                trouble(arg1);
                break;
            case "Rage":
                rage(arg1);
                break;
            case "Miracle":
                miracle();
                break;
        }
    }

    function retake(overtakingHorse, overtakenHorse) {

        let overtakingIndex = horses.indexOf(overtakingHorse);
        let overtakenIndex = horses.indexOf(overtakenHorse);
        const overtaking = horses[overtakingIndex];
        const overtaken = horses[overtakenIndex];

        if (overtakingIndex < overtakenIndex) {
            horses[overtakingIndex] = overtaken;
            horses[overtakenIndex] = overtaking;

            console.log(`${overtakingHorse} retakes ${overtakenHorse}.`);
        }
    }
    
    function trouble(horseName) {
        if (horses.includes(horseName) ) {
        let horseIndex = horses.indexOf(horseName);
        const horse = horses[horseIndex];
        if (horseIndex > 0 ) {
            horses.splice(horseIndex, 1)
            horses.splice(horseIndex - 1, 0 , horse)
            console.log(`Trouble for ${horseName} - drops one position.`);
        }
    }}

    function rage(horseName) {
        let horseIndex = horses.indexOf(horseName);
        const horse = horses[horseIndex];
        if (horseIndex === horses.length-2) {
            horses.splice(horseIndex, 1)
            horses.splice(horseIndex + 1, 0 , horse)
            // console.log('Thuis horse is in second place')
        } else if (horseIndex === horses.length - 1) {           
        } else {
            horses.splice(horseIndex, 1)
            horses.splice(horseIndex + 2, 0 , horse)
        }
         console.log(`${horseName} rages 2 positions ahead.`);
         
        }

    function miracle() {
        const lastHorse = horses[0];
        horses.splice(0, 1);
        
        horses.push( lastHorse);
            
        console.log(`What a miracle - ${lastHorse} becomes first.`);
    }
}


horseRace((["Bella|Alexia|Sugar", 'Retake Alexia Sugar', "Rage Bella", 'Trouble Bella', "Finish"]));
// Output: Alexia retakes Sugar. Bella rages 2 positions ahead. Trouble for Bella - drops one position. Sugar->Bella->Alexia. The winner is: Alexia




