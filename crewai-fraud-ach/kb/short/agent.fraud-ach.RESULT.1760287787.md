```json
{
  "id": "176368a4b94a036f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287787,
  "host_pid": "9e6742732c60:1",
  "hash": "cbed7b9858b4c2ea3a2bad4961d269b491d26d03ccfc74daa6cd09129372e341",
  "cid": "QmV1cbed7b9858b4c2ea3a2bad4961d269b491d26d03",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287787,
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
      "evaluated_at": 1760287787
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
  "sig": "5bb27fa691c1ab351ca6d12dd218c486f3c30c3676475ef710dadcae13b97b8c"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 122105155748621
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50, 'total_amount': 33459912, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285764, 'matching_hash': 'df4db45348ec5c9a'}}}