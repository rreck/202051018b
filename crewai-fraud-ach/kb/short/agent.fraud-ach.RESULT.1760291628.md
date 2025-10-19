```json
{
  "id": "982303c60db5a54d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291628,
  "host_pid": "9e6742732c60:1",
  "hash": "6eadc30e15ad2e749fce7ea3ab1688779f0482c77950c49a4cb488c23d1fe388",
  "cid": "QmV16eadc30e15ad2e749fce7ea3ab1688779f0482c7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291628,
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
      "evaluated_at": 1760291628
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
  "sig": "f42caae6ced968771ed1fd6e20981cf53a5e26f7f1defd9f339e791e8cd7568a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275697869
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 37774370, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285764, 'matching_hash': '6e45970a6bf10306'}}}