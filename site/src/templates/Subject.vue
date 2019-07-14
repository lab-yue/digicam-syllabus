<template>
  <pre>{{JSON.stringify($page.subject,null,4)}}</pre>
</template>

<page-query>
query Subject($id: String!){
  subject: subject(id:$id) {
    title
    teacher{
      name
    }
  }
}
</page-query>

<script>
export default {};
</script>

<style lang="scss" scoped>
</style>
