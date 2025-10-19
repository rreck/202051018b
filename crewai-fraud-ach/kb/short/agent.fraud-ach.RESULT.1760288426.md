```json
{
  "id": "942afa249549ec81",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288426,
  "host_pid": "9e6742732c60:1",
  "hash": "74da3b42c5e5c20cd772299d5a74b6886f337b9ec2de0d39d17cd3b488649078",
  "cid": "QmV174da3b42c5e5c20cd772299d5a74b6886f337b9e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288426,
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
      "evaluated_at": 1760288426
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
  "sig": "b54176a69fe1aa67b1f4056199e94490312a3e14e998c5d4993586cba8e29e23"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021988031
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 93, 'threshold': 50, 'total_amount': 23516631, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 92, 'first_seen': 1760285764, 'matching_hash': '88465ad333807d91'}}}