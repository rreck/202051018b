```json
{
  "id": "f722c9a27f48a68e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294267,
  "host_pid": "9e6742732c60:1",
  "hash": "a8554fd15f2538be7e6435189fa737e6c58ab5d00b4d38acb15b0905b7f6396b",
  "cid": "QmV1a8554fd15f2538be7e6435189fa737e6c58ab5d0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294267,
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
      "evaluated_at": 1760294267
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
  "sig": "f7c1c6ec03a2572daee24c4d0440adef15decf0e5c90743b113d48d319643566"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038829903
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 18319660, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': 'dff748e22041369e'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '580123066', 'validation_error': 'Invalid routing number checksum'}}}