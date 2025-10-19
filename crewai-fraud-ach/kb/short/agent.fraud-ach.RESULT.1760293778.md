```json
{
  "id": "2d3db30de70afdc5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293778,
  "host_pid": "9e6742732c60:1",
  "hash": "d6bc29b401441fc6544d29adf531d9b9e3c1ae9200e6c9e3c2f49886a64015c4",
  "cid": "QmV1d6bc29b401441fc6544d29adf531d9b9e3c1ae92",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293778,
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
      "evaluated_at": 1760293778
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
  "sig": "93ea40ad7cbdce023a9eb30203267f2ef4f72e72647f9a6e313732511c86670b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464550835
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 42127200, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': '50cb0ee46794e046'}}}