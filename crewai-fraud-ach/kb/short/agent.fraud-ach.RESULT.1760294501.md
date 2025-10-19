```json
{
  "id": "9656448c421b8a12",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294501,
  "host_pid": "9e6742732c60:1",
  "hash": "ee0718f6aba4265d8b4728399de48ecb028da7a67c7f7310ba60e2049c244e11",
  "cid": "QmV1ee0718f6aba4265d8b4728399de48ecb028da7a6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294501,
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
      "evaluated_at": 1760294501
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
  "sig": "04ce32d2e58cfc5b4c505e5e38e7c323e21021ce4c94c336662b2205d054fa0f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105150540393
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 239, 'threshold': 50, 'total_amount': 53940866, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 238, 'first_seen': 1760285763, 'matching_hash': '5c99a38661a1ddcd'}}}