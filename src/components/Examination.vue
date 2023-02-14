<template>
    <div class="bg-white">
        <div class="mx-auto  px-3 lg:px-4">

            <div class=" xl:grid xl:grid-cols-4 xl:gap-x-8 xl:gap-y-8 divide-y">
                <div class="col-span-4 ">
                    <h2 class="text-lg font-semibold text-indigo-600">Notes</h2>

                    <p class="mt-2 text-sm text-gray-500">Ac euismod vel sit maecenas id pellentesque eu sed
                        consectetur. Malesuada adipiscing sagittis vel nulla nec. Urna, sed a lectus elementum blandit
                        et.</p>
                </div>
                <div class="mt-2 sm:mt-4 md:mt-6 md:grid md:grid-cols-4 md:gap-x-8 xl:col-span-4 xl:mt-0">
                    <ul role="list" class="divide-y divide-gray-200">
                        <template v-for="(feature) in features.slice(0, 5)" :key="feature.id">

                            <li class="flex py-1">
                                <CheckIcon class="h-6 w-6 flex-shrink-0 text-green-500" />
                                <span class="ml-1 text-base text-gray-500 text-left">
                                    <p class="font-semibold">{{ feature.name }}</p>
                                    <p class="text-sm font-semibold first-letter:uppercase text-indigo-800">{{
                                        feature.value
                                    }}</p>

                                </span>
                            </li>
                        </template>
                    </ul>
                    <ul role="list" class="divide-y divide-gray-200 border-t border-gray-200 md:border-t-0">
                        <template v-for="(feature) in features.slice(5, 10)" :key="feature.id">

                            <li class="flex py-1">
                                <CheckIcon class="h-6 w-6 flex-shrink-0 text-green-500" />
                                <span class="ml-1 text-base text-gray-500 text-left">
                                    <p class="font-semibold">{{ feature.name }}</p>
                                    <p class="text-sm font-semibold first-letter:uppercase text-indigo-800">{{
                                        feature.value
                                    }}</p>

                                </span>
                            </li>
                        </template>
                    </ul>
                    <ul role="list" class="divide-y divide-gray-200">
                        <template v-for="(feature) in features.slice(10, 15)" :key="feature.id">

                            <li class="flex py-1">
                                <CheckIcon class="h-6 w-6 flex-shrink-0 text-green-500" />
                                <span class="ml-1 text-base text-gray-500 text-left">
                                    <p class="font-semibold">{{ feature.name }}</p>
                                    <p class="text-sm font-semibold first-letter:uppercase text-indigo-800">{{
                                        feature.value
                                    }}</p>

                                </span>
                            </li>
                        </template>
                    </ul>
                    <ul role="list" class="divide-y divide-gray-200 border-t border-gray-200 md:border-t-0">
                        <template v-for="(feature) in features.slice(15, 20)" :key="feature.id">

                            <li class="flex py-1">
                                <CheckIcon class="h-6 w-6 flex-shrink-0 text-green-500" />
                                <span class="ml-1 text-base text-gray-500 text-left">
                                    <p class="font-semibold">{{ feature.name }}</p>
                                    <p class="text-sm font-semibold first-letter:uppercase text-indigo-800">{{
                                        feature.value
                                    }}</p>

                                </span>
                            </li>
                        </template>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { CheckIcon } from '@heroicons/vue/24/outline'
const props = defineProps({
    examinations: { type: Object, required: true },

})
const features = [
    { id: 1, name: 'Skeletal Class', value: props.examinations.skeletal_class },
    { id: 2, name: 'Nasolabial Angle', value: props.examinations.nasolabial_angle },
    { id: 3, name: 'Nasolabial Sulcus', value: props.examinations.nasolabial_sulcus },
    { id: 4, name: 'Overjet', value: props.examinations.overjet },
    { id: 5, name: 'Oral Hygiene', value: props.examinations.oral_hygiene },
    { id: 6, name: 'Lip Competency', value: props.examinations.lip_competency },
    { id: 7, name: 'Face Form', value: props.examinations.face_form },
    { id: 8, name: 'Habit', value: props.examinations.habit },
    { id: 9, name: 'Treated Arch', value: props.examinations.treated_arch },
    { id: 10, name: 'Molar Class Left', value: props.examinations.molar_class_left },
    { id: 12, name: 'Molar Class Right', value: props.examinations.molar_class_right },
    { id: 13, name: 'Tongue Size', value: props.examinations.tongue_size },
    { id: 14, name: 'Bracket System', value: props.examinations.bracket_system },
    { id: 15, name: 'Midline Upper', value: props.examinations.midline_upper },
    { id: 16, name: 'Midline Lower', value: props.examinations.midline_lower },
    { id: 17, name: 'Slot', value: props.examinations.slot },
    { id: 18, name: 'Extraction Upper', value: props.examinations.extraction_upper },
    { id: 19, name: 'Extraction Lower', value: props.examinations.extraction_lower },
    { id: 20, name: 'Anchorage Upper', value: props.examinations.anchorage_upper },
    { id: 21, name: 'Treatment Plan', value: props.examinations.treatment_plan },
]
</script>