```json
{
  "id": "77df30e131ad4424",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294554,
  "host_pid": "9e6742732c60:1",
  "hash": "2a91a72b4348483e187d8e470cae8a8ff02eaa804b6ff8ce69f0afc63bb3c3f4",
  "cid": "QmV12a91a72b4348483e187d8e470cae8a8ff02eaa80",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294554,
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
      "evaluated_at": 1760294554
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
  "sig": "dc9c271535856b008b719ac83f6d4143d82fd864f7611194f873819847ee2f57"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028850671
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 22813920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': '07a264c4d7b66912'}}}