```json
{
  "id": "dfa1102839ea31bb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288628,
  "host_pid": "9e6742732c60:1",
  "hash": "5a7680637a252c538c4a386eb25899ff8afd0364129eb7b0fe1afbfe6a0bfb07",
  "cid": "QmV15a7680637a252c538c4a386eb25899ff8afd0364",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288628,
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
      "evaluated_at": 1760288628
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
  "sig": "ebfbf7432c5987943cee48adb753efdfd438eb482b6ad920ce303c7263bd1b0d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152914121
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 99, 'threshold': 50, 'total_amount': 37014615, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 98, 'first_seen': 1760285763, 'matching_hash': 'c85c50a0151bc705'}}}