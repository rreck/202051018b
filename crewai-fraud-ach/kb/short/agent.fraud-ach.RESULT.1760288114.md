```json
{
  "id": "45429afbb3881356",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288114,
  "host_pid": "9e6742732c60:1",
  "hash": "91c54ecf40c76f8ef182d4b9d3d3efeef8ab1eddfe53906b1dc7e01847dfba57",
  "cid": "QmV191c54ecf40c76f8ef182d4b9d3d3efeef8ab1edd",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288114,
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
      "evaluated_at": 1760288114
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
  "sig": "93e4481f4fef169f76c6f3352877a5071ab64d77adc9d68d0de8970bd6249e0f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244430877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 83, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 82, 'first_seen': 1760285763, 'matching_hash': 'c92664da58a26885'}}}een': 1760285764, 'matching_hash': '79d45ba49f6b4a46'}}}