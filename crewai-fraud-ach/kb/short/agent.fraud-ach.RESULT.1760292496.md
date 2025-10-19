```json
{
  "id": "d34b73a9dd130ccf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292496,
  "host_pid": "9e6742732c60:1",
  "hash": "c178b9e4e4a4e83fe81aa15972c72590cb813b5681c073522e06679655c998b4",
  "cid": "QmV1c178b9e4e4a4e83fe81aa15972c72590cb813b56",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292496,
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
      "evaluated_at": 1760292496
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
  "sig": "ced9eb1faa2bbeaffaa080eecf14bcc23ffb38c8dd13c9b08dfcc22c3666911d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026545394
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 199, 'threshold': 50, 'total_amount': 60534208, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 198, 'first_seen': 1760285763, 'matching_hash': '1ef68d78d8cabe5b'}}}