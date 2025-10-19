```json
{
  "id": "96a73791f09ee67f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286125,
  "host_pid": "9e6742732c60:1",
  "hash": "c9a545ec36a328ef9d14e847c1aac1b25dd3c0870a480c57bf0e0344f70f1191",
  "cid": "QmV1c9a545ec36a328ef9d14e847c1aac1b25dd3c087",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286125,
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
      "evaluated_at": 1760286125
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
  "sig": "218f82b4c19c646c6751667e429d6e2f126ef23cf638eb5e43383f337aa9ac10"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000240849779
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 14, 'first_seen': 1760285763, 'matching_hash': '760b7e67ac1502b4'}}}