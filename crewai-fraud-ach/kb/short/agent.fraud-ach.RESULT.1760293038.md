```json
{
  "id": "6f2d9dc7d05c76f3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293038,
  "host_pid": "9e6742732c60:1",
  "hash": "7733054799379d666c6ae8596193bff3d75f1bfffaa10ecee7b2082c178d1579",
  "cid": "QmV17733054799379d666c6ae8596193bff3d75f1bff",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293038,
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
      "evaluated_at": 1760293039
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
  "sig": "feeaa1b9be887fb97ef1e307e2685f699feecf434df6e446076b8fbf64f485c4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247969582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 286, 'threshold': 50, 'total_amount': 141510798, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 285, 'first_seen': 1760284979, 'matching_hash': '259c183eb9552f9c'}}}