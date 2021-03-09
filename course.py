import datetime

list_courses = [('SCSS4213', 'OPERATING SYSTEM', '1', 'SYED HAMID HUSSAIN MADNI', '20/2/2021', '10:00AM'), ('SECP1103', 'PROGRAMMING TECHNIQUES C', '1', 'NUR EILIYAH @ WONG YEE LENG', '20/2/2021', '10:00AM'), ('SECP1103', 'PROGRAMMING TECHNIQUES C', '2', 'TAGWA AHMED MOHAMMED AL-HAJ', '20/2/2021', '10:00AM'), ('SECP1103', 'PROGRAMMING TECHNIQUES C', '3', 'SURIATI BINTI SADIMON', '20/2/2021', '10:00AM'), ('SECP1103', 'PROGRAMMING TECHNIQUES C', '4', 'SYED OTHMAWI B ABD RAHMAN', '20/2/2021', '10:00AM'), ('SECP1103', 'PROGRAMMING TECHNIQUES C', '5', 'SYED OTHMAWI B ABD RAHMAN', '20/2/2021', '10:00AM'), ('SECP1103', 'PROGRAMMING TECHNIQUES C', '6', 'SYED OTHMAWI B ABD RAHMAN', '20/2/2021', '10:00AM'), ('SECP1103', 'PROGRAMMING TECHNIQUES C', '7', 'TAGWA AHMED MOHAMMED AL-HAJ', '20/2/2021', '10:00AM'), ('SEEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '1', 'DALILA BINTI MAT SAID', '10/2/2021', '9:00AM'), ('SEEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '10', 'SHAIKH NASIR @ NASIR BIN SHAIKH HUSIN', '10/2/2021', '9:00AM'), ('SEEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '11', 'MOHAMED SULTAN BIN MOHAMED ALI', '10/2/2021', '9:00AM'), ('SEEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '12', 'MOHAMED SULTAN BIN MOHAMED ALI', '10/2/2021', '9:00AM'), ('SEEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '13', 'MOHD ARIFFANAN BIN MOHD BASRI', '10/2/2021', '9:00AM'), ('SEEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '14', 'JIBRIN MUAZU MUSA', '10/2/2021', '9:00AM'), ('SEEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '2', 'MOKHTAR HARUN', '10/2/2021', '9:00AM'), ('SEEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '3', 'MOHD RODHI BIN SAHID', '10/2/2021', '9:00AM'), ('SEEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '4', 'MOHD RODHI BIN SAHID', '10/2/2021', '9:00AM'), ('SEEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '5', 'MOHAMED AFENDI BIN MOHAMED PIAH', '10/2/2021', '9:00AM'), ('SEEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '6', 'MITRA BINTI MOHD ADDI', '10/2/2021', '9:00AM'), ('SEEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '7', 'MITRA BINTI MOHD ADDI', '10/2/2021', '9:00AM'), ('SEEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '8', 'NORJULIA BINTI MOHAMAD NORDIN', '10/2/2021', '9:00AM'), ('SEEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '9', 'ASRUL IZAM BIN AZMI', '10/2/2021', '9:00AM'), ('SEEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '1', 'USMAN ULLAH SHEIKH BIN IZZAT ULLAH SHEIK', '16/2/2021', '2:30PM'), ('SEEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '10', 'MOHD SAIFUL AZIMI BIN MAHMUD', '16/2/2021', '2:30PM'), ('SEEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '11', 'MOHD ADIB SARIJARI', '16/2/2021', '2:30PM'), ('SEEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '12', 'MOHD ADIB SARIJARI', '16/2/2021', '2:30PM'), ('SEEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '2', 'USMAN ULLAH SHEIKH BIN IZZAT ULLAH SHEIK', '16/2/2021', '2:30PM'), ('SEEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '3', 'AMIRJAN BIN NAWABJAN', '16/2/2021', '2:30PM'), ('SEEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '4', 'AMIRJAN BIN NAWABJAN', '16/2/2021', '2:30PM'), ('SEEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '5', 'MUHAMMAD YUSOF BIN MOHD NOOR', '16/2/2021', '2:30PM'), ('SEEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '6', 'MUHAMMAD YUSOF BIN MOHD NOOR', '16/2/2021', '2:30PM'), ('SEEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '7', 'NURZAL EFFIYANA BINTI GHAZALI', '16/2/2021', '2:30PM'), ('SEEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '8', 'NURZAL EFFIYANA BINTI GHAZALI', '16/2/2021', '2:30PM'), ('SEEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '9', 'MOHD SAIFUL AZIMI BIN MAHMUD', '16/2/2021', '2:30PM'), ('SEEE1073', 'ELECTRONIC DEVICES AND CIRCUITS', '1', 'SUHANA BINTI MOHAMED SULTAN/ SHAHARIN FADZLI BIN ABD RAHMAN', '25/2/2021', '9:00AM'), ('SEEE1073', 'ELECTRONIC DEVICES AND CIRCUITS', '2', 'SHAHARIN FADZLI BIN ABD RAHMAN', '25/2/2021', '9:00AM'), ('SEEE1223', 'DIGITAL ELECTRONICS', '1', 'NORHAFIZAH BT RAMLI', '22/2/2021', '9:00AM'), ('SEEE1223', 'DIGITAL ELECTRONICS', '2', 'SUHAILA BINTI ISAAK', '22/2/2021', '9:00AM'), ('SEEE2073', 'SIGNALS AND SYSTEMS', '1', 'ARNIDZA BINTI RAMLI', '21/2/2021', '9:00AM'), ('SEEE2073', 'SIGNALS AND SYSTEMS', '10', "NURUL MU'AZZAH BINTI ABDUL LATIFF", '21/2/2021', '9:00AM'), ('SEEE2073', 'SIGNALS AND SYSTEMS', '11', 'NIK NOORDINI BT NIK ABD MALIK', '21/2/2021', '9:00AM'), ('SEEE2073', 'SIGNALS AND SYSTEMS', '12', 'NOORASMAWATI BINTI SAMSURI', '21/2/2021', '9:00AM'), ('SEEE2073', 'SIGNALS AND SYSTEMS', '13', 'MOHD HANIFF BIN IBRAHIM', '21/2/2021', '9:00AM'), ('SEEE2073', 'SIGNALS AND SYSTEMS', '14', 'SITI ZALEHA BT. ABDUL HAMID', '21/2/2021', '9:00AM'), ('SEEE2073', 'SIGNALS AND SYSTEMS', '2', 'AHMAD SHARMI BIN ABDULLAH', '21/2/2021', '9:00AM'), ('SEEE2073', 'SIGNALS AND SYSTEMS', '3', 'SITI ZALEHA BT. ABDUL HAMID', '21/2/2021', '9:00AM'), ('SEEE2073', 'SIGNALS AND SYSTEMS', '4', 'MOHAMAD RIJAL BIN HAMID', '21/2/2021', '9:00AM'), ('SEEE2073', 'SIGNALS AND SYSTEMS', '5', 'NIK NOORDINI BT NIK ABD MALIK', '21/2/2021', '9:00AM'), ('SEEE2073', 'SIGNALS AND SYSTEMS', '6', 'ARNIDZA BINTI RAMLI', '21/2/2021', '9:00AM'), ('SEEE2073', 'SIGNALS AND SYSTEMS', '7', 'NORHUDAH BINTI SEMAN', '21/2/2021', '9:00AM'), ('SEEE2073', 'SIGNALS AND SYSTEMS', '8', 'AHMAD SHARMI BIN ABDULLAH', '21/2/2021', '9:00AM'), ('SEEE2073', 'SIGNALS AND SYSTEMS', '9', 'MOHD FAIRUS BIN MOHD YUSOFF', '21/2/2021', '9:00AM'), ('SEEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '1', 'ANITA BINTI AHMAD', '10/2/2021', '2:30PM'), ('SEEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '10', 'MOHAMAD SHUKRI BIN ABDUL MANAF', '10/2/2021', '2:30PM'), ('SEEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '2', 'ANITA BINTI AHMAD', '10/2/2021', '2:30PM'), ('SEEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '3', 'HERLINA BINTI ABDUL RAHIM', '10/2/2021', '2:30PM'), ('SEEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '4', 'SALLEHUDDIN BIN IBRAHIM', '10/2/2021', '2:30PM'), ('SEEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '5', 'LEOW PEI LING', '10/2/2021', '2:30PM'), ('SEEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '6', 'LEOW PEI LING', '10/2/2021', '2:30PM'), ('SEEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '7', 'MOHD AMRI BIN MD. YUNUS', '10/2/2021', '2:30PM'), ('SEEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '8', 'MOHD AMRI BIN MD. YUNUS', '10/2/2021', '2:30PM'), ('SEEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '9', 'MOHAMAD SHUKRI BIN ABDUL MANAF', '10/2/2021', '2:30PM'), ('SEEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '1', 'MOHD HAFIZ BIN HABIBUDDIN', '18/2/2021', '9:00AM'), ('SEEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '10', 'MADIHAH BINTI MD RASID', '18/2/2021', '9:00AM'), ('SEEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '11', 'RASYIDAH BINTI MOHAMAD IDRIS', '18/2/2021', '9:00AM'), ('SEEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '12', 'RASYIDAH BINTI MOHAMAD IDRIS', '18/2/2021', '9:00AM'), ('SEEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '13', 'MD PAUZI BIN ABDULLAH', '18/2/2021', '9:00AM'), ('SEEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '14', 'MD PAUZI BIN ABDULLAH', '18/2/2021', '9:00AM'), ('SEEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '2', 'MOHD HAFIZ BIN HABIBUDDIN', '18/2/2021', '9:00AM'), ('SEEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '3', 'MOHD ZAKI BIN DAUD', '18/2/2021', '9:00AM'), ('SEEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '4', 'MOHD ZAKI BIN DAUD', '18/2/2021', '9:00AM'), ('SEEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '5', 'MOHD JUNAIDI BIN ABDUL AZIZ', '18/2/2021', '9:00AM'), ('SEEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '6', 'MOHD JUNAIDI BIN ABDUL AZIZ', '18/2/2021', '9:00AM'), ('SEEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '7', 'SHAHRIN BIN MD AYOB', '18/2/2021', '9:00AM'), ('SEEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '8', 'SHAHRIN BIN MD AYOB', '18/2/2021', '9:00AM'), ('SEEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '9', 'MADIHAH BINTI MD RASID', '18/2/2021', '9:00AM'), ('SEEE3223', 'MICROPROCESSOR', '11', 'SHAHIDATUL SADIAH BINTI ABDUL MANAN', '20/2/2021', '9:00AM'), ('SEEE3223', 'MICROPROCESSOR', '12', 'SHAHIDATUL SADIAH BINTI ABDUL MANAN', '20/2/2021', '9:00AM'), ('SEEE3223', 'MICROPROCESSOR', '2', 'ISMAIL BIN ARIFFIN', '20/2/2021', '9:00AM'), ('SEEU1002', 'ELECTRICAL TECHNOLOGY', '1', 'ZURAIMY BIN ADZIS', '19/2/2021', '9:00AM'), ('SEEU1002', 'ELECTRICAL TECHNOLOGY', '2', 'ZURAIMY BIN ADZIS', '19/2/2021', '9:00AM'), ('SEEU1002', 'ELECTRICAL TECHNOLOGY', '3', 'SAMURA BIN ALI', '19/2/2021', '9:00AM'), ('SEEU1002', 'ELECTRICAL TECHNOLOGY', '4', 'SAMURA BIN ALI', '19/2/2021', '9:00AM'), ('SEEU1003', 'BASIC ELECTRICAL ENGINEERING', '1', 'YUSRI B MD. YUNOS', '21/2/2021', '9:00AM'), ('SEEU1023', 'CIRCUIT THEORY', '1', 'ZULKARNAIN BIN AHMAD NOORDEN', '10/2/2021', '9:00AM'), ('SEEU1023', 'CIRCUIT THEORY', '2', 'NOOR AZLINDA BINTI AHMAD', '10/2/2021', '9:00AM'), ('SEEU1063', 'ELECTRONIC DEVICES', '1', 'AZLI BIN YAHYA', '18/2/2021', '9:00AM'), ('SEEU1063', 'ELECTRONIC DEVICES', '2', 'NASRUL HUMAIMI BIN MAHMOOD', '18/2/2021', '9:00AM'), ('SEEU1063', 'ELECTRONIC DEVICES', '3', 'MUHAMMAD ARIF BIN ABDUL RAHIM', '18/2/2021', '9:00AM'), ('SEEU2003', 'ELECTRICAL TECHNOLOGY', '1', 'RAZMAN BIN AYOP', '23/2/2021', '9:00AM'), ('SEEU2003', 'ELECTRICAL TECHNOLOGY', '2', 'RAZMAN BIN AYOP', '23/2/2021', '9:00AM'), ('SEEU2003', 'ELECTRICAL TECHNOLOGY', '3', 'MOHD ZAKI BIN DAUD', '23/2/2021', '9:00AM'), ('SEEU2073', 'SIGNALS AND SYSTEMS', '1', 'AHMAD SHAHIDAN BIN ABDULLAH', '21/2/2021', '9:00AM'), ('SEEU2073', 'SIGNALS AND SYSTEMS', '2', 'MALARVILI A/P BALA KRISHNAN', '21/2/2021', '9:00AM'), ('SEEU2073', 'SIGNALS AND SYSTEMS', '3', 'AHMAD SHAHIDAN BIN ABDULLAH', '21/2/2021', '9:00AM'), ('SKEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '1', 'DALILA BINTI MAT SAID', '10/2/2021', '9:00AM'), ('SKEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '12', 'MOHAMED SULTAN BIN MOHAMED ALI', '10/2/2021', '9:00AM'), ('SKEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '4', 'MOHD RODHI BIN SAHID', '10/2/2021', '9:00AM'), ('SKEE1013', 'ELECTRICAL CIRCUIT ANALYSIS', '7', 'MITRA BINTI MOHD ADDI', '10/2/2021', '9:00AM'), ('SKEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '1', 'USMAN ULLAH SHEIKH BIN IZZAT ULLAH SHEIK', '16/2/2021', '2:30PM'), ('SKEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '10', 'MOHD SAIFUL AZIMI BIN MAHMUD', '16/2/2021', '2:30PM'), ('SKEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '2', 'USMAN ULLAH SHEIKH BIN IZZAT ULLAH SHEIK', '16/2/2021', '2:30PM'), ('SKEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '3', 'AMIRJAN BIN NAWABJAN', '16/2/2021', '2:30PM'), ('SKEE1022', 'INTRODUCTION TO SCIENTIFIC PROGRAMMING', '9', 'MOHD SAIFUL AZIMI BIN MAHMUD', '16/2/2021', '2:30PM'), ('SKEE1073', 'ELECTRONIC DEVICES AND CIRCUIT', '1', 'SUHANA BINTI MOHAMED SULTAN', '25/2/2021', '9:00AM'), ('SKEE1073', 'ELECTRONIC DEVICES AND CIRCUIT', '2', 'SHAHARIN FADZLI BIN ABD RAHMAN', '25/2/2021', '9:00AM'), ('SKEE2073', 'SIGNALS AND SYSTEMS', '1', 'ARNIDZA BINTI RAMLI', '21/2/2021', '9:00AM'), ('SKEE2073', 'SIGNALS AND SYSTEMS', '11', 'NIK NOORDINI BT NIK ABD MALIK', '21/2/2021', '9:00AM'), ('SKEE2073', 'SIGNALS AND SYSTEMS', '13', 'MOHD HANIFF BIN IBRAHIM', '21/2/2021', '9:00AM'), ('SKEE2073', 'SIGNALS AND SYSTEMS', '2', 'AHMAD SHARMI BIN ABDULLAH', '21/2/2021', '9:00AM'), ('SKEE2073', 'SIGNALS AND SYSTEMS', '4', 'MOHAMAD RIJAL BIN HAMID', '21/2/2021', '9:00AM'), ('SKEE2073', 'SIGNALS AND SYSTEMS', '5', 'NIK NOORDINI BT NIK ABD MALIK', '21/2/2021', '9:00AM'), ('SKEE2073', 'SIGNALS AND SYSTEMS', '7', 'NORHUDAH BINTI SEMAN', '21/2/2021', '9:00AM'), ('SKEE2073', 'SIGNALS AND SYSTEMS', '8', 'AHMAD SHARMI BIN ABDULLAH', '21/2/2021', '9:00AM'), ('SKEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '1', 'ANITA BINTI AHMAD', '10/2/2021', '2:30PM'), ('SKEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '4', 'SALLEHUDDIN BIN IBRAHIM', '10/2/2021', '2:30PM'), ('SKEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '5', 'LEOW PEI LING', '10/2/2021', '2:30PM'), ('SKEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '6', 'LEOW PEI LING', '10/2/2021', '2:30PM'), ('SKEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '7', 'MOHD AMRI BIN MD. YUNUS', '10/2/2021', '2:30PM'), ('SKEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '8', 'MOHD AMRI BIN MD. YUNUS', '10/2/2021', '2:30PM'), ('SKEE2133', 'ELECTRONIC INSTRUMENTATION & MEASUREM', '9', 'MOHAMAD SHUKRI BIN ABDUL MANAF', '10/2/2021', '2:30PM'), ('SKEE2413', 'BASIC POWER & ELECTRIC MACHINE', '1', 'MOHD ZAKI BIN DAUD', '10/2/2021', '9:00AM'), ('SKEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '1', 'MD PAUZI BIN ABDULLAH', '18/2/2021', '9:00AM'), ('SKEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '13', 'MD PAUZI BIN ABDULLAH', '18/2/2021', '9:00AM'), ('SKEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '2', 'MOHD HAFIZ BIN HABIBUDDIN', '18/2/2021', '9:00AM'), ('SKEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '3', 'MOHD ZAKI BIN DAUD', '18/2/2021', '9:00AM'), ('SKEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '4', 'MOHD ZAKI BIN DAUD', '18/2/2021', '9:00AM'), ('SKEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '5', 'MOHD JUNAIDI BIN ABDUL AZIZ', '18/2/2021', '9:00AM'), ('SKEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '7', 'SHAHRIN BIN MD AYOB', '18/2/2021', '9:00AM'), ('SKEE2423', 'FUNDAMENTALS OF ELECTRICAL POWER SYSTE', '8', 'SHAHRIN BIN MD AYOB', '18/2/2021', '9:00AM'), ('SKEE2523', 'ELECTROMAGNETIC FIELD THEORY', '1', 'MOHD RASHIDI BIN SALIM', '24/2/2021', '9:00AM'), ('SKEE2523', 'ELECTROMAGNETIC FIELD THEORY', '2', 'OMAR BIN ABDUL AZIZ', '24/2/2021', '9:00AM'), ('SKEE2523', 'ELECTROMAGNETIC FIELD THEORY', '3', 'MOHD RASHIDI BIN SALIM', '24/2/2021', '9:00AM'), ('SKEE2523', 'ELECTROMAGNETIC FIELD THEORY', '4', 'NORAZAN BIN MOHD KASSIM', '24/2/2021', '9:00AM'), ('SKEE2523', 'ELECTROMAGNETIC FIELD THEORY', '5', 'NORAZAN BIN MOHD KASSIM', '24/2/2021', '9:00AM'), ('SKEE3133', 'SYSTEM MODELING & ANALYSIS', '1', 'NASARUDIN BIN AHMAD', '7/2/2021', '2:30PM'), ('SKEE3133', 'SYSTEM MODELING & ANALYSIS', '10', 'SHAHDAN BIN SUDIN/ FAZILAH BINTI HASSAN', '7/2/2021', '2:30PM'), ('SKEE3133', 'SYSTEM MODELING & ANALYSIS', '11', 'ZAHARUDDIN B MOHAMED', '7/2/2021', '2:30PM'), ('SKEE3133', 'SYSTEM MODELING & ANALYSIS', '12', 'ZAHARUDDIN B MOHAMED', '7/2/2021', '2:30PM'), ('SKEE3133', 'SYSTEM MODELING & ANALYSIS', '13', 'NORHALIZA BT.HJ.ABD. WAHAB', '7/2/2021', '2:30PM'), ('SKEE3133', 'SYSTEM MODELING & ANALYSIS', '14', 'HERMAN BIN WAHID', '7/2/2021', '2:30PM'), ('SKEE3133', 'SYSTEM MODELING & ANALYSIS', '15', 'HERMAN BIN WAHID', '7/2/2021', '2:30PM'), ('SKEE3133', 'SYSTEM MODELING & ANALYSIS', '2', 'NASARUDIN BIN AHMAD', '7/2/2021', '2:30PM'), ('SKEE3133', 'SYSTEM MODELING & ANALYSIS', '3', 'FATIMAH SHAM BT. ISMAIL/ NORHALIZA BT.HJ.ABD. WAHAB', '7/2/2021', '2:30PM'), ('SKEE3133', 'SYSTEM MODELING & ANALYSIS', '4', 'FATIMAH SHAM BT. ISMAIL/ NORHALIZA BT.HJ.ABD. WAHAB', '7/2/2021', '2:30PM'), ('SKEE3133', 'SYSTEM MODELING & ANALYSIS', '5', 'SALINDA BINTI BUYAMIN', '7/2/2021', '2:30PM'), ('SKEE3133', 'SYSTEM MODELING & ANALYSIS', '6', 'SALINDA BINTI BUYAMIN', '7/2/2021', '2:30PM'), ('SKEE3133', 'SYSTEM MODELING & ANALYSIS', '7', 'SHAHDAN BIN SUDIN', '7/2/2021', '2:30PM'), ('SKEE3133', 'SYSTEM MODELING & ANALYSIS', '8', 'SHAHDAN BIN SUDIN', '7/2/2021', '2:30PM'), ('SKEE3133', 'SYSTEM MODELING & ANALYSIS', '9', 'FAZILAH BINTI HASSAN/ SHAHDAN BIN SUDIN', '7/2/2021', '2:30PM'), ('SKEE3143', 'CONTROL SYSTEM DESIGN', '1', "MOHD FUA'AD BIN RAHMAT", '10/2/2021', '9:00AM'), ('SKEE3223', 'MICROPROCESSOR', '1', 'ISMAIL BIN ARIFFIN', '20/2/2021', '9:00AM'), ('SKEE3223', 'MICROPROCESSOR', '10', 'ZULFAKAR BIN ASPAR', '20/2/2021', '9:00AM'), ('SKEE3223', 'MICROPROCESSOR', '11', 'SHAHIDATUL SADIAH BINTI ABDUL MANAN', '20/2/2021', '9:00AM'), ('SKEE3223', 'MICROPROCESSOR', '12', 'SHAHIDATUL SADIAH BINTI ABDUL MANAN', '20/2/2021', '9:00AM'), ('SKEE3223', 'MICROPROCESSOR', '13', 'MUHAMMAD AFIQ NURUDIN BIN HAMZAH', '20/2/2021', '9:00AM'), ('SKEE3223', 'MICROPROCESSOR', '2', 'ISMAIL BIN ARIFFIN', '20/2/2021', '9:00AM'), ('SKEE3223', 'MICROPROCESSOR', '3', 'MOHD SHAHRIZAL BIN RUSLI', '20/2/2021', '9:00AM'), ('SKEE3223', 'MICROPROCESSOR', '4', 'MOHD SHAHRIZAL BIN RUSLI', '20/2/2021', '9:00AM'), ('SKEE3223', 'MICROPROCESSOR', '5', 'MUHAMMAD AFIQ NURUDIN BIN HAMZAH/ MUHAMMAD NASIR BIN IBRAHI', '20/2/2021', '9:00AM'), ('SKEE3223', 'MICROPROCESSOR', '6', 'MUHAMMAD AFIQ NURUDIN BIN HAMZAH/ MUHAMMAD NASIR BIN IBRAHI', '20/2/2021', '9:00AM'), ('SKEE3223', 'MICROPROCESSOR', '7', 'MOHD AFZAN BIN OTHMAN', '20/2/2021', '9:00AM'), ('SKEE3223', 'MICROPROCESSOR', '8', 'MOHD AFZAN BIN OTHMAN', '20/2/2021', '9:00AM'), ('SKEE3223', 'MICROPROCESSOR', '9', 'ZULFAKAR BIN ASPAR', '20/2/2021', '9:00AM'), ('SKEE3533', 'COMMUNICATION PRINCIPLES', '1', 'MUHAMMAD AL FARABI BIN MUHAMMAD IQBAL', '22/2/2021', '9:00AM'), ('SKEE3533', 'COMMUNICATION PRINCIPLES', '10', 'JAFRI BIN DIN', '22/2/2021', '9:00AM'), ('SKEE3533', 'COMMUNICATION PRINCIPLES', '11', 'NADIATULHUDA BINTI ZULKIFLI', '22/2/2021', '9:00AM'), ('SKEE3533', 'COMMUNICATION PRINCIPLES', '12', 'NADIATULHUDA BINTI ZULKIFLI', '22/2/2021', '9:00AM'), ('SKEE3533', 'COMMUNICATION PRINCIPLES', '13', 'ROZEHA BT. A. RASHID', '22/2/2021', '9:00AM'), ('SKEE3533', 'COMMUNICATION PRINCIPLES', '14', 'OSMAN BIN AYOP', '22/2/2021', '9:00AM'), ('SKEE3533', 'COMMUNICATION PRINCIPLES', '2', 'MUHAMMAD AL FARABI BIN MUHAMMAD IQBAL', '22/2/2021', '9:00AM'), ('SKEE3533', 'COMMUNICATION PRINCIPLES', '3', 'MOHAMAD KAMAL B. A. RAHIM', '22/2/2021', '9:00AM'), ('SKEE3533', 'COMMUNICATION PRINCIPLES', '4', 'MOHAMAD KAMAL B. A. RAHIM', '22/2/2021', '9:00AM'), ('SKEE3533', 'COMMUNICATION PRINCIPLES', '5', 'RASHIDAH@SITI  SAEDAH BINTI ARSAT', '22/2/2021', '9:00AM'), ('SKEE3533', 'COMMUNICATION PRINCIPLES', '6', 'RASHIDAH@SITI  SAEDAH BINTI ARSAT', '22/2/2021', '9:00AM'), ('SKEE3533', 'COMMUNICATION PRINCIPLES', '7', 'CHUA TIEN HAN', '22/2/2021', '9:00AM'), ('SKEE3533', 'COMMUNICATION PRINCIPLES', '8', 'CHUA TIEN HAN', '22/2/2021', '9:00AM'), ('SKEE3533', 'COMMUNICATION PRINCIPLES', '9', 'JAFRI BIN DIN', '22/2/2021', '9:00AM'), ('SKEE4012', 'PROFESSIONAL ENGINEERING PRACTICE', '1', 'MOHD RIDZUAN BIN AHMAD', '24/2/2021', '2:30PM'), ('SKEE4173', 'INDUSTRIAL PROCESS CONTROL', '1', 'SHAFISHUHAZA SAHLAN', '20/2/2021', '9:00AM'), ('SKEE4433', 'POWER ELECTRONICS & DRIVES', '1', 'SHAHRIN BIN MD AYOB', '22/2/2021', '9:00AM'), ('SKEE4443', 'POWER SYSTEM ANALYSIS', '1', 'AHMAD SAFAWI BIN MOKHTAR', '18/2/2021', '9:00AM'), ('SKEE4443', 'POWER SYSTEM ANALYSIS', '2', 'AHMAD SAFAWI BIN MOKHTAR', '18/2/2021', '9:00AM'), ('SKEE4443', 'POWER SYSTEM ANALYSIS', '3', 'SAIFULNIZAM BIN ABD. KHALID', '18/2/2021', '9:00AM'), ('SKEE4443', 'POWER SYSTEM ANALYSIS', '4', 'SAIFULNIZAM BIN ABD. KHALID', '18/2/2021', '9:00AM'), ('SKEE4443', 'POWER SYSTEM ANALYSIS', '5', 'MOHD FADLI BIN RAHMAT', '18/2/2021', '9:00AM'), ('SKEE4453', 'POWER SYSTEM CONTROL', '1', 'SYED NORAZIZUL BIN SYED NASIR', '21/2/2021', '9:00AM'), ('SKEE4453', 'POWER SYSTEM CONTROL', '2', 'SYED NORAZIZUL BIN SYED NASIR', '21/2/2021', '9:00AM'), ('SKEE4633', 'ELECTRICAL MACHINES', '1', 'AWANG BIN JUSOH', '23/2/2021', '9:00AM'), ('SKEE4633', 'ELECTRICAL MACHINES', '2', 'AWANG BIN JUSOH', '23/2/2021', '9:00AM'), ('SKEE4633', 'ELECTRICAL MACHINES', '3', 'NIK DIN B. MUHAMAD', '23/2/2021', '9:00AM'), ('SKEE4633', 'ELECTRICAL MACHINES', '4', 'NIK DIN B. MUHAMAD', '23/2/2021', '9:00AM'), ('SKEE4633', 'ELECTRICAL MACHINES', '5', 'NIK RUMZI BIN NIK IDRIS', '23/2/2021', '9:00AM'), ('SKEE4653', 'PHOTOVOLTAIC AND WIND ENERGY SYSTEM', '1', 'TAN CHEE WEI', '17/2/2021', '9:00AM'), ('SKEE4653', 'PHOTOVOLTAIC AND WIND ENERGY SYSTEM', '2', 'TAN CHEE WEI', '17/2/2021', '9:00AM'), ('SKEE4663', 'ELECTRICITY FOR SUSTAINABLE ENERGY', '1', 'NORZANAH BINTI ROSMIN', '9/2/2021', '2:30PM'), ('SKEE4663', 'ELECTRICITY FOR SUSTAINABLE ENERGY', '2', 'NORZANAH BINTI ROSMIN', '9/2/2021', '2:30PM'), ('SKEI3133', 'INDUSTRIAL INSTRUMENTATIONS AND APPLICA', '1', 'SALLEHUDDIN BIN IBRAHIM', '21/2/2021', '9:00AM'), ('SKEI4313', 'PLC AND SCADA SYSTEM DESIGN', '1', 'SOPHAN WAHYUDI BIN NAWAWI', '10/2/2021', '9:00AM'), ('SKEI4313', 'PLC AND SCADA SYSTEM DESIGN', '2', 'SOPHAN WAHYUDI BIN NAWAWI', '10/2/2021', '9:00AM'), ('SKEL4213', 'SOFTWARE ENGINEERING', '1', "MUHAMMAD MUN'IM BIN AHMAD ZABIDI", '25/2/2021', '9:00AM'), ('SKEL4223', 'DIGITAL SIGNAL PROCESSING I', '1', 'MUSA BIN MOHD MOKJI', '19/2/2021', '9:00AM'), ('SKEL4223', 'DIGITAL SIGNAL PROCESSING I', '2', 'ZAID BIN OMAR', '19/2/2021', '9:00AM'), ('SKEL4223', 'DIGITAL SIGNAL PROCESSING I', '3', 'KHAIRUL HAMIMAH BINTI ABAS', '19/2/2021', '9:00AM'), ('SKEL4283', 'ANALOG CMOS IC DESIGN', '1', 'YUSMEERAZ BINTI YUSOF', '17/2/2021', '9:00AM'), ('SKEL4343', 'INFORMATION SECURITY', '1', 'AHMAD ZURI B SHA AMERI', '23/2/2021', '9:00AM'), ('SKEL4363', 'DIGITAL IMAGE PROCESSING', '1', 'SYED ABDUL RAHMAN BIN SYED ABU BAKAR', '23/2/2021', '9:00AM'), ('SKEL4373', 'IC TESTING TECHNIQUES', '1', 'IZAM BIN KAMISIAN', '10/2/2021', '2:30PM'), ('SKEL4373', 'IC TESTING TECHNIQUES', '2', 'IZAM BIN KAMISIAN', '10/2/2021', '2:30PM'), ('SKEL4533', 'BIOMEDICAL SIGNAL PROCESSING', '1', 'NORLAILI BINTI MAT SAFRI', '23/2/2021', '9:00AM'), ('SKEL4543', 'BIOSYSTEM MODELLING', '1', 'NURUL ASHIKIN BINTI ABDUL KADIR/ NOR AINI BINTI ZAKARIA', '18/2/2021', '9:00AM'), ('SKEL4563', 'BIOSENSORS & TRANSDUCERS', '1', 'MOHD AZHAR BIN ABDUL RAZAK', '21/2/2021', '9:00AM'), ('SKEL4613', 'SEMICONDUCTOR DEVICE ENGINEERING', '1', 'NURUL EZAILA BINTI ALIAS', '21/2/2021', '9:00AM'), ('SKEL4653', 'MODELLING & SIMULATION OF MICROELECTRO', '1', 'MICHAEL TAN LOONG PENG', '23/2/2021', '9:00AM'), ('SKEM3123', 'HYDRAULIC AND PNEUMATIC SYSTEMS', '1', 'MOHAMAD SHUKRI BIN ABDUL MANAF', '22/2/2021', '9:00AM'), ('SKEM4133', 'MACHINE VISION SYSTEMS', '1', 'AHMAD RIDHWAN BIN WAHAP', '21/2/2021', '2:30PM'), ('SKEM4143', 'ROBOTICS', '1', 'KUMERESEN A/L A.DANAPALASINGAM', '7/2/2021', '9:00AM'), ('SKEM4143', 'ROBOTICS', '2', 'KUMERESEN A/L A.DANAPALASINGAM', '7/2/2021', '9:00AM'), ('SKEM4143', 'ROBOTICS', '3', 'KUMERESEN A/L A.DANAPALASINGAM', '7/2/2021', '9:00AM'), ('SKEM4173', 'ARTIFICIAL INTELLIGENCE', '1', 'MOHAMAD HAFIS IZRAN BIN ISHAK', '17/2/2021', '2:30PM'), ('SKEM4173', 'ARTIFICIAL INTELLIGENCE', '2', 'MOHAMAD HAFIS IZRAN BIN ISHAK', '17/2/2021', '2:30PM'), ('SKEM4223', 'EMBEDDED SYSTEMS', '1', 'YEONG CHE FAI', '16/2/2021', '2:30PM'), ('SKEM4333', 'MECHATRONICS SYSTEM DESIGN', '1', 'LIM CHENG SIONG', '24/2/2021', '9:00AM'), ('SKET3573', 'MICROWAVE ENGINEERING', '1', 'NOOR ASNIZA BINTI MURAD', '16/2/2021', '9:00AM'), ('SKET3583', 'DIGITAL COMMUNICATION SYSTEM', '1', 'SHARIFAH KAMILAH BT SYED YUSOF', '18/2/2021', '9:00AM'), ('SKET3623', 'DATA COMMUNICATION & NETWORKS', '1', 'MUHAMMAD ARIFF BIN BAHARUDIN', '7/2/2021', '9:00AM'), ('SKET4523', 'OPTICAL COMMUNICATION SYSTEMS', '1', 'MOHD HANIFF BIN IBRAHIM', '10/2/2021', '2:30PM'), ('SKET4543', 'RF MICROWAVE CIRCUIT DESIGN', '1', 'MOHD HAIZAL BIN JAMALUDIN', '20/2/2021', '9:00AM'), ('SKET4623', 'NETWORK PROGRAMMING', '1', 'MUHAMMAD ARIFF BIN BAHARUDIN', '22/2/2021', '9:00AM'), ('SKEU1002', 'ELECTRICAL TECHNOLOGY', '1', 'ZURAIMY BIN ADZIS', '19/2/2021', '9:00AM'), ('SKEU1063', 'ELECTRONIC DEVICES', '1', 'AZLI BIN YAHYA', '10/2/2021', '9:00AM'), ('SKEU1063', 'ELECTRONIC DEVICES', '3', 'MUHAMMAD ARIF BIN ABDUL RAHIM', '10/2/2021', '9:00AM'), ('SKEU1212', 'DIGITAL LOGICS', '1', 'MUHAMMAD ARIF BIN ABDUL RAHIM', '21/2/2021', '9:00AM'), ('SKEU2003', 'ELECTRICAL TECHNOLOGY', '1', 'MOHD HAFIZI BIN AHMAD', '23/2/2021', '9:00AM'), ('SKEU2003', 'ELECTRICAL TECHNOLOGY', '2', 'MOHD HAFIZI BIN AHMAD', '23/2/2021', '9:00AM'), ('SKEU2003', 'ELECTRICAL TECHNOLOGY', '3', 'MOHD JUNAIDI BIN ABDUL AZIZ', '23/2/2021', '9:00AM'), ('SKEU2012', 'ELECTRONICS', '1', 'JOHARI BIN KASIM', '19/2/2021', '9:00AM'), ('SKEU2033', 'CIRCUIT THEORY', '1', 'SITI MAHERAH BINTI HUSSIN', '20/2/2021', '9:00AM'), ('SKEU2073', 'SIGNALS AND SYSTEM', '1', 'AHMAD SHAHIDAN BIN ABDULLAH', '21/2/2021', '9:00AM'), ('SKEU2073', 'SIGNALS AND SYSTEM', '2', 'MALARVILI A/P BALA KRISHNAN', '21/2/2021', '9:00AM'), ('SKEU2073', 'SIGNALS AND SYSTEM', '3', 'AHMAD SHAHIDAN BIN ABDULLAH', '21/2/2021', '9:00AM'), ('SKEU2123', 'MEASUREMENT & INSTRUMENTATION', '1', 'MOHAMAD SHUKRI BIN ABDUL MANAF', '20/2/2021', '9:00AM'), ('SKEU2523', 'ELECTROMAGNETIC FIELD THEORY', '1', 'MOHD RASHIDI BIN SALIM', '24/2/2021', '9:00AM'), ('SKEU2523', 'ELECTROMAGNETIC FIELD THEORY', '2', 'OMAR BIN ABDUL AZIZ/ JAYSUMAN BIN PUSPPANATHAN', '24/2/2021', '9:00AM'), ('SKEU3063', 'ELECTRONIC CIRCUITS AND SYSTEMS', '1', 'CAMALLIL BIN OMAR', '18/2/2021', '9:00AM'), ('SKEU3063', 'ELECTRONIC CIRCUITS AND SYSTEMS', '2', 'ZAHARAH BINTI JOHARI', '18/2/2021', '9:00AM'), ('SKEU3533', 'COMMUNICATION PRINCIPLES', '1', 'YOU KOK YEOW', '22/2/2021', '9:00AM'), ('SKEU3533', 'COMMUNICATION PRINCIPLES', '2', 'AISYAH BINTI AHMAD SHAFI', '22/2/2021', '9:00AM'), ('SSCE1693', 'ENGINEERING MATHEMATICS I', '11', 'AHMAD FADILLAH BIN EMBONG', '7/2/2021', '9:00AM'), ('SSCE1693', 'ENGINEERING MATHEMATICS I', '30', 'ONG CHEE TIONG', '7/2/2021', '9:00AM'), ('SSCE1693', 'ENGINEERING MATHEMATICS I', '31', 'GAMBO IBRAHIM', '7/2/2021', '9:00AM'), ('SSCE1693', 'ENGINEERING MATHEMATICS I', '32', 'SITI MARIAM BINTI NORRULASHIKIN', '7/2/2021', '9:00AM'), ('SSCE1693', 'ENGINEERING MATHEMATICS I', '33', 'NUR ARINA BAZILAH BINTI KAMISAN', '7/2/2021', '9:00AM'), ('SSCE1693', 'ENGINEERING MATHEMATICS I', '34', 'ANJU VIJAYAN NAIR', '7/2/2021', '9:00AM'), ('SSCE1693', 'ENGINEERING MATHEMATICS I', '35', 'NORAIHAN AFIQAH BINTI RAWI', '7/2/2021', '9:00AM'), ('SSCE1793', 'DIFFERENTIAL EQUATIONS', '11', 'HAZZIRAH IZZATI BINTI MAT HASSIM', '17/2/2021', '9:00AM'), ('SSCE1793', 'DIFFERENTIAL EQUATIONS', '30', 'ANATI BTE ALI', '17/2/2021', '9:00AM'), ('SSCE1993', 'ENGINEERING MATHEMATICS II', '30', 'MOHAMMAD FAISAL BIN MOHD BASIR', '8/2/2021', '9:00AM'), ('SSCE1993', 'ENGINEERING MATHEMATICS II', '31', 'ZAITON BINTI MAT ISA', '8/2/2021', '9:00AM'), ('SSCE1993', 'ENGINEERING MATHEMATICS II', '32', 'FARIDAH BTE MUSTAPHA', '8/2/2021', '9:00AM'), ('SSCE1993', 'ENGINEERING MATHEMATICS II', '33', 'FUAADA BT MOHD SIAM', '8/2/2021', '9:00AM'), ('SSCE1993', 'ENGINEERING MATHEMATICS II', '34', 'MOHD ALI KHAMEINI BIN AHMAD', '8/2/2021', '9:00AM'), ('SSCE1993', 'ENGINEERING MATHEMATICS II', '35', 'MOHAMMAD IZAT EMIR BIN ZULKIFLY', '8/2/2021', '9:00AM'), ('SSCE1993', 'ENGINEERING MATHEMATICS II', '36', 'NORAIHAN AFIQAH BINTI RAWI', '8/2/2021', '9:00AM'), ('SSCE1993', 'ENGINEERING MATHEMATICS II', '40', 'FARIDAH BTE MUSTAPHA', '8/2/2021', '9:00AM'), ('SSCE1993', 'ENGINEERING MATHEMATICS II', '61', 'MOHAMMAD IZAT EMIR BIN ZULKIFLY', '8/2/2021', '9:00AM'), ('SSCE2193', 'ENGINEERING STATISTICS', '20', 'NORASLINDA BINTI MOHAMED ISMAIL', '16/2/2021', '9:00AM'), ('SSCE2193', 'ENGINEERING STATISTICS', '21', 'ZARINA BINTI MOHD KHALID', '16/2/2021', '9:00AM'), ('SSCE2193', 'ENGINEERING STATISTICS', '40', 'SITI ROHANI BINTI MOHD NOR', '16/2/2021', '9:00AM'), ('SSCE2193', 'ENGINEERING STATISTICS', '43', 'NORHAIZA BINTI AHMAD', '16/2/2021', '9:00AM'), ('SSCE2393', 'NUMERICAL METHODS', '22', 'HANG SEE PHENG', '9/2/2021', '9:00AM'), ('SSCE2393', 'NUMERICAL METHODS', '30', 'WAN RUKAIDA BINTI WAN ABDULLAH', '9/2/2021', '9:00AM'), ('SSCE2393', 'NUMERICAL METHODS', '31', 'MUHAMAD NAJIB BIN ZAKARIA', '9/2/2021', '9:00AM'), ('SSCE2393', 'NUMERICAL METHODS', '32', 'SHAZIRAWATIBINTI MOHD PUZI', '9/2/2021', '9:00AM'), ('SSCE2393', 'NUMERICAL METHODS', '33', 'FARHANA BT JOHAR', '9/2/2021', '9:00AM'), ('SSCE2393', 'NUMERICAL METHODS', '34', 'WAN ROHAIZAD BIN WAN IBRAHIM', '9/2/2021', '9:00AM'), ('SSCE2393', 'NUMERICAL METHODS', '35', 'NORMA BT ALIAS', '9/2/2021', '9:00AM'), ('SSCE2393', 'NUMERICAL METHODS', '36', 'HANG SEE PHENG', '9/2/2021', '9:00AM'), ('SSCE2393', 'NUMERICAL METHODS', '60', 'SHAZIRAWATIBINTI MOHD PUZI', '9/2/2021', '9:00AM')]

def course_list_in_tuples():
    tuple_courses = []

    for course in list_courses:
        course_date = course[4]
        date_split = course_date.split("/")
        course_time = course[5]
        time_split = course_time.split(":")

        hour = int(time_split[0])
        if time_split[1][-2] == "P":
            hour = int(time_split[0]) + 12

        minutes = int(time_split[1][0] + time_split[1][1])

        std_date = datetime.datetime(int(date_split[2]), int(date_split[1]), int(date_split[0]), hour, minutes)

        tuple_course = {
                            'courseID':course[0], 
                            'courseName':course[1], 
                            'section':course[2], 
                            'lecturer':course[3],
                            'date':course[4],
                            'time':course[5],
                            'std_dateTime': std_date,
                        }
        tuple_courses.append(tuple_course)


    return tuple_courses

def get_course_all():
    return course_list_in_tuples()

def get_course_no_repeat():
    temp_list = []
    previous_code = 'XXX'
    no_course = 0

    for course in course_list_in_tuples():   
        if previous_code != course['courseID']:
            no_course = no_course + 1
            previous_code = course['courseID']
            temp_list.append(course)

    return temp_list

def get_course_section(courseID):
    section_list = []
    for  course in course_list_in_tuples():
        if courseID == course['courseID']:  
            section_list.append(course)
    
    section_list.sort(key= lambda x: int(x['section']))
    return section_list

def get_course_detail(courseID, section):
    for  course in get_course_section(courseID):
        if section == course['section']:  
            return course