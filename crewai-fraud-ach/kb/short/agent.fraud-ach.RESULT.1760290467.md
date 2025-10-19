```json
{
  "id": "48e1a931455ee4e8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290467,
  "host_pid": "9e6742732c60:1",
  "hash": "535c78dbe1963ca188a381857b77c2d0f869f70781f68d3483bd3b4bcadd71b6",
  "cid": "QmV1535c78dbe1963ca188a381857b77c2d0f869f707",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290467,
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
      "evaluated_at": 1760290467
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
  "sig": "c39577a7e396c0e636bd6b8bff59d97c2dd4c80ef6f19a5cd21e9ab29f35bd88"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596636125
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 67237582, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285763, 'matching_hash': 'de29ac64387e8e3f'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '607486349', 'validation_error': 'Invalid routing number checksum'}}}