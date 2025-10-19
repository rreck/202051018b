```json
{
  "id": "c2621c0113b631fb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294454,
  "host_pid": "9e6742732c60:1",
  "hash": "c1d1be535c5573757c81214da4e8588616b1f39c244a3d0ae34630bf0caf18b4",
  "cid": "QmV1c1d1be535c5573757c81214da4e8588616b1f39c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294454,
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
      "evaluated_at": 1760294454
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
  "sig": "83761c4d9e106fec9ab70b5c55a410fb7aaff180ce81345a63244501044b633c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245808112
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 238, 'threshold': 50, 'total_amount': 74003720, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 237, 'first_seen': 1760285765, 'matching_hash': 'd8dffc30f620e6a0'}}}