```json
{
  "id": "25172286aa7974fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288096,
  "host_pid": "9e6742732c60:1",
  "hash": "3e4658f66b04537ab3797474a6d89373ef4f2a5e445bd10291b33c629a9b6e0c",
  "cid": "QmV13e4658f66b04537ab3797474a6d89373ef4f2a5e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288096,
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
      "evaluated_at": 1760288096
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
  "sig": "fcfeca29654151006f945a414bc28fde18cf526dea37e9ababcb81f314edc81b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033965137
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 11699760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285765, 'matching_hash': 'a94abbf708458614'}}}