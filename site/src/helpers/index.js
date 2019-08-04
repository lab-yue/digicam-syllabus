export function getListCount(list) {
  let map = {};
  for (let val in list) {
    map[val] = (map[val] || 0) + 1;
  }
}

export function collectSubjectInfo(subjects) {
  subjects.node.map((node) => ({
    teacherName: node.teacher && node.teacher.name,
    field: node.field,
    category: node.category
  }))
}