```json
{
  "id": "a565488af6dc4daa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288652,
  "host_pid": "9e6742732c60:1",
  "hash": "177fcd0bd9de95504187d741a060426b174e8faf223f01c5d042a33009dfac3d",
  "cid": "QmV1177fcd0bd9de95504187d741a060426b174e8faf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288652,
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
      "evaluated_at": 1760288652
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
  "sig": "d29eb1d6f85b76357ba173526485fe57779ec3faab6024ac3fc84132c945738a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027005922
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 100, 'threshold': 50, 'total_amount': 28658800, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 99, 'first_seen': 1760285763, 'matching_hash': '8fe7ed8865cd9a2a'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5035466}}}