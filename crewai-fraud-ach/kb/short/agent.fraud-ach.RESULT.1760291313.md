```json
{
  "id": "541676bb7a891973",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291313,
  "host_pid": "9e6742732c60:1",
  "hash": "be31fbd7814d396422cf6fc61707445aa2d1b25730ff6e5fc7a8d8003bb4a6c3",
  "cid": "QmV1be31fbd7814d396422cf6fc61707445aa2d1b257",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291313,
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
      "evaluated_at": 1760291313
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
  "sig": "f418b67bb7c2d434cf8fa172875823397398b632a4c7cff67517a64baf578ffc"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462772191
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 35227148, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': '3cc4f4a3442921e3'}}}