```json
{
  "id": "4d32cc099054ccb5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291105,
  "host_pid": "9e6742732c60:1",
  "hash": "a5d886dd5ee9b7f672a533130d915707110f7d05b33cc97f39c4340598e81efa",
  "cid": "QmV1a5d886dd5ee9b7f672a533130d915707110f7d05",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291105,
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
      "evaluated_at": 1760291105
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
  "sig": "0fc827ed9b3e6768f65d649bde28099f44b7842b5a8d74df465fa944a0126030"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031287652
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 46271859, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285763, 'matching_hash': 'd2d8cdbc9df50106'}}}