```json
{
  "id": "6b3a511739a94dcc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292951,
  "host_pid": "9e6742732c60:1",
  "hash": "8287e69cfc39288315887823b8362d5b9a422bb6c39556c7e733a8c8f616b996",
  "cid": "QmV18287e69cfc39288315887823b8362d5b9a422bb6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292951,
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
      "evaluated_at": 1760292951
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
  "sig": "7b2f38c10378d0707d307ea683846b5aaed6483c0415311f54848b6ae030ac01"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465632833
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 100231872, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285765, 'matching_hash': '908d3acbf69a371c'}}}