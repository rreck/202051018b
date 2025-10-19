```json
{
  "id": "9745c0ace23b0db6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292475,
  "host_pid": "9e6742732c60:1",
  "hash": "4a397701a52afe7d94ab5d8f00e3f67e20beb8061471c9be27102fcb8aae70e8",
  "cid": "QmV14a397701a52afe7d94ab5d8f00e3f67e20beb806",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292475,
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
      "evaluated_at": 1760292475
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
  "sig": "3dcf1f0c6d90760b1fd78638124f8700755b8d9e1b9b7742eea30adc35f27b88"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000023966417
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 90059112, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285764, 'matching_hash': 'bf59b19c5a8c3ed8'}}}