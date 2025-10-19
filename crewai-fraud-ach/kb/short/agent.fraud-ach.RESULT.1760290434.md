```json
{
  "id": "cc9114e57107e9ea",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290434,
  "host_pid": "9e6742732c60:1",
  "hash": "644e8f3be8f3609920a9a1b8eee56a91e580c57cf119494c05f274359f0f913b",
  "cid": "QmV1644e8f3be8f3609920a9a1b8eee56a91e580c57c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290434,
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
      "evaluated_at": 1760290435
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
  "sig": "51901a53f5ce43ea034d8e4940b38030a449dfe0ba8c5478c96087a7ba404711"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035599822
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 23140050, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': 'a98e7fc79b0958d1'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '039274537', 'validation_error': 'Invalid routing number checksum'}}}