```json
{
  "id": "7f25f3e236c90982",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294114,
  "host_pid": "9e6742732c60:1",
  "hash": "ba431f338c9abdf08f346828ad01b95ba75254b3b9aeaaf73b336014c61e2d59",
  "cid": "QmV1ba431f338c9abdf08f346828ad01b95ba75254b3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294114,
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
      "evaluated_at": 1760294114
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
  "sig": "8d5fcc77bac0e893a8611ff2d367db5f84e50f1b26e89ae7cf9563bbadbdd7a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038072034
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 80977048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': '336ae1a1ad6e821c'}}}