```json
{
  "id": "c663cd54fd6c0898",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292879,
  "host_pid": "9e6742732c60:1",
  "hash": "a972e703bb8e839e6136b0e816662a43df79dd7862119fe187b53a2ceedef52e",
  "cid": "QmV1a972e703bb8e839e6136b0e816662a43df79dd78",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292879,
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
      "evaluated_at": 1760292879
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
  "sig": "55b23c1beaf3c6fa31e41f838e65e95a1a4289fb061f80a7909171a45294c0a1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024298856
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 70647030, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': 'c651031c314af1fc'}}}