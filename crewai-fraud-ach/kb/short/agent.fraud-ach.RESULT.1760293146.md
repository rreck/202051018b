```json
{
  "id": "24882b309cd79ddb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293146,
  "host_pid": "9e6742732c60:1",
  "hash": "aa190911a69a0a8de08f9dbc53c02c95c95cad4b588e3ae0c6ddf5e65294d933",
  "cid": "QmV1aa190911a69a0a8de08f9dbc53c02c95c95cad4b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293146,
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
      "evaluated_at": 1760293146
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
  "sig": "959f6749182e519c7e420a0594aa8a48e922b7e63f58292723f9ca7aedddd108"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465368597
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 52732456, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285765, 'matching_hash': 'f57f84d557436d23'}}}