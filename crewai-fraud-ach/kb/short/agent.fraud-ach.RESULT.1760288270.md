```json
{
  "id": "26b8715da22c56b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288270,
  "host_pid": "9e6742732c60:1",
  "hash": "8ac6538ca5b0adbe560f7f975debfcf5dbecf47ee9674b7ed8cc2f5a897de941",
  "cid": "QmV18ac6538ca5b0adbe560f7f975debfcf5dbecf47e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288270,
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
      "evaluated_at": 1760288270
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
  "sig": "643b885f9e2e8fd5171c3398d0dea8af21da8e10ca764c418dd56fe6440198b6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277046981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 27291440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285763, 'matching_hash': '189e75bc7166d961'}}}