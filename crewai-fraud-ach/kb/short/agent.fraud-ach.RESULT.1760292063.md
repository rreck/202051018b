```json
{
  "id": "b82124df68f1100a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292063,
  "host_pid": "9e6742732c60:1",
  "hash": "fb264df7a6d566f8a99ba7b4459fef04105bc5cc1f0986ec7d9c90c2a1f4e4fb",
  "cid": "QmV1fb264df7a6d566f8a99ba7b4459fef04105bc5cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292063,
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
      "evaluated_at": 1760292063
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
  "sig": "c4fd4ddb909f1828a1147d9968b177a608b1f2586801f9afec788de87e7c26a9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241083307
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 189, 'threshold': 50, 'total_amount': 17266851, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 188, 'first_seen': 1760285763, 'matching_hash': '06ddfe971a6a4d24'}}}