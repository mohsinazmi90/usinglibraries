import sys
import math
import random
from PyQt6.QtCore import (
    Qt, QPointF, QRectF, QPropertyAnimation, QEasingCurve, 
    QParallelAnimationGroup, QSequentialAnimationGroup, pyqtProperty, QObject
)
from PyQt6.QtGui import (
    QPainter, QColor, QPen, QBrush, QLinearGradient, 
    QPainterPath, QAction, QKeySequence, QImage
)
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, 
    QDockWidget, QTreeWidget, QTreeWidgetItem, QLabel, 
    QPushButton, QGraphicsView, QGraphicsScene, QGraphicsObject, 
    QFileDialog, QGroupBox, QSpinBox, QGraphicsDropShadowEffect, QComboBox
)

# ----------------------------------------------------------------------
# Animatable Graphics Object with Custom Property Transitions
# ----------------------------------------------------------------------
class TransitionNodeItem(QGraphicsObject):
    """
    Custom QGraphicsObject exposing Qt Properties (animScale, animOpacity, animRotation)
    to enable smooth hardware-accelerated property transitions via QPropertyAnimation.
    """
    
    def __init__(self, path, primary_color, secondary_color):
        super().__init__()
        self._path = path
        self._primary_color = primary_color
        self._secondary_color = secondary_color
        
        # Animatable Internal States
        self._anim_scale = 1.0
        self._anim_opacity = 1.0
        self._anim_rotation = 0.0

        # Item Flags & Setup
        self.setFlags(
            QGraphicsObject.GraphicsItemFlag.ItemIsMovable |
            QGraphicsObject.GraphicsItemFlag.ItemIsSelectable |
            QGraphicsObject.GraphicsItemFlag.ItemSendsGeometryChanges
        )
        self.setAcceptHoverEvents(True)

        # Glow Effect Transition Target
        self.glow_effect = QGraphicsDropShadowEffect()
        self.glow_effect.setBlurRadius(25)
        self.glow_effect.setColor(self._primary_color)
        self.glow_effect.setOffset(0, 0)
        self.setGraphicsEffect(self.glow_effect)

    def boundingRect(self):
        return self._path.boundingRect().adjusted(-20, -20, 20, 20)

    def paint(self, painter, option, widget=None):
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Draw Gradient Path
        rect = self._path.boundingRect()
        gradient = QLinearGradient(rect.topLeft(), rect.bottomRight())
        gradient.setColorAt(0.0, self._primary_color)
        gradient.setColorAt(1.0, self._secondary_color)
        
        pen = QPen(self._primary_color.lighter(150), 2)
        pen.setCosmetic(True)
        painter.setPen(pen)
        painter.setBrush(QBrush(gradient))
        painter.setOpacity(self._anim_opacity)
        painter.drawPath(self._path)

    # --- Qt Properties for QPropertyAnimation Transition Engine ---
    
    def get_anim_scale(self):
        return self._anim_scale

    def set_anim_scale(self, value):
        self._anim_scale = value
        self.setScale(value)
        self.update()

    animScale = pyqtProperty(float, get_anim_scale, set_anim_scale)

    def get_anim_opacity(self):
        return self._anim_opacity

    def set_anim_opacity(self, value):
        self._anim_opacity = value
        self.update()

    animOpacity = pyqtProperty(float, get_anim_opacity, set_anim_opacity)

    def get_anim_rotation(self):
        return self._anim_rotation

    def set_anim_rotation(self, value):
        self._anim_rotation = value
        self.setRotation(value)
        self.update()

    animRotation = pyqtProperty(float, get_anim_rotation, set_anim_rotation)

# ----------------------------------------------------------------------
# Procedural Geometry Engine
# ----------------------------------------------------------------------
class FlowGeometryEngine:
    @staticmethod
    def generate_starburst(points, outer_r, inner_r):
        path = QPainterPath()
        angle_step = math.pi / points
        for i in range(2 * points):
            r = outer_r if i % 2 == 0 else inner_r
            angle = i * angle_step
            pt = QPointF(r * math.cos(angle), r * math.sin(angle))
            if i == 0:
                path.moveTo(pt)
            else:
                path.lineTo(pt)
        path.closeSubpath()
        return path

    @staticmethod
    def generate_superellipse(a, b, n=2.5, steps=200):
        path = QPainterPath()
        first = True
        for i in range(steps + 1):
            t = (i / steps) * 2 * math.pi
            cos_t = math.cos(t)
            sin_t = math.sin(t)
            
            x = math.copysign(1, cos_t) * (abs(cos_t) ** (2 / n)) * a
            y = math.copysign(1, sin_t) * (abs(sin_t) ** (2 / n)) * b
            
            if first:
                path.moveTo(x, y)
                first = False
            else:
                path.lineTo(x, y)
        path.closeSubpath()
        return path

# ----------------------------------------------------------------------
# Interactive Viewport with Smooth Zoom/Pan
# ----------------------------------------------------------------------
class QuantumCanvasView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.setRenderHints(QPainter.RenderHint.Antialiasing | QPainter.RenderHint.SmoothPixmapTransform)
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.is_panning = False
        self.pan_start = QPointF()

    def wheelEvent(self, event):
        zoom_factor = 1.15 if event.angleDelta().y() > 0 else 1 / 1.15
        self.scale(zoom_factor, zoom_factor)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.MiddleButton:
            self.is_panning = True
            self.pan_start = event.position()
            self.setCursor(Qt.CursorShape.ClosedHandCursor)
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.is_panning:
            delta = event.position() - self.pan_start
            self.pan_start = event.position()
            self.horizontalScrollBar().setValue(int(self.horizontalScrollBar().value() - delta.x()))
            self.verticalScrollBar().setValue(int(self.verticalScrollBar().value() - delta.y()))
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.MouseButton.MiddleButton:
            self.is_panning = False
            self.setCursor(Qt.CursorShape.ArrowCursor)
        else:
            super().mouseReleaseEvent(event)

    def drawBackground(self, painter, rect):
        painter.fillRect(rect, QColor("#090b10"))
        grid_size = 40
        left = int(rect.left()) - (int(rect.left()) % grid_size)
        top = int(rect.top()) - (int(rect.top()) % grid_size)
        
        pen = QPen(QColor(0, 255, 170, 15), 1, Qt.PenStyle.DotLine)
        painter.setPen(pen)
        
        for x in range(left, int(rect.right()), grid_size):
            painter.drawLine(x, int(rect.top()), x, int(rect.bottom()))
        for y in range(top, int(rect.bottom()), grid_size):
            painter.drawLine(int(rect.left()), y, int(rect.right()), y)

# ----------------------------------------------------------------------
# Main Application Window
# ----------------------------------------------------------------------
class QuantumFlowStudio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuantumFlow Studio - Property Transition Generator")
        self.resize(1300, 850)
        self.setStyleSheet(self._dark_quantum_stylesheet())

        # Graphics Scene & Viewport
        self.scene = QGraphicsScene(-2000, -2000, 4000, 4000)
        self.view = QuantumCanvasView(self.scene)
        self.setCentralWidget(self.view)

        # Active Transition Group Reference
        self.active_animation_group = None

        # Build Interfaces
        self._setup_dock_panels()
        self._setup_menu_bar()
        
        # Initial Node
        self.add_starburst_node()

    def trigger_transition(self):
        """Builds and executes a multi-property transition group using QPropertyAnimation."""
        items = [i for i in self.scene.items() if isinstance(i, TransitionNodeItem)]
        if not items:
            return

        # Select target Easing Curve from combo box
        curve_type = self.curve_combo.currentData()
        duration = self.duration_spin.value()

        self.active_animation_group = QParallelAnimationGroup()

        for item in items:
            # 1. Scale Transition
            anim_scale = QPropertyAnimation(item, b"animScale")
            anim_scale.setDuration(duration)
            anim_scale.setStartValue(item.get_anim_scale())
            anim_scale.setEndValue(random.uniform(0.5, 2.2))
            anim_scale.setEasingCurve(curve_type)

            # 2. Rotation Transition
            anim_rot = QPropertyAnimation(item, b"animRotation")
            anim_rot.setDuration(duration)
            anim_rot.setStartValue(item.get_anim_rotation())
            anim_rot.setEndValue(item.get_anim_rotation() + random.choice([-180, 180, 360]))
            anim_rot.setEasingCurve(curve_type)

            # 3. Fade Opacity Transition
            anim_fade = QPropertyAnimation(item, b"animOpacity")
            anim_fade.setDuration(duration)
            anim_fade.setStartValue(item.get_anim_opacity())
            anim_fade.setEndValue(random.uniform(0.4, 1.0))
            anim_fade.setEasingCurve(QEasingCurve.Type.InOutSine)

            # Add to Parallel Group
            self.active_animation_group.addAnimation(anim_scale)
            self.active_animation_group.addAnimation(anim_rot)
            self.active_animation_group.addAnimation(anim_fade)

        self.active_animation_group.start()

    def add_starburst_node(self):
        path = FlowGeometryEngine.generate_starburst(
            points=self.star_pts.value(),
            outer_r=self.star_outer.value(),
            inner_r=self.star_inner.value()
        )
        c1 = QColor.fromHsv(random.randint(140, 200), 230, 255)
        c2 = QColor.fromHsv(random.randint(280, 340), 230, 255)
        node = TransitionNodeItem(path, c1, c2)
        node.setPos(random.randint(-80, 80), random.randint(-80, 80))
        self.scene.addItem(node)
        self._refresh_layer_tree()

    def add_superellipse_node(self):
        path = FlowGeometryEngine.generate_superellipse(
            a=self.ellipse_a.value(),
            b=self.ellipse_b.value()
        )
        c1 = QColor.fromHsv(random.randint(20, 80), 230, 255)
        c2 = QColor.fromHsv(random.randint(180, 240), 230, 255)
        node = TransitionNodeItem(path, c1, c2)
        node.setPos(random.randint(-80, 80), random.randint(-80, 80))
        self.scene.addItem(node)
        self._refresh_layer_tree()

    def clear_canvas(self):
        self.scene.clear()
        self._refresh_layer_tree()

    def _refresh_layer_tree(self):
        self.layer_tree.clear()
        for idx, item in enumerate(self.scene.items()):
            if isinstance(item, TransitionNodeItem):
                tree_item = QTreeWidgetItem([f"Flow Node {idx + 1}", f"Scale: {item.get_anim_scale():.2f}x"])
                self.layer_tree.addTopLevelItem(tree_item)

    # ------------------------------------------------------------------
    # UI Setup
    # ------------------------------------------------------------------
    def _setup_dock_panels(self):
        # Left Panel
        controls_dock = QDockWidget("Transition & Generator", self)
        controls_dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)
        panel = QWidget()
        layout = QVBoxLayout(panel)

        # Transition Engine Settings Group
        trans_group = QGroupBox("Transition Engine")
        trans_layout = QVBoxLayout(trans_group)
        
        self.curve_combo = QComboBox()
        self.curve_combo.addItem("OutBack (Elastic Bounce)", QEasingCurve.Type.OutBack)
        self.curve_combo.addItem("OutBounce (Hard Bounce)", QEasingCurve.Type.OutBounce)
        self.curve_combo.addItem("InOutExpo (Smooth Power)", QEasingCurve.Type.InOutExpo)
        self.curve_combo.addItem("InOutSine (Soft Flow)", QEasingCurve.Type.InOutSine)
        self.curve_combo.addItem("OutElastic (Spring)", QEasingCurve.Type.OutElastic)

        self.duration_spin = QSpinBox()
        self.duration_spin.setRange(200, 5000)
        self.duration_spin.setValue(1200)
        self.duration_spin.setSingleStep(100)
        self.duration_spin.setSuffix(" ms")

        trans_layout.addWidget(QLabel("Easing Curve Transition:"))
        trans_layout.addWidget(self.curve_combo)
        trans_layout.addWidget(QLabel("Transition Duration:"))
        trans_layout.addWidget(self.duration_spin)

        btn_trigger = QPushButton("✨ Trigger Property Transition")
        btn_trigger.clicked.connect(self.trigger_transition)
        trans_layout.addWidget(btn_trigger)
        layout.addWidget(trans_group)

        # Starburst Generator
        star_group = QGroupBox("Starburst Settings")
        star_layout = QVBoxLayout(star_group)
        
        self.star_pts = QSpinBox(); self.star_pts.setRange(3, 30); self.star_pts.setValue(8)
        self.star_outer = QSpinBox(); self.star_outer.setRange(20, 400); self.star_outer.setValue(120)
        self.star_inner = QSpinBox(); self.star_inner.setRange(5, 300); self.star_inner.setValue(50)

        star_layout.addWidget(QLabel("Points Count:"))
        star_layout.addWidget(self.star_pts)
        star_layout.addWidget(QLabel("Outer Radius:"))
        star_layout.addWidget(self.star_outer)
        star_layout.addWidget(QLabel("Inner Radius:"))
        star_layout.addWidget(self.star_inner)

        btn_add_star = QPushButton("Generate Starburst")
        btn_add_star.clicked.connect(self.add_starburst_node)
        star_layout.addWidget(btn_add_star)
        layout.addWidget(star_group)

        # Superellipse Generator
        ellipse_group = QGroupBox("Superellipse Settings")
        ellipse_layout = QVBoxLayout(ellipse_group)
        
        self.ellipse_a = QSpinBox(); self.ellipse_a.setRange(20, 400); self.ellipse_a.setValue(100)
        self.ellipse_b = QSpinBox(); self.ellipse_b.setRange(20, 400); self.ellipse_b.setValue(100)

        ellipse_layout.addWidget(QLabel("X Radius (a):"))
        ellipse_layout.addWidget(self.ellipse_a)
        ellipse_layout.addWidget(QLabel("Y Radius (b):"))
        ellipse_layout.addWidget(self.ellipse_b)

        btn_add_ellipse = QPushButton("Generate Superellipse")
        btn_add_ellipse.clicked.connect(self.add_superellipse_node)
        ellipse_layout.addWidget(btn_add_ellipse)
        layout.addWidget(ellipse_group)

        # Global Clear
        clear_btn = QPushButton("Clear Canvas")
        clear_btn.clicked.connect(self.clear_canvas)
        layout.addWidget(clear_btn)

        layout.addStretch()
        panel.setLayout(layout)
        controls_dock.setWidget(panel)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, controls_dock)

        # Right Panel
        layers_dock = QDockWidget("Node Tree Inspector", self)
        self.layer_tree = QTreeWidget()
        self.layer_tree.setHeaderLabels(["Node Name", "State"])
        layers_dock.setWidget(self.layer_tree)
        self.addDockWidget(Qt.DockWidgetArea.RightDockWidgetArea, layers_dock)

    def _setup_menu_bar(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        export_act = QAction("Export High-Res Image...", self)
        export_act.setShortcut(QKeySequence.StandardKey.Save)
        export_act.triggered.connect(self.export_image)
        file_menu.addAction(export_act)

        file_menu.addSeparator()
        exit_act = QAction("Exit", self)
        exit_act.triggered.connect(self.close)
        file_menu.addAction(exit_act)

    def export_image(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Export Canvas", "", "PNG Image (*.png);;JPEG Image (*.jpg)")
        if file_path:
            rect = self.scene.itemsBoundingRect()
            if rect.isEmpty():
                rect = QRectF(-200, -200, 400, 400)
            
            image = QImage(int(rect.width()), int(rect.height()), QImage.Format.Format_ARGB32)
            image.fill(QColor("#090b10"))
            
            painter = QPainter(image)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            self.scene.render(painter, QRectF(image.rect()), rect)
            painter.end()
            image.save(file_path)

    def _dark_quantum_stylesheet(self):
        return """
        QMainWindow { background-color: #050608; }
        QDockWidget { color: #00ffaa; titlebar-close-icon: none; titlebar-normal-icon: none; }
        QDockWidget::title { background: #0e1118; padding: 6px; font-weight: bold; border-bottom: 1px solid #00ffaa; }
        QWidget { background-color: #0a0d14; color: #b0c0d0; font-family: 'Segoe UI', monospace; font-size: 13px; }
        QGroupBox { border: 1px solid #161e2e; border-radius: 5px; margin-top: 10px; padding-top: 10px; font-weight: bold; }
        QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; color: #00ffaa; }
        QPushButton { background-color: #121824; border: 1px solid #00ffaa; padding: 6px; border-radius: 4px; font-weight: bold; color: #00ffaa; }
        QPushButton:hover { background-color: #00ffaa; color: #050608; }
        QPushButton:pressed { background-color: #ff007f; color: #ffffff; border-color: #ff007f; }
        QComboBox, QSpinBox { background-color: #050608; border: 1px solid #161e2e; padding: 4px; color: #00ffaa; border-radius: 3px; }
        QTreeWidget { background-color: #050608; border: 1px solid #161e2e; }
        QHeaderView::section { background-color: #0e1118; color: #00ffaa; padding: 4px; border: none; }
        """

# ----------------------------------------------------------------------
# Application Entrypoint
# ----------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuantumFlowStudio()
    window.show()
    sys.exit(app.exec())