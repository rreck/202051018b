```json
{
  "id": "2ab2cf7de1a9d723",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293099,
  "host_pid": "9e6742732c60:1",
  "hash": "e468e9196fb39337745aaa4159d8d7cafa7f3ce2225b278aa0321e46ee154c50",
  "cid": "QmV1e468e9196fb39337745aaa4159d8d7cafa7f3ce2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293099,
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
      "evaluated_at": 1760293099
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
  "sig": "71d25f9c1d42d11a704bf4d211e9ea060e5b3ef0f96191dbf8744932b12b483a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025824799
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 54913172, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285765, 'matching_hash': 'f20c8e7a7a7e0174'}}}