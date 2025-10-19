```json
{
  "id": "d5bb4697dfe2ebfb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294017,
  "host_pid": "9e6742732c60:1",
  "hash": "3752525f2de25af7b302b98e7b8f8d2a24f2b6149490206d758365f5f709eb35",
  "cid": "QmV13752525f2de25af7b302b98e7b8f8d2a24f2b614",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294017,
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
      "evaluated_at": 1760294017
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
  "sig": "71c15b3103bcd121d098dfbd426e5e5762f844a9c5124dc3dbbc88d9f6c93838"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463891034
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 47667270, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '2167bcd96d131e8f'}}}