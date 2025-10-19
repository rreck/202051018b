```json
{
  "id": "bf05829f199c2546",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288474,
  "host_pid": "9e6742732c60:1",
  "hash": "04d5e86cce160254043f72d2e25ffb16a89193dfa23236528b66a7436630034c",
  "cid": "QmV104d5e86cce160254043f72d2e25ffb16a89193df",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288474,
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
      "evaluated_at": 1760288474
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
  "sig": "39c50f8accce4210860c708b2b1fecb8318807b9c36d2f3986e3867c80bbb700"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201466322331
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285765, 'matching_hash': '8006c6780242cc6a'}}}