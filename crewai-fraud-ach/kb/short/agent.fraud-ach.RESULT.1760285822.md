```json
{
  "id": "a549db5086c419a3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285822,
  "host_pid": "9e6742732c60:1",
  "hash": "a33270e71ee7c72adc89194a521ad8a14539a81598c59d428d8a4fb55f6e883f",
  "cid": "QmV1a33270e71ee7c72adc89194a521ad8a14539a815",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285822,
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
      "evaluated_at": 1760285822
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
  "sig": "cf71b80645c6770cc20574ca50c2d8788ea44e7c7225373cc00c9387739f89d1"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 063100276282888
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 3, 'first_seen': 1760285763, 'matching_hash': '2c6b6a2c3736dbce'}}}