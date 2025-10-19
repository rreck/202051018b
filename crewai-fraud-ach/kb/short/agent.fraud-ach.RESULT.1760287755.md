```json
{
  "id": "acd62a9352f78ce9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287755,
  "host_pid": "9e6742732c60:1",
  "hash": "dd6ebb46d24c2415342581a6f9253f6ac8e10228667cff076fae33f520c1c1f7",
  "cid": "QmV1dd6ebb46d24c2415342581a6f9253f6ac8e10228",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287755,
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
      "evaluated_at": 1760287755
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
  "sig": "29f4b09dc539e5898fa5c8fb9c4f59e6a54eeacd870feb0a49dbe42032b4a517"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 026009594711181
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50, 'total_amount': 10367420, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285765, 'matching_hash': '37ffc636e48dfc6b'}}}