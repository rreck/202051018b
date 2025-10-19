```json
{
  "id": "827a1c1ec64ef96e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294896,
  "host_pid": "9e6742732c60:1",
  "hash": "e3067f4543a4b1bef9f696c92b2994023e6f82e659ba3407799884a1b608f1e0",
  "cid": "QmV1e3067f4543a4b1bef9f696c92b2994023e6f82e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294896,
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
      "evaluated_at": 1760294896
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
  "sig": "71e943c25d05f78819ab11c1dfdc962b86815db9a4e99b1fc0ed5ef94f0c1713"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599118273
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 31970652, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285765, 'matching_hash': '777fe2ef7ab8cdc9'}}}