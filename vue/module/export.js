
// export let PLAYERS = ["손흥민", "이승우", "이강인"];
// export const MAX_SIZE = 1000;
// export function add(n1, n2) {
//     return n1 + n2;
// }

// component
export default {
    template: `<div>My Template</div>`,
    data() {
        return {
            num: 20,
        }
    },
    log() {
        console.log("log() is called");
        return "안녕";
    }
};

//export { PLAYERS, MAX_SIZE, add, obj };