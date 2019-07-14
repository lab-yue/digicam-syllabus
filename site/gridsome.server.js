// Server API makes it possible to hook into various parts of Gridsome
// on server-side and add custom data to the GraphQL data layer.
// Learn more: https://gridsome.org/docs/server-api

// Changes here require a server restart.
// To restart press CTRL + C in terminal and run `gridsome develop`
const syllabus = require('../data/syllabus.json')

module.exports = function (api) {
  api.loadSource(({ addContentType, createReference, addReference }) => {

    const subjectType = addContentType({
      typeName: 'Subject',
      route: '/subject/:id'
    })
    const detailType = addContentType({
      typeName: 'Detail',
    })

    const teacherType = addContentType({
      typeName: 'Teacher',
      route: '/teacher/:id'
    })

    const categoyType = addContentType({
      typeName: 'Category',
      route: '/category/:id'
    })

    const fieldType = addContentType({
      typeName: 'Field',
      route: '/field/:id'
    })

    const yearType = addContentType({
      typeName: 'Year',
      route: '/year/:id'
    })

    const teachers = {}
    const categories = {}
    const years = {}
    const fields = {}

    const gather = (collection, key, code) => {
      if (key in collection) {
        collection[key].subjects.push(code)
      } else {
        collection[key] = {
          subjects: [code]
        }
      }
    }

    const create = (contentType, collection) => {
      Object.entries(collection).map(([key, val], id) => {
        collection[key].id = id.toString()

        contentType.addNode({
          id: id.toString(),
          name: key || "unknown",
          ...val,
          subjects: createReference('Subject', val.subjects)
        })
      })
    }

    syllabus.data.map(subject => {
      gather(teachers, subject.teacher, subject.code)
      gather(categories, subject.category, subject.code)
      gather(years, subject.year, subject.code)
      gather(fields, subject.field, subject.code)
    })

    create(teacherType, teachers)
    create(categoyType, categories)
    create(yearType, years)
    create(fieldType, fields)

    syllabus.data.map(subject => {

      const detail = { ...subject.detail };
      delete subject.detail
      const detailNode = detailType.addNode({
        ...detail,
        path: `subject/${subject.code}/detail`
      })
      subjectType.addNode({
        ...subject,
        id: subject.code,
        detail: createReference(detailNode),
        teacher: createReference('Teacher', teachers[subject.teacher].id),
        categories: createReference('Categoy', categories[subject.category].id),
        year: createReference('Year', years[subject.year].id)
      })
    })



  })

  api.createPages(({ createPage }) => {
    // Use the Pages API here: https://gridsome.org/docs/pages-api
  })
}
