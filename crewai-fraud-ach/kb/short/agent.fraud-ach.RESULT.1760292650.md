```json
{
  "id": "fbe368a7f269b891",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292650,
  "host_pid": "9e6742732c60:1",
  "hash": "5fe192a0ea8bb171ee6c3c1424e32894a96d8027141c228f0ea31bffb89d154f",
  "cid": "QmV15fe192a0ea8bb171ee6c3c1424e32894a96d8027",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292650,
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
      "evaluated_at": 1760292650
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
  "sig": "94e2f499d9f93335386c11decb5f9c8dbcc9c8e8e9510d2f97499a15293e6404"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153734827
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 202, 'threshold': 50, 'total_amount': 99675890, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 201, 'first_seen': 1760285764, 'matching_hash': 'f575a9f929aab221'}}}