'use client'
import Image from 'next/image'
import Link from 'next/link'

import React, { useState } from 'react';
import Slider from 'react-slider';
import { motion } from 'framer-motion';

export default function Home() {
    const [sliderValue1, setSliderValue1] = useState(50); // Initial value for the first slider
    const [sliderValue2, setSliderValue2] = useState(25); // Initial value for the second slider

    return (
        <div className="p-4 space-y-4">
          <div className="w-64">
            <label htmlFor="slider1" className="block font-semibold">
              Slider 1
            </label>
            <Slider
              className="bg"
              value={sliderValue1}
              min={0}
              max={100}
              onChange={(value) => setSliderValue1(value)}
            />
            <div className="text-center mt-2">{sliderValue1}</div>
          </div>
    
          <div className="w-64">
            <label htmlFor="slider2" className="block font-semibold">
              Slider 2
            </label>
            <Slider
              className="my-other-slider-class"
              value={sliderValue2}
              min={0}
              max={100}
              onChange={(value) => setSliderValue2(value)}
            />
            <div className="text-center mt-2">{sliderValue2}</div>
          </div>
        </div>
    );

    
}
