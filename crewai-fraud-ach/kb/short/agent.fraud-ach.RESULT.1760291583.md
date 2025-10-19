```json
{
  "id": "b6eb82e55e45286b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291583,
  "host_pid": "9e6742732c60:1",
  "hash": "8874059a933cadce588452db56d6f0ac4b6f3349409d3c7bbe1c9c7f1c11d9c7",
  "cid": "QmV18874059a933cadce588452db56d6f0ac4b6f3349",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291583,
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
      "evaluated_at": 1760291583
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
  "sig": "deb96b86707b7db009f68114c3bf8b962c20526c0809bc0a965aa1af0b4be21b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594283807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 35879638, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285764, 'matching_hash': 'e41bbca7fc0ba663'}}}