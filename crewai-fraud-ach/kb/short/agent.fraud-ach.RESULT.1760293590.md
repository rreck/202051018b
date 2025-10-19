```json
{
  "id": "3ace1a55ebdf7a8e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293590,
  "host_pid": "9e6742732c60:1",
  "hash": "607f82baa0b5cbf629803ae15bb3488bf89e05af0c300e1a74599c86a1146f06",
  "cid": "QmV1607f82baa0b5cbf629803ae15bb3488bf89e05af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293590,
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
      "evaluated_at": 1760293590
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
  "sig": "f3fbbcbc04beaf95bb290c275300840005efa3a85245263e6c0ee6147d7cca4a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 70332808, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}