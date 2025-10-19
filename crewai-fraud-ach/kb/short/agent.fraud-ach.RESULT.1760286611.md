```json
{
  "id": "c7c772fb2a0d2c76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286611,
  "host_pid": "9e6742732c60:1",
  "hash": "b4cbbc92ac77d78dd8e6dd29b45fec1e4e984a27d5900b4a1755039de1154235",
  "cid": "QmV1b4cbbc92ac77d78dd8e6dd29b45fec1e4e984a27",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286611,
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
      "evaluated_at": 1760286611
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
  "sig": "598b8f02cb1da9d2b0a741026fbff7e448a2c6c05d62cdfd99b98d44c05addab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246878582
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 107, 'threshold': 50, 'total_amount': 29185320, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 106, 'first_seen': 1760284979, 'matching_hash': '3e968f91ba41b0b5'}}}