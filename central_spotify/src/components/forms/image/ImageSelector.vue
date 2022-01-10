<template>
    <v-card elevation-1>
      <v-card-title>
        {{label}}
      </v-card-title>
      <v-card-text>
        <v-img v-if="data && !loading" elevation-2 :src="data" :lazy-src="dataLazy" max-width="250" class="imgPreview"></v-img>
        <v-progress-linear v-if="loading" indeterminate></v-progress-linear>
        <v-btn v-if="data" block @click="openImage" color="primary" text>
          <v-icon class="mx-3">mdi-open-in-new</v-icon>
          Ver Imagem
        </v-btn>
        <v-btn v-if="!disabled" block @click="dialog = !dialog" color="primary" text>
          <v-icon class="mx-3"> {{data ? 'mdi-folder-refresh' : 'mdi-folder-multiple-image'}} </v-icon>
          {{data ? 'Trocar Imagem' : 'Selecionar Imagem'}}
        </v-btn>
        <CropperDialog :show="dialog" @close="close()" @crop="cropped" :ratio="ratio" />
      </v-card-text>
    </v-card>
</template>
<script>

// import AvatarCropper from "vue-avatar-cropper";
// @ is an alias to /src
import CropperDialog from './CropperDialog'
import Upload from '@/service/upload'
const upload = new Upload()
import {getUrl} from '@/service/optimizer'

export default {
  name: "ImageSelector",
  components: { CropperDialog },
  props: ['ratio', 'filename','bucket', 'subfolder', 'label', 'disabled', 'maxWidth'],
  data() {
    return {
      dialog: false,
      data: '',
      dataLazy: '',
      url: '',
      loading: false
    };
  },
  methods: {
    openImage(){
      window.open(this.data, '_blank')
    },
    close(){
      this.dialog = false
      this.$emit('update')
    },
    async cropped(data){
        this.loading = true
        let maxWidth = this.maxWidth ? parseInt(this.maxWidth) : undefined
        let maxHeight = this.maxWidth ? parseInt(this.maxWidth / this.ratio) : undefined
        let res = await upload.image(data, this.bucket, this.subfolder, maxWidth, maxHeight)
        this.url = res.fileURLKey
        this.loading = false
        this.data = data
        this.$emit('uploaded', this.url)
    }

  },
  mounted(){
    if(this.filename){
      this.data = getUrl(this.filename, this.bucket, this.newWidth, this.newHeight)
      this.dataLazy = getUrl(this.filename, this.bucket, 50, (this.ratio ? 50 / this.ratio: undefined))
    }
  },
  computed: {
    newWidth() {
      return this.width ? this.width : 1000
    },
    newHeight() {
      if(this.height) return this.height
      else return this.ratio ? this.whidth / this.ratio : undefined
    }
  }
};
</script>
<style lang="scss" scoped>
.imgPreview {
  margin: 15px auto !important;
  border-radius: 5px;
  box-shadow: 5px 5px 8px -6px black !important; 
}
</style>
