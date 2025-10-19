```json
{
  "id": "b4e6454a64a60f7e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291016,
  "host_pid": "9e6742732c60:1",
  "hash": "1c2659f5e42626281fc91f582f790fcc6dbbe33df41c8f81bfc6c8eaaac5af4c",
  "cid": "QmV11c2659f5e42626281fc91f582f790fcc6dbbe33d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291016,
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
      "evaluated_at": 1760291016
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
  "sig": "97bbf1a230a72078bb8c437a40de3b76a868ece66636d18a2bab57581535aa82"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464121559
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 74875845, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285763, 'matching_hash': '1ddc8562b5a9ecf0'}}}