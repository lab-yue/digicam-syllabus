<template>
  <syllabus-layout>
    <v-card width="1500" class="mx-auto">
      <v-card-title class="s-title">
        <v-tooltip top>
          <template v-slot:activator="{ on }">
            <span v-on="on">
              <a
                :href="`https://www.google.com/search?q=${$page.teacher.name}`"
                rel="noopener"
                target="_blank"
              >{{ $page.teacher.name }}</a>
            </span>
          </template>
          <span>{{$page.teacher.position}}</span>
        </v-tooltip>
        <v-chip class="ma-2" color="primary" outlined>
          講義数
          <v-avatar right class="primary darken-2">
            <span class="white--text">{{ subjects.length }}</span>
          </v-avatar>
        </v-chip>
      </v-card-title>

      <v-container class="pa-2" fluid>
        <syllabus-statistics :subjects="$page.teacher.subjects" :keys="['field','category']" />
        <syllabus-list :items="subjects" />
      </v-container>
    </v-card>
  </syllabus-layout>
  <!--
  <syllabus-layout class="teacher">
    <h1 class="syllabus-page-title">
      <a
        class="teacher-search"
        :href="`https://www.google.com/search?q=${$page.teacher.name}`"
        rel="noopener"
        target="_blank"
      >{{ $page.teacher.name }}</a>
    </h1>

    <p class="teacher-subjects-count">
      講義数
      <span class="syllabus-page-title-count">{{ subjects.length }}</span>
    </p>

    <syllabus-statistics :subjects="$page.teacher.subjects" :keys="['field','category']" />

    <syllabus-list :items="subjects" />
  </syllabus-layout>
  -->
</template>

<page-query>
query Teacher($id: ID!) {
  teacher: teacher(id: $id) {
    name
    position
    subjects {
      node {
        id
        title
        field {
          id
          name
        }
        category {
          name
          id
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
      title: this.$page.teacher.name
    };
  },
  computed: {
    subjects() {
      let subjects = this.$page.teacher.subjects.node.map(({ title, id }) => {
        return {
          id,
          name: title,
          url: `/subject/${id}`
        };
      });
      return subjects;
    }
  }
};
</script>

<style lang="scss" scoped>
.teacher {
  &-search {
    cursor: help;
  }
  &-subjects {
    &-count {
      color: $theme-green;
      text-align: center;
    }
  }
}
.s {
  &-title {
    margin: 30px 0 10px 30px;
  }
}
</style>
