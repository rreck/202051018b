```json
{
  "id": "e6e8a70fdb491ab0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291018,
  "host_pid": "9e6742732c60:1",
  "hash": "761f3aadb3cd6658d9ced40b1c9af686c994435297034a5e04e7d577f7420da8",
  "cid": "QmV1761f3aadb3cd6658d9ced40b1c9af686c9944352",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291018,
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
      "evaluated_at": 1760291018
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "565b3eb78d7e788ae646d9ecaa79005bb716fe0b15507ba0b7085ec41707d547"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 060557484693193
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 70688145, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285763, 'matching_hash': 'db8aeeee2135ece1'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '060557489', 'validation_error': 'Invalid routing number checksum'}}}