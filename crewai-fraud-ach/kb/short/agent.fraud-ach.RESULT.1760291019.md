```json
{
  "id": "2055fb76c6d8ab6d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291019,
  "host_pid": "9e6742732c60:1",
  "hash": "1dcbacfb57f87f56527f37c19435138c1f58c1deab5a2edf594132b6b7bdb2be",
  "cid": "QmV11dcbacfb57f87f56527f37c19435138c1f58c1de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291019,
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
      "evaluated_at": 1760291019
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
  "sig": "80d2a4a06b7ce870d03ee501c9113a157f1100ab7299c43b201b85e4d86c4c1d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030505524
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 74162715, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285764, 'matching_hash': '58071665864a5dbb'}}}