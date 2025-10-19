```json
{
  "id": "c00bbb81b5c78c60",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288982,
  "host_pid": "9e6742732c60:1",
  "hash": "0dc38fd6ccfa2c4e07ea20d254046d875473d442405f85c6a986c57f0c740203",
  "cid": "QmV10dc38fd6ccfa2c4e07ea20d254046d875473d442",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288982,
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
      "evaluated_at": 1760288982
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
  "sig": "09855bd9ff219792537f3dcf589d3b5bb42c8b19030038a764b2531b2a2449e0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154543608
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 110, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 109, 'first_seen': 1760285763, 'matching_hash': '3d9c367e54a48e12'}}}een': 1760285763, 'matching_hash': '3f378333472d9dcb'}}}