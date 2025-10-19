```json
{
  "id": "e7a7c7ed9ee226a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294833,
  "host_pid": "9e6742732c60:1",
  "hash": "0163ef2b859d7a3f668e2456775f5d86f300df76355f237301c394a8de6c5246",
  "cid": "QmV10163ef2b859d7a3f668e2456775f5d86f300df76",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294833,
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
      "evaluated_at": 1760294833
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
  "sig": "de8ecc83290f36c2afb42dd96bb6b9d9c6fb05f57ea55ac6d69d891bff1de391"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276148173
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 69260275, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285765, 'matching_hash': 'f15677eba424e05f'}}}