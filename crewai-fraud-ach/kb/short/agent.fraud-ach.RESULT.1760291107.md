```json
{
  "id": "bf2b069472d5497b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291107,
  "host_pid": "9e6742732c60:1",
  "hash": "cb47948058ceb1a1a373e31e062563a3605a5577d8459ae3183cf6a8036249ae",
  "cid": "QmV1cb47948058ceb1a1a373e31e062563a3605a5577",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291107,
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
      "evaluated_at": 1760291107
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
  "sig": "94f494556f61264b75c2465f3db1dc6072aa95c702f63250be14278389e76c31"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100273039049
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 56822919, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': '71e11df02cc7494b'}}}