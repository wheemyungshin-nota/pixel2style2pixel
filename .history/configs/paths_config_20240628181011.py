dataset_paths = {
	'celeba_train': '',
	'celeba_test': '',
	'celeba_train_sketch': '',
	'celeba_test_sketch': '',
	'celeba_train_segmentation': '',
	'celeba_test_segmentation': '',
	'ffhq': '',

	'zigbang_beta_400600_rgb': '../../data/zigbang_halffinal_crops/beta/400_600/rgb',
	'zigbang_beta_all_ir': '../../data/zigbang_crop_faces/beta/all/ir',
	'zigbang_beta_400_rgb': '../../data/zigbang_crop_faces/beta/400mm/rgb',
	'zigbang_beta_400_ir': '../../data/zigbang_crop_faces/beta/400mm/ir',
	'zigbang_beta_500_rgb': '../../data/zigbang_crop_faces/beta/500mm/rgb',
	'zigbang_beta_500_ir': '../../data/zigbang_crop_faces/beta/500mm/ir',
	'zigbang_beta_600_rgb': '../../data/zigbang_crop_faces/beta/600mm/rgb',
	'zigbang_beta_600_ir': '../../data/zigbang_crop_faces/beta/600mm/ir',

	'zigbang_alpha_all_rgb': '../../data/zigbang_crop_faces/alpha/all/rgb',
	'zigbang_alpha_all_ir': '../../data/zigbang_crop_faces/alpha/all/ir',
	'zigbang_alpha_300_rgb': '../../data/zigbang_crop_faces/alpha/300mm/rgb',
	'zigbang_alpha_300_ir': '../../data/zigbang_crop_faces/alpha/300mm/ir',
	'zigbang_alpha_500_rgb': '../../data/zigbang_crop_faces/alpha/500mm/rgb',
	'zigbang_alpha_500_ir': '../../data/zigbang_crop_faces/alpha/500mm/ir',
	'zigbang_alpha_700_rgb': '../../data/zigbang_crop_faces/alpha/700mm/rgb',
	'zigbang_alpha_700_ir': '../../data/zigbang_crop_faces/alpha/700mm/ir',
	'zigbang_alpha_900_rgb': '../../data/zigbang_crop_faces/alpha/900mm/rgb',
	'zigbang_alpha_900_ir': '../../data/zigbang_crop_faces/alpha/900mm/ir',
	'zigbang_alpha_zigzag_rgb': '../../data/zigbang_crop_faces/alpha/zigzag/rgb',
	'zigbang_alpha_zigzag_ir': '../../data/zigbang_crop_faces/alpha/zigzag/ir',
}

model_paths = {
	'stylegan_ffhq': 'pretrained_models/stylegan2-ffhq-config-f.pt',
	'ir_se50': 'pretrained_models/model_ir_se50.pth',
	'circular_face': 'pretrained_models/CurricularFace_Backbone.pth',
	'mtcnn_pnet': 'pretrained_models/mtcnn/pnet.npy',
	'mtcnn_rnet': 'pretrained_models/mtcnn/rnet.npy',
	'mtcnn_onet': 'pretrained_models/mtcnn/onet.npy',
	'shape_predictor': 'shape_predictor_68_face_landmarks.dat',
	'moco': 'pretrained_models/moco_v2_800ep_pretrain.pth.tar',
	
	'mygan_alpha': '../stylegan2-pytorch/checkpoint/010000.pt',
}
