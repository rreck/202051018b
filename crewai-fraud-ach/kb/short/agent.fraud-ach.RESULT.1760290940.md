```json
{
  "id": "c5028972c7aecc6e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290940,
  "host_pid": "9e6742732c60:1",
  "hash": "4c10c40330702904ea5363a2965e2383baf1086c95f09f7ab9483a2fda2c0e94",
  "cid": "QmV14c10c40330702904ea5363a2965e2383baf1086c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290940,
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
      "evaluated_at": 1760290940
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
  "sig": "8fc1c2b5e02400ab14705d84d25f526d7c04535e882de992c78540794bd9ad44"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037446147
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 163, 'threshold': 50, 'total_amount': 79529982, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 162, 'first_seen': 1760285763, 'matching_hash': '66d102d4303d651c'}}}