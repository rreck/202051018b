```json
{
  "id": "dc6b6b5516b6ad2f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287125,
  "host_pid": "9e6742732c60:1",
  "hash": "f22295d6c1835f20e4047ced1e6d34a23331d61846313630db79f687abd45e4b",
  "cid": "QmV1f22295d6c1835f20e4047ced1e6d34a23331d618",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287125,
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
      "evaluated_at": 1760287125
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "d91fcdf28823595cc69a180f06f15946465dbdbb4d6563c0904982bc93b89472"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 026009594139699
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 22644125, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285763, 'matching_hash': '7ab15b33947f4722'}}}g': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '164661952', 'validation_error': 'Invalid routing number checksum'}}}