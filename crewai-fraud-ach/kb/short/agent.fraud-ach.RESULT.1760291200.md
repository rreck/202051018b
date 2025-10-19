```json
{
  "id": "4d583d3a3cd7cd6b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291200,
  "host_pid": "9e6742732c60:1",
  "hash": "f6a5429b7e7acb1a3ba0f1645a89d97eda54ee87b08405f9b8a362e1a7285070",
  "cid": "QmV1f6a5429b7e7acb1a3ba0f1645a89d97eda54ee87",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291200,
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
      "evaluated_at": 1760291200
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
  "sig": "f697bf5fecc1e0181dfb39ebf1250af9fcd786a50aa716dc2bfcd4cc8320d22a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201462554282
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285763, 'matching_hash': '2083692f538c0312'}}}