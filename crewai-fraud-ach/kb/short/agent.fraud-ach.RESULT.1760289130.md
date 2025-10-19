```json
{
  "id": "4bd0723a372bfc1c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289130,
  "host_pid": "9e6742732c60:1",
  "hash": "a0dba910102b23ecac07fa9aa935d493b61196bd2311bfde675981ef6feeea36",
  "cid": "QmV1a0dba910102b23ecac07fa9aa935d493b61196bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289130,
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
      "evaluated_at": 1760289130
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
  "sig": "f6994f18ccd0275c43c8a3413767b04b66a748e882e3aa549f0705f5d26d1ca7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025723119
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 114, 'threshold': 50, 'total_amount': 53760006, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 113, 'first_seen': 1760285764, 'matching_hash': '7f709c8256c8a242'}}}