```json
{
  "id": "eed02f50d213ff96",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287299,
  "host_pid": "9e6742732c60:1",
  "hash": "be656635a585b461ef9ec93d0ce1fcad5e28bf1b0ef892d43e3aa8598d6ebdda",
  "cid": "QmV1be656635a585b461ef9ec93d0ce1fcad5e28bf1b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287299,
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
      "evaluated_at": 1760287299
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
  "sig": "ac3bbb57c9d6902cd4bc40a1f7755d368f505900e52dc62007ea9de0e7825c92"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000243340063
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 55, 'threshold': 50, 'total_amount': 23313510, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285763, 'matching_hash': '5f2724e98c8a67b0'}}}