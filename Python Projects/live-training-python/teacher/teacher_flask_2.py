# import sys 
# import math
# import random
# import json
# from PyQt6.QtCore import Qt, QPointF, QRectF, QTimer
# from PyQt6.QtGui import (
#     QPainter, QColor, QPen, QBrush, QLinearGradient, QRadialGradient, 
#     QPainterPath, QTransform, QFont, QAction, QKeySequence
# )
# from PyQt6.QtWidgets import (
#     QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, 
#     QDockWidget, QTreeWidget, QTreeWidgetItem, QSlider, QLabel, 
#     QPushButton, QGraphicsView, QGraphicsScene, QGraphicsItem, 
#     QGraphicsPathItem, QFileDialog, QComboBox, QGroupBox, QSpinBox,
#     QColorDialog, QSplitter
# )

# # -----------------
# # PROCEDURAL GENERATOR ENGINE
# # -----------------

# class ProceduralArtGenerator:
#     """
#     GENERATOR GENERATES DYNAMIC VECTOR PATHS BASED ON MATHEMATICAL ALGORITHMS.
#     """
    
#     @staticmethod
#     def generate_spirograph(R, r, p, steps=1000):
#         path = QPainterPath()
#         first = True
        
#         for i in range(steps):
#             t = (i / steps) * 8 * math.pi
#             x = (R - r) * math.cos(t) + p * math.cos((R - r) * t / r)
#             y = (R - r) * math.sin(t) - p * math.sin((R - r) * t / r)
#             if first:
#                 path.moveTo(x, y)
#                 first = False
#             else:
#                 path.closeSubpath()
#                 return path
    
#     @staticmethod
#     def generate_mandala(petals, radius, inner_radius):
#         path = QPainterPath()
#         angle_step = (2 * math.pi() / petals)
#         for i in range(petals):
#             angle = i * angle_step
#             next_angle = (i + 1) * angle_step
#             mid_angle = (angle + angle_step) / 2
#             p1 = QPointF(math.cos(angle) * inner_radius, math.sin(angle) * inner_radius)
#             ctrl = QPointF(math.cos(mid_angle) * radius, math.sin(mid_angle) * radius)
#             p2 = QPointF(math.cos(next_angle) * inner_radius, math.sin(next_angle) * inner_radius)
#             if i == 0:
#                 path.moveTo(p1)
#                 path.quadTo(ctrl, p2)
#                 path.closeSubpath()
#                 return path
            
# # -----------------
# # INTERACTIVE CANVAS ITEM
# # -----------------
            
# class VectorNodeItem(QGraphicsPathItem):
#     """
#     'INTERACTIVE VECTOR OBJECT' SUPPORTIG TRANSFORMATION, COLORING, AND ANIMATIONS.
#     """
    
#     def __init__(self, path, color_start=QColor('#FF007F'), color_end=QColor('#7F00FF')):
#         super().__init__(path)
#         self.setFlags(
#             QGraphicsItem.GraphicsItemFlag.ItemIsMovable |
#             QGraphicsItem.GraphicsItemFlag.ItemIsSelectable |
#             QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges
#         )
#         self.setAcceptHoverEvents(True)
#         self.color_start = color_start
#         self.color_end = color_end
#         self.rotation_speed = 0.5
#         self.scale_factor = 1.0
#         self.update_brush()
    
#     def update_brush(self):
#         rect = self.boundingRect
#         gradient = QLinearGradient(rect.topLeft(), rect.bottomRight())
#         gradient.setColorAt(0.0, self.color_start)
#         gradient.setColorAt(1.0, self.color_end)
#         self.setPen(QPen(QColor(255, 255, 255, 180), 2))
#         self.setBrush(QBrush(gradient))
        
#     def step_animation(self):
#         self.setRotation(self.rotation() + self.rotation_speed)

# # -----------------
# # CUSTOME INTERACTIVE VIEWPORT
# # -----------------
                
# class StudioCanvasView(QGraphicsView):
#     """
#     VIEWPORT SUPPORTING ZOOM, PAN, GRID, SNAPPING, AND RENDERING SETUP
#     """
#     def __init__(self, scene):
#         super().__init__(scene)
#         self.setRenderHints(
#             QPainter.RenderHint.Antialiasing | 
#             QPainter.RenderHint.SmoothPixmapTransform
#         )
#         self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)
#         self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
#         self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
#         self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
#         self.is_panning = False
#         self.pan_start = QPointF()
        
#     def wheelEvent(self, event):
#         zoom_factor = 1.15 if event.angleDelta().y() > 0 else 1 / 1.15
#         self.scale(zoom_factor, zoom_factor)
        
import sys
import math
import random
import json
from PyQt6.QtCore import Qt, QPointF, QRectF, QTimer
from PyQt6.QtGui import (
    QPainter, QColor, QPen, QBrush, QLinearGradient, QRadialGradient, 
    QPainterPath, QTransform, QFont, QAction, QKeySequence
)
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, 
    QDockWidget, QTreeWidget, QTreeWidgetItem, QSlider, QLabel, 
    QPushButton, QGraphicsView, QGraphicsScene, QGraphicsItem, 
    QGraphicsPathItem, QFileDialog, QComboBox, QGroupBox, QSpinBox,
    QColorDialog, QSplitter
)

# ----------------------------------------------------------------------
# Procedural Generator Engine
# ----------------------------------------------------------------------
class ProceduralArtGenerator:
    """Generates dynamic vector paths based on mathematical algorithms."""
    
    @staticmethod
    def generate_spirograph(R, r, p, steps=1000):
        path = QPainterPath()
        first = True
        for i in range(steps):
            t = (i / steps) * 8 * math.pi
            x = (R - r) * math.cos(t) + p * math.cos((R - r) * t / r)
            y = (R - r) * math.sin(t) - p * math.sin((R - r) * t / r)
            if first:
                path.moveTo(x, y)
                first = False
            else:
                path.lineTo(x, y)
        path.closeSubpath()
        return path

    @staticmethod
    def generate_mandala(petals, radius, inner_radius):
        path = QPainterPath()
        angle_step = (2 * math.pi) / petals
        for i in range(petals):
            angle = i * angle_step
            next_angle = (i + 1) * angle_step
            mid_angle = angle + angle_step / 2
            p1 = QPointF(math.cos(angle) * inner_radius, math.sin(angle) * inner_radius)
            ctrl = QPointF(math.cos(mid_angle) * radius, math.sin(mid_angle) * radius)
            p2 = QPointF(math.cos(next_angle) * inner_radius, math.sin(next_angle) * inner_radius)
            
            if i == 0:
                path.moveTo(p1)
            path.quadTo(ctrl, p2)
        path.closeSubpath()
        return path

# ----------------------------------------------------------------------
# Interactive Canvas Items
# ----------------------------------------------------------------------
class VectorNodeItem(QGraphicsPathItem):
    """Interactive vector object supporting transformation, coloring, and animations."""
    
    def __init__(self, path, color_start=QColor("#ff007f"), color_end=QColor("#7f00ff")):
        super().__init__(path)
        self.setFlags(
            QGraphicsItem.GraphicsItemFlag.ItemIsMovable |
            QGraphicsItem.GraphicsItemFlag.ItemIsSelectable |
            QGraphicsItem.GraphicsItemFlag.ItemSendsGeometryChanges
        )
        self.setAcceptHoverEvents(True)
        self.color_start = color_start
        self.color_end = color_end
        self.rotation_speed = 0.5
        self.scale_factor = 1.0
        self.update_brush()

    def update_brush(self):
        rect = self.boundingRect()
        gradient = QLinearGradient(rect.topLeft(), rect.bottomRight())
        gradient.setColorAt(0.0, self.color_start)
        gradient.setColorAt(1.0, self.color_end)
        self.setPen(QPen(QColor(255, 255, 255, 180), 2))
        self.setBrush(QBrush(gradient))

    def step_animation(self):
        self.setRotation(self.rotation() + self.rotation_speed)

# ----------------------------------------------------------------------
# Custom Interactive Viewport
# ----------------------------------------------------------------------
class StudioCanvasView(QGraphicsView):
    """Viewport supporting zoom, pan, grid snapping, and rendering setup."""
    
    def __init__(self, scene):
        super().__init__(scene)
        self.setRenderHints(
            QPainter.RenderHint.Antialiasing | 
            QPainter.RenderHint.SmoothPixmapTransform
        )
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.FullViewportUpdate)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
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
        painter.fillRect(rect, QColor("#121216"))
        grid_size = 40
        left = int(rect.left()) - (int(rect.left()) % grid_size)
        top = int(rect.top()) - (int(rect.top()) % grid_size)
        
        pen = QPen(QColor(255, 255, 255, 15), 1, Qt.PenStyle.DotLine)
        painter.setPen(pen)
        
        for x in range(left, int(rect.right()), grid_size):
            painter.drawLine(x, int(rect.top()), x, int(rect.bottom()))
        for y in range(top, int(rect.bottom()), grid_size):
            painter.drawLine(int(rect.left()), y, int(rect.right()), y)

# ----------------------------------------------------------------------
# Main Application Window
# ----------------------------------------------------------------------
class ChromaForgeStudio(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ChromaForge Studio - Advanced Vector Generator")
        self.resize(1300, 850)
        self.setStyleSheet(self._dark_theme_stylesheet())

        # Scene Setup
        self.scene = QGraphicsScene(-2000, -2000, 4000, 4000)
        self.view = StudioCanvasView(self.scene)
        self.setCentralWidget(self.view)

        # Animation Loop
        self.anim_timer = QTimer()
        self.anim_timer.timeout.connect(self._animate_scene)
        self.is_playing = False

        # Build UI Components
        self._setup_dock_panels()
        self._setup_menu_bar()
        
        # Initial Canvas Creation
        self.add_spirograph_node()

    def _animate_scene(self):
        for item in self.scene.items():
            if isinstance(item, VectorNodeItem):
                item.step_animation()

    def toggle_animation(self):
        if self.is_playing:
            self.anim_timer.stop()
            self.play_btn.setText("▶️ Start Engine")
            self.play_btn.setStyleSheet("background-color: #007acc; color: white;")
        else:
            self.anim_timer.start(16) # ~60 FPS
            self.play_btn.setText("⏸ Pause Engine")
            self.play_btn.setStyleSheet("background-color: #d9534f; color: white;")
        self.is_playing = not self.is_playing

    def add_spirograph_node(self):
        path = ProceduralArtGenerator.generate_spirograph(
            R=self.R_spin.value(),
            r=self.r_spin.value(),
            p=self.p_spin.value()
        )
        c1 = QColor.fromHsv(random.randint(0, 360), 200, 255)
        c2 = QColor.fromHsv(random.randint(0, 360), 200, 255)
        node = VectorNodeItem(path, c1, c2)
        node.setPos(0, 0)
        self.scene.addItem(node)
        self._refresh_layer_tree()

    def add_mandala_node(self):
        path = ProceduralArtGenerator.generate_mandala(
            petals=self.petals_spin.value(),
            radius=self.radius_spin.value(),
            inner_radius=self.inner_r_spin.value()
        )
        c1 = QColor.fromHsv(random.randint(0, 360), 200, 255)
        c2 = QColor.fromHsv(random.randint(0, 360), 200, 255)
        node = VectorNodeItem(path, c1, c2)
        node.setPos(random.randint(-100, 100), random.randint(-100, 100))
        self.scene.addItem(node)
        self._refresh_layer_tree()

    def clear_canvas(self):
        self.scene.clear()
        self._refresh_layer_tree()

    def _refresh_layer_tree(self):
        self.layer_tree.clear()
        for idx, item in enumerate(self.scene.items()):
            if isinstance(item, VectorNodeItem):
                tree_item = QTreeWidgetItem([f"Node Layer {idx + 1}", f"Rot: {item.rotation():.1f}°"])
                self.layer_tree.addTopLevelItem(tree_item)

    # ------------------------------------------------------------------
    # UI Setup Helpers
    # ------------------------------------------------------------------
    def _setup_dock_panels(self):
        # Control Panel Dock
        controls_dock = QDockWidget("Procedural Generator", self)
        controls_dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)
        panel = QWidget()
        layout = QVBoxLayout(panel)

        # Spirograph Generator Group
        spiro_group = QGroupBox("Spirograph Settings")
        spiro_layout = QVBoxLayout(spiro_group)
        
        self.R_spin = QSpinBox(); self.R_spin.setRange(10, 500); self.R_spin.setValue(120)
        self.r_spin = QSpinBox(); self.r_spin.setRange(1, 300); self.r_spin.setValue(80)
        self.p_spin = QSpinBox(); self.p_spin.setRange(1, 300); self.p_spin.setValue(50)
        
        spiro_layout.addWidget(QLabel("Outer Radius (R):"))
        spiro_layout.addWidget(self.R_spin)
        spiro_layout.addWidget(QLabel("Inner Radius (r):"))
        spiro_layout.addWidget(self.r_spin)
        spiro_layout.addWidget(QLabel("Pen Distance (p):"))
        spiro_layout.addWidget(self.p_spin)
        
        btn_add_spiro = QPushButton("Generate Spirograph")
        btn_add_spiro.clicked.connect(self.add_spirograph_node)
        spiro_layout.addWidget(btn_add_spiro)
        layout.addWidget(spiro_group)

        # Mandala Generator Group
        mandala_group = QGroupBox("Mandala Settings")
        mandala_layout = QVBoxLayout(mandala_group)
        
        self.petals_spin = QSpinBox(); self.petals_spin.setRange(3, 64); self.petals_spin.setValue(12)
        self.radius_spin = QSpinBox(); self.radius_spin.setRange(20, 500); self.radius_spin.setValue(150)
        self.inner_r_spin = QSpinBox(); self.inner_r_spin.setRange(5, 300); self.inner_r_spin.setValue(30)

        mandala_layout.addWidget(QLabel("Petals Count:"))
        mandala_layout.addWidget(self.petals_spin)
        mandala_layout.addWidget(QLabel("Outer Radius:"))
        mandala_layout.addWidget(self.radius_spin)
        mandala_layout.addWidget(QLabel("Inner Radius:"))
        mandala_layout.addWidget(self.inner_r_spin)

        btn_add_mandala = QPushButton("Generate Mandala")
        btn_add_mandala.clicked.connect(self.add_mandala_node)
        mandala_layout.addWidget(btn_add_mandala)
        layout.addWidget(mandala_group)

        # Global Control Buttons
        self.play_btn = QPushButton("▶️ Start Engine")
        self.play_btn.clicked.connect(self.toggle_animation)
        layout.addWidget(self.play_btn)

        clear_btn = QPushButton("Clear Canvas")
        clear_btn.clicked.connect(self.clear_canvas)
        layout.addWidget(clear_btn)

        layout.addStretch()
        panel.setLayout(layout)
        controls_dock.setWidget(panel)
        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, controls_dock)

        # Layers Panel Dock
        layers_dock = QDockWidget("Node Tree", self)
        self.layer_tree = QTreeWidget()
        self.layer_tree.setHeaderLabels(["Layer Name", "State"])
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
        file_path, _ = QFileDialog.getSaveFileName(self, "Export Image", "", "PNG Image (*.png);;JPEG Image (*.jpg)")
        if file_path:
            rect = self.scene.itemsBoundingRect()
            if rect.isEmpty():
                rect = QRectF(-200, -200, 400, 400)
            
            image = QImage(int(rect.width()), int(rect.height()), QImage.Format.Format_ARGB32)
            image.fill(QColor("#121216"))
            
            painter = QPainter(image)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            self.scene.render(painter, QRectF(image.rect()), rect)
            painter.end()
            image.save(file_path)

    # ------------------------------------------------------------------
    # Stylesheet Definition
    # ------------------------------------------------------------------
    def _dark_theme_stylesheet(self):
        return """
        QMainWindow { background-color: #1a1a1e; }
        QDockWidget { color: #e0e0e0; titlebar-close-icon: none; titlebar-normal-icon: none; }
        QDockWidget::title { background: #25252b; padding: 6px; font-weight: bold; }
        QWidget { background-color: #1e1e24; color: #d0d0d0; font-family: 'Segoe UI', sans-serif; font-size: 13px; }
        QGroupBox { border: 1px solid #33333d; border-radius: 6px; margin-top: 10px; padding-top: 10px; font-weight: bold; }
        QGroupBox::title { subcontrol-origin: margin; left: 10px; padding: 0 5px; color: #007acc; }
        QPushButton { background-color: #2a2a35; border: 1px solid #3e3e4f; padding: 6px; border-radius: 4px; font-weight: bold; }
        QPushButton:hover { background-color: #3b3b4f; border-color: #007acc; }
        QPushButton:pressed { background-color: #007acc; }
        QSpinBox { background-color: #121216; border: 1px solid #33333d; padding: 4px; border-radius: 3px; color: #ffffff; }
        QTreeWidget { background-color: #121216; border: 1px solid #2a2a35; }
        QHeaderView::section { background-color: #25252b; color: #aaaaaa; padding: 4px; border: none; }
        """

# ----------------------------------------------------------------------
# Application Entrypoint
# ----------------------------------------------------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChromaForgeStudio()
    window.show()
    sys.exit(app.exec())