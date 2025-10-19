```json
{
  "id": "83ab748ab6edafb8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288440,
  "host_pid": "9e6742732c60:1",
  "hash": "bca4950a4df0950d1d4627ed53c7d5dbba9da9a1f91f3a654e40ab0b6921c749",
  "cid": "QmV1bca4950a4df0950d1d4627ed53c7d5dbba9da9a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288440,
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
      "evaluated_at": 1760288440
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
  "sig": "40ceddb7d8afd358a5b22a7131135a0ef6a2d51a2cbcea14f030300885fc2646"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246259253
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 10287102, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285765, 'matching_hash': '5582c4cd79a5b751'}}}