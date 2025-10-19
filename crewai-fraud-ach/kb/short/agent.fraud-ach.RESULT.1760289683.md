```json
{
  "id": "f0eaf29525c14a50",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289683,
  "host_pid": "9e6742732c60:1",
  "hash": "218943ed19422f58d011364295e4d384346d17efd201b519bc3fa9139e51d93e",
  "cid": "QmV1218943ed19422f58d011364295e4d384346d17ef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289683,
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
      "evaluated_at": 1760289683
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
  "sig": "d88b473320304423681b0f0b26044a23a9088688c11106477d33991fb704c24d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248226164
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 37898640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285763, 'matching_hash': 'b7846971abb7164d'}}}