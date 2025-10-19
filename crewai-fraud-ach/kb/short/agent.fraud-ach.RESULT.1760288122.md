```json
{
  "id": "816cdc8fdb8b83bc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288122,
  "host_pid": "9e6742732c60:1",
  "hash": "6f4401b41c776b768d9181f85887f6fbed2da39c9627b6039abf1f84d3e7f570",
  "cid": "QmV16f4401b41c776b768d9181f85887f6fbed2da39c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288122,
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
      "evaluated_at": 1760288122
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
  "sig": "2173d139596956449f5026404a3d4097a8e9ffa98956369d93d7a6c11b8c8909"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159904059
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50, 'total_amount': 37257704, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285764, 'matching_hash': '7ad1725ffd2dadfd'}}}