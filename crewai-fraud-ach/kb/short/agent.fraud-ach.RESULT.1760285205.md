```json
{
  "id": "f99bad86be9d7be7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285205,
  "host_pid": "9e6742732c60:1",
  "hash": "081075c3bbc2dc7fd7570921ae608051f0d5015b33858815cb3c8ad9b8e593b5",
  "cid": "QmV1081075c3bbc2dc7fd7570921ae608051f0d5015b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285205,
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
      "evaluated_at": 1760285205
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
  "sig": "5bc4b0f8d782d40c8c65119c5dafe23189f9b69f92cffaeb2a418ec055da7157"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000026203898
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 22, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}