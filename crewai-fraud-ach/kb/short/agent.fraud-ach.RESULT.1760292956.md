```json
{
  "id": "cd55aa9d23bfca68",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292956,
  "host_pid": "9e6742732c60:1",
  "hash": "0053ed1a55ac5f7431b6ebfdd9ee6c9420236ca75c04a4ad70e942ff5a594ddd",
  "cid": "QmV10053ed1a55ac5f7431b6ebfdd9ee6c9420236ca7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292956,
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
      "evaluated_at": 1760292956
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
  "sig": "c595125347c12b1d8a870b2e8e656080a15dadc5a9feb093c1c2de31150d5512"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 208, 'threshold': 50, 'total_amount': 66195584, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 207, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}