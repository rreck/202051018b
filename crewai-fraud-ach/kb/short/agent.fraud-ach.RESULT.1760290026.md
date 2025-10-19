```json
{
  "id": "3993ea5afd7e2798",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290026,
  "host_pid": "9e6742732c60:1",
  "hash": "26d4ae279539306c9fdf16755f44dbfa886a24040094099c16f2fcce4c8fcf85",
  "cid": "QmV126d4ae279539306c9fdf16755f44dbfa886a2404",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290026,
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
      "evaluated_at": 1760290026
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
  "sig": "e244f67058ee3f72ca76ac301ba3676167ba18539076b844a202879ba814ae55"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022117413
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 139, 'threshold': 50, 'total_amount': 34213738, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 138, 'first_seen': 1760285765, 'matching_hash': 'c7f16f3a9aa8490f'}}}