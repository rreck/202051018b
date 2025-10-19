```json
{
  "id": "ee9f240e4c1603d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285051,
  "host_pid": "9e6742732c60:1",
  "hash": "18fadc3b16ce5007a84385f4dcdca45628330983d9a661afc79e962200a391a5",
  "cid": "QmV118fadc3b16ce5007a84385f4dcdca45628330983",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285051,
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
      "evaluated_at": 1760285051
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
  "sig": "aeb93c5952bd0e7c495c33c1f3af974bd028a36e953357b5c2e65f30e8ad9f1e"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}