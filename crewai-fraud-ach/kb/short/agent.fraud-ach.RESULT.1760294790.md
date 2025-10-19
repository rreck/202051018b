```json
{
  "id": "6b46ec3c28e6eebe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294790,
  "host_pid": "9e6742732c60:1",
  "hash": "98d30c224e9c9e90a5555f56b6e7f4f43bbcd0fddc8a914dbc89edf4f2f13147",
  "cid": "QmV198d30c224e9c9e90a5555f56b6e7f4f43bbcd0fd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294790,
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
      "evaluated_at": 1760294790
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
  "sig": "ec010361dccb876b5caa02d17cb20f859d68b12d976721df1096f44db54553bb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028263855
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 61000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285765, 'matching_hash': 'de539bef65b21552'}}}