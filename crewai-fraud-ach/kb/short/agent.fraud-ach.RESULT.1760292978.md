```json
{
  "id": "be51a9ab3ba00d7f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292978,
  "host_pid": "9e6742732c60:1",
  "hash": "bf72d91e71592fb159f5514727a198d057238125683cb6f2825d117cdaf12ea2",
  "cid": "QmV1bf72d91e71592fb159f5514727a198d057238125",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292978,
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
      "evaluated_at": 1760292978
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
  "sig": "221701c1769f817b35b4f12e874e3a3219d123256cf852e7721b76b130271f6c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201463677078
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 10450000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': '2c78ec7dacd934fb'}}}