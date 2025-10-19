```json
{
  "id": "619efae33f7be332",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290665,
  "host_pid": "9e6742732c60:1",
  "hash": "3bf7260dee45a017a496786bd808ec550e80b2c3049616bdbe73859c90351ce1",
  "cid": "QmV13bf7260dee45a017a496786bd808ec550e80b2c3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290665,
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
      "evaluated_at": 1760290665
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
  "sig": "c81bdef966c6f9043a29fd9edbf70ace76fc3a77996c64cd4abcec0d5d34c7c0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462495850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 40852812, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285763, 'matching_hash': '1976ee1fa1c7bc70'}}}