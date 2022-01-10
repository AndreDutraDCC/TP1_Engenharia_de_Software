<template>
    <v-row :class="rowClass">
        <v-col cols="1" class="pa-0" v-if="callbackActionShow && (callbackAction.prepend)">
            <v-row :class="callbackAction.class" style="height:100%" align="start" justify="center">
                <v-col>
                    <v-tooltip bottom :disabled="!callbackAction.tooltip">
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn
                                v-bind="attrs"
                                v-on="on"
                                :color="callbackAction.color"
                                :height="callbackAction.size ? callbackAction.size : callbackAction.height"
                                :width="callbackAction.size ? callbackAction.size : callbackAction.width"
                                :disabled="callbackAction.disabled"
                                @click="$emit('action')"
                                fab
                                elevation="0"
                            >
                                <v-icon>
                                    {{callbackAction.icon ? callbackAction.icon : 'mdi-plus'}}
                                </v-icon>
                            </v-btn>
                        </template>
                        <span  v-if="callbackAction.tooltip">{{callbackAction.tooltip}}</span>
                    </v-tooltip>
                </v-col>
            </v-row>
        </v-col>

        <v-col :cols="(doubt || callbackActionShow) ? 11 : 12">

            <!-- <v-container 
                fluid
                v-if="type=='checkbox'"
                :ref='key2'
                v-model="select"
            >
                <p>{{ label }}</p>
                <v-checkbox
                    @change="update(), onChange()"
                    v-for="item in items"
                    :key="item"
                    :label="item"
                    :value="item"
                    v-model="select"
                    :color="color"
                    :hide-details="hideDetails"
                    :background-color="background"
                    :disabled="disabled"
                    :readonly="readonly"
                    :loading="loading"
                    :style="stylization"
                ></v-checkbox>
            </v-container> -->

            <v-checkbox
                :ref='key2'
                v-if="type=='checkbox'"
                @change="update(), onChange()"
                v-model="value1"
                :dense="dense"
                :label="label"
                :color="color"
                :hide-details="hideDetails"
                :background-color="background"
                :disabled="disabled"
                :readonly="readonly"
                :loading="loading"
                :style="stylization"
            ></v-checkbox>

            <v-radio-group
                :ref='key2'
                v-model="value1"
                v-if="type=='radio'"
                @change="update(), onChange()"
                :hide-details="hideDetails"
                :background-color="background"
                :disabled="disabled"
                :readonly="readonly"
                :loading="loading"
                :style="stylization"
                >
                <v-radio
                    v-for="item in items"
                    :key="item"
                    :label="item"
                    :value="item"
                ></v-radio>
            </v-radio-group>
            <v-autocomplete
                :ref='key2'
                v-if="type=='autocomplete'"
                v-model="value1"
                :items="items"
                :counter="counter"
                @change="update(), onChange()"
                :label="label"
                :chips="chips"
                :multiple="multiple"
                :dense="dense"
                :color="color"
                :rules="rules"
                :outlined="outlined"
                :placeholder="placeholder"
                :hint="hint"
                :persistent-hint="persistentHint"
                :prepend-icon="prependIcon"
                :prepend-inner-icon="prependInnerIcon"
                :prepend-outer-icon="prependOuterIcon"
                :append-icon="appendIcon"
                :append-inner-icon="appendInnerIcon"
                :append-outer-icon="appendOuterIcon"
                :hide-details="hideDetails"
                :background-color="background"
                :disabled="disabled"
                :readonly="readonly"
                :loading="loading"
                :filter="filter"
                :style="stylization"
                :prefix="prefix"
                :suffix="suffix"
            ></v-autocomplete>
            <v-select
                :ref='key2'
                v-if="type=='select'"
                v-model="value1"
                :items="items"
                @change="update(), onChange()"
                :label="label"
                :chips="chips"
                :multiple="multiple"
                :dense="dense"
                :color="color"
                :rules="rules"
                :outlined="outlined"
                :placeholder="placeholder"
                :hint="hint"
                :persistent-hint="persistentHint"
                :prepend-icon="prependIcon"
                :prepend-inner-icon="prependInnerIcon"
                :prepend-outer-icon="prependOuterIcon"
                :append-icon="appendIcon"
                :append-inner-icon="appendInnerIcon"
                :append-outer-icon="appendOuterIcon"
                :hide-details="hideDetails"
                :background-color="background"
                :disabled="disabled"
                :readonly="readonly"
                :loading="loading"
                :style="stylization"
            ></v-select>
            <v-switch
                :ref='key2'
                v-if="type=='switch'"
                @change="update(), onChange()"
                v-model="value1"
                :dense="dense"
                :label="label"
                :color="color"
                :value="value1"
                :background-color="background"
                :hide-details="hideDetails"
                :disabled="disabled"
                :readonly="readonly"
                :loading="loading"
                :style="stylization"
            ></v-switch>
            <v-textarea
                :auto-grow="autoGrow"
                :rows="rows"
                :ref='key2'
                v-model="value1"
                v-if="type=='textarea'"
                @keyup="update(), onChange()"
                :dense="dense"
                :label="label"
                :color="color"
                :rules="rules"
                :outlined="outlined"
                :placeholder="placeholder"
                :hint="hint"
                :persistent-hint="persistentHint"
                :prepend-icon="prependIcon"
                :prepend-inner-icon="prependInnerIcon"
                :prepend-outer-icon="prependOuterIcon"
                :append-icon="appendIcon"
                :append-inner-icon="appendInnerIcon"
                :append-outer-icon="appendOuterIcon"
                :hide-details="hideDetails"
                :background-color="background"
                :disabled="disabled"
                :readonly="readonly"
                :loading="loading"
                :style="stylization"
                :counter="counter"
                :prefix="prefix"
                :suffix="suffix"
            ></v-textarea>
            <v-text-field
                :ref='key2'
                v-model="value1"
                v-if="type=='phone'"
                v-mask="value1.replace(/[^\d]+/g,'').length <= 10 ? '(##) ####-####' : '(##) #####-####'"
                @keyup="update()"
                @change="onChange()"
                :label="label"
                :dense="dense"
                :rules="rules"
                :outlined="outlined"
                :placeholder="placeholder"
                :hint="hint"
                :persistent-hint="persistentHint"
                :prepend-icon="prependIcon"
                :prepend-inner-icon="prependInnerIcon"
                :prepend-outer-icon="prependOuterIcon"
                :append-icon="appendIcon"
                :append-inner-icon="appendInnerIcon"
                :append-outer-icon="appendOuterIcon"
                :hide-details="hideDetails"
                :background-color="background"
                :disabled="disabled"
                :readonly="readonly"
                :loading="loading"
                :style="stylization"
                :counter="counter"
                :prefix="prefix"
                :suffix="suffix"
            ></v-text-field>
            <v-text-field
                :ref='key2'
                v-model="value1"
                v-if="type=='cnpj'"
                v-mask="'##.###.###/####-##'"
                @keyup="update()"
                @change="onChange()"
                :label="label"
                :dense="dense"
                :rules="rules"
                :outlined="outlined"
                :placeholder="placeholder"
                :hint="hint"
                :persistent-hint="persistentHint"
                :prepend-icon="prependIcon"
                :prepend-inner-icon="prependInnerIcon"
                :prepend-outer-icon="prependOuterIcon"
                :append-icon="appendIcon"
                :append-inner-icon="appendInnerIcon"
                :append-outer-icon="appendOuterIcon"
                :hide-details="hideDetails"
                :background-color="background"
                :disabled="disabled"
                :readonly="readonly"
                :loading="loading"
                :style="stylization"
                :prefix="prefix"
                :suffix="suffix"
            ></v-text-field>
            <v-text-field
                :ref='key2'
                v-model="value1"
                v-if="type=='cep'"
                v-mask="'#####-###'"
                @keyup="update()"
                @change="onChange()"
                :label="label"
                :dense="dense"
                :rules="rules"
                :outlined="outlined"
                :placeholder="placeholder"
                :hint="hint"
                :persistent-hint="persistentHint"
                :prepend-icon="prependIcon"
                :prepend-inner-icon="prependInnerIcon"
                :prepend-outer-icon="prependOuterIcon"
                :append-icon="appendIcon"
                :append-inner-icon="appendInnerIcon"
                :append-outer-icon="appendOuterIcon"
                :hide-details="hideDetails"
                :background-color="background"
                :disabled="disabled"
                :readonly="readonly"
                :loading="loading"
                :style="stylization"
                :prefix="prefix"
                :suffix="suffix"
            ></v-text-field>
            <v-text-field
                :ref='key2'
                v-model="value1"
                v-if="type=='text'"
                @change="money(), onChange()"
                @keyup="update()"
                :label="label"
                :dense="dense"
                :rules="rules"
                :outlined="outlined"
                :placeholder="placeholder"
                :hint="hint"
                :persistent-hint="persistentHint"
                :prepend-icon="prependIcon"
                :prepend-inner-icon="prependInnerIcon"
                :prepend-outer-icon="prependOuterIcon"
                :append-icon="appendIcon"
                :append-inner-icon="appendInnerIcon"
                :append-outer-icon="appendOuterIcon"
                :hide-details="hideDetails"
                :background-color="background"
                :disabled="disabled"
                :readonly="readonly"
                :loading="loading"
                :style="stylization"
                :counter="counter"
                :prefix="prefix"
                :suffix="suffix"
            ></v-text-field>
            <v-text-field
                :ref='key2'
                v-model="value1"
                v-if="type=='percent'"
                @change="percent(), onChange()"
                @keyup="update()"
                :label="label"
                :dense="dense"
                :rules="rules"
                :outlined="outlined"
                :placeholder="placeholder"
                :hint="hint"
                :persistent-hint="persistentHint"
                :prepend-icon="prependIcon"
                :prepend-inner-icon="prependInnerIcon"
                :prepend-outer-icon="prependOuterIcon"
                :append-icon="appendIcon"
                :append-inner-icon="appendInnerIcon"
                :append-outer-icon="appendOuterIcon"
                :hide-details="hideDetails"
                :background-color="background"
                :disabled="disabled"
                :readonly="readonly"
                :loading="loading"
                :style="stylization"
                :counter="counter"
                :prefix="prefix"
                :suffix="suffix"
            ></v-text-field>
            <v-text-field
                :ref='key2'
                v-model="value1"
                v-if="type=='numeric'"
                type="number"
                @keyup="update()"
                @change="onChange()"
                :label="label"
                :dense="dense"
                :rules="rules"
                :outlined="outlined"
                :placeholder="placeholder"
                :hint="hint"
                :persistent-hint="persistentHint"
                :prepend-icon="prependIcon"
                :prepend-inner-icon="prependInnerIcon"
                :prepend-outer-icon="prependOuterIcon"
                :append-icon="appendIcon"
                :append-inner-icon="appendInnerIcon"
                :append-outer-icon="appendOuterIcon"
                :hide-details="hideDetails"
                :background-color="background"
                :disabled="disabled"
                :readonly="readonly"
                :loading="loading"
                :style="stylization"
                :counter="counter"
                :prefix="prefix"
                :suffix="suffix"
            ></v-text-field>
            <v-text-field
                :ref='key2'
                v-model="value1"
                v-if="type=='int'"
                type="number"
                step="1"
                @keyup="update()"
                @change="onChange()"
                :label="label"
                :dense="dense"
                :rules="rules"
                :outlined="outlined"
                :placeholder="placeholder"
                :hint="hint"
                :persistent-hint="persistentHint"
                :prepend-icon="prependIcon"
                :prepend-inner-icon="prependInnerIcon"
                :prepend-outer-icon="prependOuterIcon"
                :append-icon="appendIcon"
                :append-inner-icon="appendInnerIcon"
                :append-outer-icon="appendOuterIcon"
                :hide-details="hideDetails"
                :background-color="background"
                :disabled="disabled"
                :readonly="readonly"
                :loading="loading"
                :style="stylization"
                :counter="counter"
                :prefix="prefix"
                :suffix="suffix"
            ></v-text-field>
            <v-text-field
                :ref='key2'
                v-model="value1"
                v-if="type=='cpf'"
                v-mask="'###.###.###-##'"
                @keyup="update()"
                @change="onChange()"
                :label="label"
                :dense="dense"
                :rules="rules"
                :outlined="outlined"
                :placeholder="placeholder"
                :hint="hint"
                :persistent-hint="persistentHint"
                :prepend-icon="prependIcon"
                :prepend-inner-icon="prependInnerIcon"
                :prepend-outer-icon="prependOuterIcon"
                :append-icon="appendIcon"
                :append-inner-icon="appendInnerIcon"
                :append-outer-icon="appendOuterIcon"
                :hide-details="hideDetails"
                :background-color="background"
                :disabled="disabled"
                :readonly="readonly"
                :loading="loading"
                :style="stylization"
                :prefix="prefix"
                :suffix="suffix"
            ></v-text-field>
            <v-subheader
            class="pl-0"
            v-if="type=='slider'"
            >
                {{label}}
            </v-subheader>
            <v-slider
                :ref='key2'
                v-if="type=='slider'"
                @input="update()"
                @change="onChange()"
                v-model="value1"
                :dense="dense"
                :color="color"
                :hide-details="hideDetails"
                :track-color="trackColor"
                :thumb-color="thumbColor"
                :thumb-label="thumbLabel"
                :min="min"
                :max="max"
                :step="step"
                :append-icon="appendIcon"
                :prepend-icon="prependIcon"
                :background-color="background"
                :disabled="disabled"
                :readonly="readonly"
                :loading="loading"
                :style="stylization"
            >
            <template v-if="thumbValue" v-slot:thumb-label="value">
                {{ thumbValue }}
            </template>
            </v-slider>
            <ImageSelector :ref='key2' @uploaded="save" @update="update()" @change="onChange()" :filename="value1" :bucket="bucket" :subfolder="subfolder" :label="label" :ratio="ratio" :maxWidth="maxWidth" :disabled="readonly || disabled" v-if="type=='image'"/>
            <PDFuploader :ref='key2' @uploaded="save" @update="update()" @change="onChange()" :filename="value1" :bucket="bucket" :subfolder="subfolder" :label="label" :ratio="ratio" :maxWidth="maxWidth" :disabled="readonly || disabled" v-if="type=='pdf'"/>
            <fileUploader :ref='key2' @uploaded="save" @update="update()" @change="onChange()" :filename="value1" :bucket="bucket" :subfolder="subfolder" :label="label" :ratio="ratio" :maxWidth="maxWidth" :disabled="readonly || disabled" v-if="type=='file'"/>
        </v-col>
        <v-col cols="1" class="pa-0" v-if="callbackActionShow && !(callbackAction.prepend)">
            <v-row :class="callbackAction.class" style="height:100%" align="start" justify="center">
                <v-col>
                    <v-tooltip bottom :disabled="!callbackAction.tooltip">
                        <template v-slot:activator="{ on, attrs }">
                            <v-btn
                                v-bind="attrs"
                                v-on="on"
                                :color="callbackAction.color"
                                :height="callbackAction.size ? callbackAction.size : callbackAction.height"
                                :width="callbackAction.size ? callbackAction.size : callbackAction.width"
                                :disabled="callbackAction.disabled"
                                @click="$emit('action')"
                                fab
                                elevation="0"
                            >
                                <v-icon>
                                    {{callbackAction.icon ? callbackAction.icon : 'mdi-plus'}}
                                </v-icon>
                            </v-btn>
                        </template>
                        <span  v-if="callbackAction.tooltip">{{callbackAction.tooltip}}</span>
                    </v-tooltip>
                </v-col>
            </v-row>
        </v-col>
        <v-col cols="1" class="pa-0" v-if="doubt">
                <v-dialog
                v-model="dialog"
                width="500"
                >
                <template v-slot:activator="{ on, attrs }">
                    <v-row class="ma-0" style="height:100%" align="start" justify="center">
                        <v-col>
                            <v-btn
                            :color="doubt.color"
                            v-bind="attrs"
                            v-on="on"
                            fab
                            elevation="0"
                            x-small
                            >
                                <v-icon>
                                    {{doubt.icon ? doubt.icon : 'mdi-alert-circle-outline'}}
                                </v-icon>
                            </v-btn>
                        </v-col>
                    </v-row>
                </template>

                <v-card>
                    <v-card-title class="headline">
                    {{doubt.title}}
                    </v-card-title>

                    <v-card-text>
                    {{doubt.text}}
                    </v-card-text>

                    <v-divider></v-divider>

                    <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-btn
                        v-if="doubt.link"
                        color="primary"
                        text
                        @click="open(doubt.link)"
                    >
                        {{doubt.linkText ? doubt.linkText : 'Abrir'}}
                    </v-btn>
                    <v-btn
                        color="primary"
                        text
                        @click="dialog = false"
                    >
                        {{doubt.close}}
                    </v-btn>
                    </v-card-actions>
                </v-card>
                </v-dialog>
        </v-col>
    </v-row>
</template>
<script>
import numeral from 'numeral'
import ImageSelector from '@/components/forms/image/ImageSelector.vue'
import PDFuploader from '@/components/forms/pdf/PDFuploader.vue'
import fileUploader from '@/components/forms/file/fileUploader.vue'

export default {
    name: 'autoinput',
    components: {
        ImageSelector,
        PDFuploader,
        fileUploader,
    },
    props: [
     'type',
     'label',
     'rules',
     'outlined',
     'placeholder',
     'hint',
     'persistentHint',
     'prependIcon',
     'prependInnerIcon',
     'prependOuterIcon',
     'appendIcon',
     'appendInnerIcon',
     'appendOuterIcon',
     'color',
     'trackColor',
     'thumbColor',
     'thumbLabel',
     'thumbValue',
     'min',
     'max',
     'step',
     'hideDetails',
     'items',
     'chips',
     'multiple',
     'dense',
     'doubt',
     'callbackAction',
     'monetary',
     'background',
     'disabled',
     'loading',
     'filter',
     'stylization',
     'value',
     'ratio',
     'counter',
     'readonly',
     'prefix',
     'suffix',
     'bucket',
     'subfolder',
     'maxWidth',
     'key2',
     'rows',
     'autoGrow',
     'rowConfig'
     ],
    data(){
        return {
            value1: '',
            dialog: false,
            select: [],
        }
    },
    methods: {
        open(link){
            window.open(link, '_blank')
        },
        save (url) {
            this.value1 = url
            this.update()
        },
        money(){
            if(this.monetary){
                this.value1 = this.value1 ? numeral(this.value1).format('$ 0,0.00') : ''
            }
        },
        percent(){
            if(this.value1){
                let val1 = parseFloat(this.value1.toLocaleString('pt-Br').replace('%','').replace('\.','').replace('\,','\.'))
                val1 = numeral(val1).value()
                val1 = val1/100
                this.value1 = numeral(val1*100).format('#,###.##')+'%'
                this.$emit('input', val1)
                this.$emit('update')
            }
        },
        update() {
            if(this.type=='switch') this.$emit('input', !!this.value1)
            else this.$emit('input', this.value1)
            this.$emit('update', this.key2)
        },
        onChange() {
            if(this.type=='switch') this.$emit('input', !!this.value1)
            else this.$emit('input', this.value1)
            this.$emit('onChange', this.key2)
        },
        start(){
            this.value1 = this.value ? this.value : ''
        }
    },
    beforeMount(){
        this.value1 = this.value ? this.value : ''
    },
    mounted() {
        this.type == 'percent' ? this.percent() : ''
    },
    computed: {
        callbackActionShow(){
            return !!this.callbackAction && !this.disable
        },
        rowClass(){
            return this.rowConfig.rowClassPersonalize ? this.rowConfig.rowClass : "px-4 mr-3 mt-1"
        }
    }
}
</script>
<style lang="scss">
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none !important;
  margin: 0;
}
input[type=number] {
  -moz-appearance: textfield !important;
}
</style>