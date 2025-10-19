```json
{
  "id": "8307fba663e4c156",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289797,
  "host_pid": "9e6742732c60:1",
  "hash": "4e5a45298be9866c3a2b42e156ebac09c8e3a009fe8bc73c023631bbb0f030ce",
  "cid": "QmV14e5a45298be9866c3a2b42e156ebac09c8e3a009",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289797,
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
      "evaluated_at": 1760289797
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
  "sig": "3e18918cb91962dec2fdd8f09638d11eb96d40977205e670838abd8331a17280"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153385568
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 133, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 132, 'first_seen': 1760285763, 'matching_hash': '556aff2bced704f0'}}}