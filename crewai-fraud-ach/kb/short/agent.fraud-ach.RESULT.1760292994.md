```json
{
  "id": "2e2978625fef7c87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292994,
  "host_pid": "9e6742732c60:1",
  "hash": "f37bd971a8aab67b4e3e5d44513fd3344bbc56bdb6a72977b474c0bff522dc75",
  "cid": "QmV1f37bd971a8aab67b4e3e5d44513fd3344bbc56bd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292994,
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
      "evaluated_at": 1760292994
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
  "sig": "fa95688b34444a8eb36c867b12d2bfc5356a87aecb96d9e0391a293bbc1b0122"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157031776
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 48487791, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': '2e79bf0e4633df5f'}}}