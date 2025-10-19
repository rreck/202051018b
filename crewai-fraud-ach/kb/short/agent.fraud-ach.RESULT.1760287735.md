```json
{
  "id": "8a8b6413f0cb9fb1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287735,
  "host_pid": "9e6742732c60:1",
  "hash": "ccb8e40af868fd8d9910b3cef9d2fd10ae6ce566d1b410809fc99b00ee710d78",
  "cid": "QmV1ccb8e40af868fd8d9910b3cef9d2fd10ae6ce566",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287735,
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
      "evaluated_at": 1760287735
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
  "sig": "b156a03ae0e31930e44808ec2587879179cd92a6ce71bddc62ab7a966921a0d7"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 22277360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}