<template>
    <div>{{slug}}</div>
</template>

<script>
    export default {
        name: "index",
        mounted() {
            this.slug = this.$route.params.slug
        },
        data: () => ({
          slug: null,
        }),

    }
</script>

<style scoped>

</style>
