```json
{
  "id": "d404cad1599ad6f8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288002,
  "host_pid": "9e6742732c60:1",
  "hash": "2575357964926c1c136096638a5aed1497cf5738f970fe20920e2d6a7cee1213",
  "cid": "QmV12575357964926c1c136096638a5aed1497cf5738",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288002,
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
      "evaluated_at": 1760288002
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
  "sig": "b8fc07b6da78f6539a93e6cca42f9d31a5ebd9cc962fb4c11f6345631b720b38"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157659459
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 79, 'threshold': 50, 'total_amount': 28748969, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 78, 'first_seen': 1760285765, 'matching_hash': 'b2c549e42e296c8f'}}}