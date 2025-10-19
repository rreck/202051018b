```json
{
  "id": "92f75e96498ce56c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286213,
  "host_pid": "9e6742732c60:1",
  "hash": "8731a06d24fe6c40db5e96502490976dcdf7a0362a89374409b3e32575038a2e",
  "cid": "QmV18731a06d24fe6c40db5e96502490976dcdf7a036",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286213,
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
      "evaluated_at": 1760286213
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
  "sig": "7ec880088e0aee29f337dae62ee6a2d8bbb956dae45f7293e1eb92f589810b81"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201462495850
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 17, 'first_seen': 1760285763, 'matching_hash': '1976ee1fa1c7bc70'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '053611749', 'validation_error': 'Invalid routing number checksum'}}}