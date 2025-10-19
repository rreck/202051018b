```json
{
  "id": "4dd7ffcea40a106e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289788,
  "host_pid": "9e6742732c60:1",
  "hash": "9a55839c7417f8dd329912f93d580f3d4467221db3ab2bc877fe38e2eb3e89c9",
  "cid": "QmV19a55839c7417f8dd329912f93d580f3d4467221d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289788,
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
      "evaluated_at": 1760289788
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
  "sig": "d4a30586a0c14d287601b09df67a8c4e6e2325c7eda24ca5f364b81e4f422133"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150046055
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50, 'total_amount': 52279507, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285764, 'matching_hash': 'b44312efb353b904'}}}