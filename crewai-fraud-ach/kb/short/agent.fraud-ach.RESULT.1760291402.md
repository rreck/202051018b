```json
{
  "id": "9eec5a1a44bf8e76",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291402,
  "host_pid": "9e6742732c60:1",
  "hash": "066c8952d4182139a127534d33f9196be1e9e5f5213ae0ae2014520f8976a032",
  "cid": "QmV1066c8952d4182139a127534d33f9196be1e9e5f5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291402,
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
      "evaluated_at": 1760291402
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
  "sig": "050751b141e5afda17b7eab7c15d2bb286ec9a131bf2edec670a223ab6a43aa0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027363246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 174, 'threshold': 50, 'total_amount': 20158944, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 173, 'first_seen': 1760285764, 'matching_hash': 'ed45becb5b65c89d'}}}