```json
{
  "id": "aa2b993c4579736d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285870,
  "host_pid": "9e6742732c60:1",
  "hash": "432a8553ba5a0f80649b656fa740c1f6efd265d1d379d3eeb8829d8150e9cac2",
  "cid": "QmV1432a8553ba5a0f80649b656fa740c1f6efd265d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285870,
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
      "evaluated_at": 1760285870
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
  "sig": "7b0edecdc2cfe52e43a7dbad602d8cf53cedda65ff4546fd57a177058d9a1b61"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460216158
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 21652756, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760284979, 'matching_hash': 'd03ac62e4cd65436'}}}