```json
{
  "id": "5340780ad9a09ccd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291025,
  "host_pid": "9e6742732c60:1",
  "hash": "2cf9dde67e4693522c236df4182ae03cd91b49d1f3a5db0fdc5b8049db9c3647",
  "cid": "QmV12cf9dde67e4693522c236df4182ae03cd91b49d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291025,
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
      "evaluated_at": 1760291025
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "338e2444644aac6c0486a8607a980a22c5f73492c8e923dcda828d63882c1b7b"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201467886368
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 82500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285763, 'matching_hash': 'b8e6d176a4768585'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}