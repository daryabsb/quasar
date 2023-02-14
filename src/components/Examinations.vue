<template>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" src="/examinations/skeletal.jpg" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Skeletal Class
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.skeletal_class }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" src="/examinations/nasolabial.jpg" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Nasolabial Angle
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.nasolabial_angle }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" src="/examinations/sulcus.jpg" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Nasolabial Sulcus
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.nasolabial_sulcus }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" src="/examinations/overjet.jpg" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Overjet
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.overjet }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Oral Hygiene
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.oral_hygiene }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Lip Competency
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.lip_competency }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Face Form
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.face_form }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Habit
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.habit }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Treated Arch
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.treated_arch }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Molar Class Left
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.molar_class_left }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Molar Class Right
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.molar_class_right }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Tongue Size
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.tongue_size }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Bracket System
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.bracket_system }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Midline Upper
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.midline_upper }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Midline Lower
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.midline_lower }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Slot
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.slot }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Extraction Upper
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.extraction_upper }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Extraction Lower
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.extraction_lower }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Anchorage Upper
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.anchorage_upper }}</p>
        </div>
    </div>
    <div class="text-center md:flex md:items-start md:text-left lg:block lg:text-center py-2">
        <div class="md:flex-shrink-0">
            <div class="flow-root">
                <img class="-my-1 mx-auto h-24 w-auto" :src="exam.imageUrl" alt="" />
            </div>
        </div>
        <div class="mt-3 md:mt-0 md:ml-4 lg:mt-3 lg:ml-0">
            <h3 class="text-base font-medium text-gray-900">Treatment Plan
            </h3>
            <p class="mt-1 text-sm text-gray-500">{{ examinations.treatment_plan }}</p>
        </div>
    </div>

</template>

<script setup>

defineProps({
    examinations: { type: Object, required: true },
    exam: { type: Object, required: true }
})

</script>