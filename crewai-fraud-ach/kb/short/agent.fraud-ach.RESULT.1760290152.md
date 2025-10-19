```json
{
  "id": "c121e06cc3022e25",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290152,
  "host_pid": "9e6742732c60:1",
  "hash": "163c01e13253b60f300985e16ecf9a60131c7a8590b05f0bc0dcdb58d2178731",
  "cid": "QmV1163c01e13253b60f300985e16ecf9a60131c7a85",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290152,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760290152
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "97aaa6266cbb623144d525f3b1c7e3b21ee7b5da255b38502ccdc5fd31d42395"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037116719
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 25473448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285763, 'matching_hash': 'c24831f619c6556e'}}}