<template>
  <syllabus-layout>
    <v-card width="1500" class="mx-auto">
      <v-card-title class="s-title">
        {{ $page.category.name }}
        <v-chip class="ma-2" color="primary" outlined>
          講義数
          <v-avatar right class="primary darken-2">
            <span class="white--text">{{ subjects.length }}</span>
          </v-avatar>
        </v-chip>
      </v-card-title>

      <v-container class="pa-2" fluid>
        <syllabus-statistics :subjects="$page.category.subjects" :keys="['teacher']" />
        <syllabus-list :items="subjects" />
      </v-container>
    </v-card>
  </syllabus-layout>
  <!--
  <syllabus-layout class="teacher">
    <h1 class="syllabus-page-title">{{ $page.category.name }}</h1>
    <p class="teacher-subjects-count">
      講義数
      <span class="syllabus-page-title-count">{{ subjects.length }}</span>
    </p>

    <syllabus-statistics :subjects="$page.category.subjects" :keys="['teacher']" />

    <syllabus-list :items="subjects" />
  </syllabus-layout>
  -->
</template>

<page-query>
query Category($id: String!) {
  category: category(id: $id) {
    name
    subjects {
      node {
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
export default {
  metaInfo() {
    return {
      title: this.$page.category.name
    };
  },
  computed: {
    subjects() {
      let items = this.$page.category.subjects.node.map(({ title, id }) => {
        return {
          id,
          name: title,
          url: `/subject/${id}`
        };
      });
      return items;
    }
  }
};
</script>

<style lang="scss" scoped>
.s {
  &-title {
    margin: 30px 0 10px 30px;
  }
}
.teacher {
  &-subjects {
    &-count {
      color: $theme-green;
      text-align: center;
    }
  }
}
</style>
