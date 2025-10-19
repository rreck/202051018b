```json
{
  "id": "cfbd868f98801171",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290192,
  "host_pid": "9e6742732c60:1",
  "hash": "9861675a0864d526f836d09961797f5323c7a3f7f4d76a6f78d9d240b159d3e5",
  "cid": "QmV19861675a0864d526f836d09961797f5323c7a3f7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290192,
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
      "evaluated_at": 1760290192
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
  "sig": "05f81f6b49a658d4e75d86c54c25cfc270c68833841b5b5f730404dc7f0fa2b1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249881393
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 58266000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285763, 'matching_hash': '72e20928773d23d6'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '349235113', 'validation_error': 'Invalid routing number checksum'}}}