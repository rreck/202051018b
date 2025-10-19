```json
{
  "id": "a1275ab9235189f2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294813,
  "host_pid": "9e6742732c60:1",
  "hash": "c3263ddd191c84114cc84c8c41f1f6e82f896f504954d4cd798510209bf86d5a",
  "cid": "QmV1c3263ddd191c84114cc84c8c41f1f6e82f896f50",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294813,
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
      "evaluated_at": 1760294813
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
  "sig": "75d8b80a3ebe9213dce16ab357fc841e857202055114d1bcc47fbf32504adceb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024926087
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 103571300, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': '726e20d3efcb42e0'}}}