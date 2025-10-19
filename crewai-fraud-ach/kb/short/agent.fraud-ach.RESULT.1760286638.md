```json
{
  "id": "ba4d0443fbaa75d1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286638,
  "host_pid": "9e6742732c60:1",
  "hash": "cd2bc6612093de17b5387fc3d3604facf22454d8676a43d2881c4e2bce105383",
  "cid": "QmV1cd2bc6612093de17b5387fc3d3604facf22454d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286638,
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
      "evaluated_at": 1760286638
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "a9060aa8ccea23dcd796664693fb3672d5530df4a98a5210e489f340e4004f3a"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105155324238
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15070624, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 31, 'first_seen': 1760285764, 'matching_hash': '6027d2fe89c09f43'}}}