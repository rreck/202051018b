```json
{
  "id": "4c41e2b18ebf81c1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289390,
  "host_pid": "9e6742732c60:1",
  "hash": "a10de924b095caa0bc8a25720b50de52fc81c1550f6ba868f5315b15d2ab2394",
  "cid": "QmV1a10de924b095caa0bc8a25720b50de52fc81c155",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289390,
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
      "evaluated_at": 1760289390
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
  "sig": "426e0d3a142059234c25d7f8afc38a94c0a4ed59fa07592a97e5dacf9c915043"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027962561
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 122, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 121, 'first_seen': 1760285763, 'matching_hash': '3395f05250aaaeda'}}}een': 1760285763, 'matching_hash': '9f3869b775bbb8aa'}}}