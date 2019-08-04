export function getListCount(list) {
  let map = {};
  for (let val of list) {
    map[val] = (map[val] || 0) + 1;
  }
  return map
}

export function collectSubjectInfo(subjects, fieldList) {

  let fieldMap = Object.fromEntries(fieldList.map(field => [field, {}]))

  let returnMap = {}
  subjects.node.map((node) => {
    fieldList.map(field => {
      fieldMap[field][node[field] || '不明'] = (fieldMap[field][node[field]] || 0) + 1;
    })
  })

  Object.entries(fieldMap).map(([field, fieldCount]) => {
    returnMap[field] = []
    Object.keys(fieldCount).map((key, id) => {
      returnMap[field].push({
        id,
        extra: fieldCount[key],
        name: key,
        url: `#`
      })
    }
    )
  })

  return returnMap;
}