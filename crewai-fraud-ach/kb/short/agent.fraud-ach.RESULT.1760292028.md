```json
{
  "id": "8e6e1ab758481aa0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292028,
  "host_pid": "9e6742732c60:1",
  "hash": "dee12ddb7643df2b2eccc8abcf4b1d52fd645989716030b8807d2778db642ac1",
  "cid": "QmV1dee12ddb7643df2b2eccc8abcf4b1d52fd645989",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292028,
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
      "evaluated_at": 1760292028
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
  "sig": "1df61aa7c0fe4a3ddf94e44c020f3dcbb8d437cac13c0b48c3e1ff2f140f0695"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 188, 'threshold': 50, 'total_amount': 59830624, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 187, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}