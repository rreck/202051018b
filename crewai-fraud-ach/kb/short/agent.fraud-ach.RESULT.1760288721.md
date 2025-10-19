```json
{
  "id": "898d6a62f8bc50dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288721,
  "host_pid": "9e6742732c60:1",
  "hash": "e116a53e55257617cd792c509c83e5b501f89a0704998386282cf1fcb62e27e0",
  "cid": "QmV1e116a53e55257617cd792c509c83e5b501f89a07",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288721,
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
      "evaluated_at": 1760288721
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
  "sig": "2ea530b08d41d70b6efe8e1c2e1e498518cba7b2c1d19a435680343b3e7452e1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024843981
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 15044184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285764, 'matching_hash': 'a5434e6981d8724b'}}}