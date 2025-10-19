```json
{
  "id": "e7b98e31d84be7c5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287413,
  "host_pid": "9e6742732c60:1",
  "hash": "fbd544be6154251e91dd61f12864b72a4b1f391700cc059010632b7b0c8aa82b",
  "cid": "QmV1fbd544be6154251e91dd61f12864b72a4b1f3917",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287413,
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
      "evaluated_at": 1760287413
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "9077558d24fbce7714d5aa0c0d990de310a4610347fd4ea2d79223d01e5c349f"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009594283807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 59, 'threshold': 50, 'total_amount': 11892689, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 58, 'first_seen': 1760285764, 'matching_hash': 'e41bbca7fc0ba663'}}}