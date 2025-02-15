G. Hayes 2023

These are the scripts I used for the steady-state cerebrovascular reactivity (CVR) analysis in:

S. Sparks, G. Hayes, J. Pinto, and D. Bulte, “Characterising cerebrovascular reactivity and the pupillary light response–a comparative study,” Front. Physiol., vol. 15, Aug. 2024, doi: 10.3389/fphys.2024.1384113.

The data consisted of 2 MHz pulsed transcranial Doppler ultrasound blood flow velocity, acquired in the middle cerebral artery.
The CO2 data was acquired using a thin nasal cannula placed into both nostrils and an infrared gas analyser.
These signals were acquired during a protocol of 3 mins of breathing of air, 3 mins of breathing a 5% CO2 air gas mixture, and 2 mins of breathing air again.

Feel free to download and alter this code to suit your own analysis and reference/acknowledge the publication above if you do so.

Adjust parameters as needed for your data. Notably, pay attention to your file paths, sampling rate, the peak promience for peak identification, and the barometric pressue in your location.

It should be noted that our input powerlabs (PWL) data had the following channels: channel 1 of the pwl data is the CO2, channel 2 is the O2 data, channel 3 is the raw TCD data, channel 4 is the PPG data, and channel 5 is the comment data.
