export default function getListCount(list) {
    let map = {}
    for (let val in list) {
        map[val] = (map[val] || 0) + 1
    }
}