export interface Client {
  id: number;
  user: number;
  name: string;
  dob: string;
  date_bonding: string;
  age: number;
  gender: string;
  address: number;
  phone: string;
  email: string;
  description: string;
  status: string;
  created: string;
  updated: string;
  image: string;
}

export interface Attachment {
  id: number;
  client: number;
  file_type: string;
  filename: string;
  file: string;
  page_count: number;
}

export interface Examination {
  id: number;
  skeletal_class: string;
  nasolabial_angle: string;
  nasolabial_sulcus: string;
  overjet: string;
  oral_hygiene: string;
  lip_competency: string;
  face_form: string;
  habit: string;
  treated_arch: string;
  molar_class_left: string;
  molar_class_right: string;
  tongue_size: string;
  bracket_system: string;
  midline_upper: string;
  midline_lower: string;
  slot: string;
  extraction_upper: string;
  extraction_lower: string;
  anchorage_upper: string;
  treatment_plan: string;
  created: string;
  updated: string;
  user: number;
  client: number;
}

export interface Appointment {
  id: number;
  client: number;
  description: string;
  date: string;
  date_to: string;
  start: string;
  end: string;
  startDate: string;
  endDate: string;
  treatment?: Treatment[];
  prescription?: Prescription[];
}

export interface Treatment {
  id: number;
  appointment: number;
  note: string;
  created: string;
}

export interface Prescription {
  id: number;
  appointment: number;
  medication: number;
  created: string;
  medications?: Medications[];
}

export interface Medications {
  id: number;
  medicine_name: string;
  dosage: string;
  duration: number;
  created: string;
  updated: string;
  user: number;
}
