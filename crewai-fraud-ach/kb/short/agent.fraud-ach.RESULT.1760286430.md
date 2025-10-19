```json
{
  "id": "1ee8efa2125ccec6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286430,
  "host_pid": "9e6742732c60:1",
  "hash": "2b030d6926cd433463b3e3b85114d36e1a64f57feded6ba5174a4c81d0c3e9dd",
  "cid": "QmV12b030d6926cd433463b3e3b85114d36e1a64f57f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286430,
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
      "evaluated_at": 1760286430
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
  "sig": "fca7510f055401dbbf34fb6e3e0fa205849d32be0b36ddb5da9788d8c96044c8"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009592616863
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285764, 'matching_hash': '1f69fcd8882944a6'}}}ue, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285763, 'matching_hash': '8c09836a51c1ceac'}}}760284979, 'matching_hash': '9c963f39e9fb9122'}}}