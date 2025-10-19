```json
{
  "id": "f70c20398a89d5fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294082,
  "host_pid": "9e6742732c60:1",
  "hash": "17b6076ddb64571600d9218a118d1810d24ca781a8c3c7369713f6838e9a55cf",
  "cid": "QmV117b6076ddb64571600d9218a118d1810d24ca781",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294082,
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
      "evaluated_at": 1760294082
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
  "sig": "32edfc44eb178f7e8ddb7264803925aed242c7830187a8742c5dc9b515230fa6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152345106
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 107161824, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285764, 'matching_hash': '244a38e8c31df032'}}}