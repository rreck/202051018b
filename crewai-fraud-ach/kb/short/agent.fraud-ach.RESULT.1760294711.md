```json
{
  "id": "d8b6c9586a748513",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294711,
  "host_pid": "9e6742732c60:1",
  "hash": "1e54d7ab10a6745c78618ab934dfb3b4befb04d2cce983bb37a0f9bd9231bb03",
  "cid": "QmV11e54d7ab10a6745c78618ab934dfb3b4befb04d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294711,
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
      "evaluated_at": 1760294711
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
  "sig": "51d29f9201f47ab3c0cf69b84995c784cfcdc05fa1d1f55854ecb184264550c5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279745557
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 22751118, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285765, 'matching_hash': '46b84f4cf2bc4bde'}}}