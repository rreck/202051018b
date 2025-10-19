```json
{
  "id": "c5dd8ab616910cd4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293246,
  "host_pid": "9e6742732c60:1",
  "hash": "f7b7d8756d7011b7b1e9316c208f0b627e4857e4d84b7bf6b50b60521dc1a3fe",
  "cid": "QmV1f7b7d8756d7011b7b1e9316c208f0b627e4857e4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293246,
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
      "evaluated_at": 1760293246
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
  "sig": "ea25ce79eb3bb821e3e2d5a68e1d5d152fca0cd108dfb74d7e01eb5f90b250a2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000026265735
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 214, 'threshold': 50, 'total_amount': 75346832, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 213, 'first_seen': 1760285765, 'matching_hash': 'e94388ee515b2db1'}}}