```json
{
  "id": "6880fe8c68e6ee2e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288923,
  "host_pid": "9e6742732c60:1",
  "hash": "83f04fa4626698ecea8f036af19869782dbc9b195b52406c40fb5dcbf4b73509",
  "cid": "QmV183f04fa4626698ecea8f036af19869782dbc9b19",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288923,
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
      "evaluated_at": 1760288923
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
  "sig": "d84236ed8aa1a1151e98212fb12f85f61a7e74e66cd015476ea8f481af6e4cc8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462495850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 28282716, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285763, 'matching_hash': '1976ee1fa1c7bc70'}}}