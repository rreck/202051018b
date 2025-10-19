```json
{
  "id": "983aee62ce2ae443",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288154,
  "host_pid": "9e6742732c60:1",
  "hash": "e92ae3271ff39e69eb8c6553c8ce31feb10da571a2990acd9c089b878767540d",
  "cid": "QmV1e92ae3271ff39e69eb8c6553c8ce31feb10da571",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288154,
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
      "evaluated_at": 1760288154
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
  "sig": "3713242f6159228436d6dbeae0d986262db6bc2c24b5bd34869c9378a53d0d1e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245911336
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 41814024, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285765, 'matching_hash': '6e0081c3975eda61'}}}