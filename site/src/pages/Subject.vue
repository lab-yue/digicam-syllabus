<template>
  <div>
    <h2>Subjects</h2>
    <ul>
      <li v-for="edge in $page.allSubject.edges" :key="edge.node.id">
        <g-link :to="`/subject/${edge.node.id}`">{{ edge.node.title }}</g-link>
        {{edge.node.teacher? edge.node.teacher.name : ""}}
      </li>
    </ul>
  </div>
</template>

<page-query>
query {
    allSubject {
    edges{
      node{
        id
        title
        teacher {
          id
          name
        }
      }
    }
  }
}
</page-query>

<script>
export default {};
</script>


<style lang="scss" scoped>
</style>
