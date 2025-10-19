```json
{
  "id": "cd83d76a5bb8851b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293925,
  "host_pid": "9e6742732c60:1",
  "hash": "591418b6147da5e4a6efd23e99a39a52396c426d2cec4e7f2cc3dfdd8f8fd7c9",
  "cid": "QmV1591418b6147da5e4a6efd23e99a39a52396c426d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293925,
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
      "evaluated_at": 1760293925
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
  "sig": "9a15eb9edcad20006e2734896af939bf6097645b5dbf62648f779bf6e64e3a81"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463621906
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 228, 'threshold': 50, 'total_amount': 77095008, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 227, 'first_seen': 1760285763, 'matching_hash': 'c1b23d91813533f7'}}}