```json
{
  "id": "f2fc109a8e2a6f81",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288927,
  "host_pid": "9e6742732c60:1",
  "hash": "be90f4280ae6a653e1be9f463bb273edc674d66bd72924aed26b8089841fdd3b",
  "cid": "QmV1be90f4280ae6a653e1be9f463bb273edc674d66b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288927,
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
      "evaluated_at": 1760288927
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
  "sig": "f8a49a9b8dfb0acab7ebb36b98b86f9d79c196fed43f05b0f718dece92cab5d2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271369125
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 16724772, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285763, 'matching_hash': 'b975113295de86ab'}}}