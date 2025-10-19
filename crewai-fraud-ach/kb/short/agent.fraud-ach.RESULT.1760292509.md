```json
{
  "id": "6b5341049a4aa697",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292509,
  "host_pid": "9e6742732c60:1",
  "hash": "aae913a7d4e962541225158c3a1fdb4bac3f8f973cd03a270fe0c9442c6526cd",
  "cid": "QmV1aae913a7d4e962541225158c3a1fdb4bac3f8f97",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292509,
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
      "evaluated_at": 1760292509
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
  "sig": "0f32e837e8cdfb7ce05ab340f96ac88170f500cf9f68d7afdbd1c42e435f002d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032539256
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 98315950, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': '34ea678ce834982a'}}}