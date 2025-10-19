```json
{
  "id": "3a4063295b1dc249",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294831,
  "host_pid": "9e6742732c60:1",
  "hash": "4c69229f258d7c72689eef4a63c26d3bff20e82060ea01eb5394b83836848363",
  "cid": "QmV14c69229f258d7c72689eef4a63c26d3bff20e820",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294831,
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
      "evaluated_at": 1760294831
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
  "sig": "a903e524bf16ef78b44e15976518441c9820386b9f77fb659e733e0f94537387"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154102308
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 321, 'threshold': 50, 'total_amount': 118265067, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 320, 'first_seen': 1760284979, 'matching_hash': '687d8a253912c530'}}}