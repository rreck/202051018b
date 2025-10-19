```json
{
  "id": "1d915b9a6f03ab62",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292806,
  "host_pid": "9e6742732c60:1",
  "hash": "c150e9c5ce3aa310506625a2e60acff842acfddb139597d0cb1844756b15b906",
  "cid": "QmV1c150e9c5ce3aa310506625a2e60acff842acfddb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292806,
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
      "evaluated_at": 1760292806
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
  "sig": "5f35ff3f488a05f18edaec7811d7cc97dfb83c435618ec2aec4076da5243111f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039663431
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 30529215, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285764, 'matching_hash': '33f644fe289ea89d'}}}