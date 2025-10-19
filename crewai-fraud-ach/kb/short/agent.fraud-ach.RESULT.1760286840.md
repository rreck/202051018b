```json
{
  "id": "f8ced39327ee7f7f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286840,
  "host_pid": "9e6742732c60:1",
  "hash": "6eec93f2d4bd31266e5338952784e71093c08ef0eed272d2a660e766417973ac",
  "cid": "QmV16eec93f2d4bd31266e5338952784e71093c08ef0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286840,
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
      "evaluated_at": 1760286840
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
  "sig": "2ae2c3f9212eddd88978f40edde85a4e5a0a987d06e90b416837543813197939"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000028559782
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760285763, 'matching_hash': '551fe21bbee5d648'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '118929079', 'validation_error': 'Invalid routing number checksum'}}}