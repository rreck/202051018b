```json
{
  "id": "eb70246bbce9ffb0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291762,
  "host_pid": "9e6742732c60:1",
  "hash": "bf8aeb2a20b70b89fb7585a3bad05450053f2ee7f75545a2bcc09f561bcf32cc",
  "cid": "QmV1bf8aeb2a20b70b89fb7585a3bad05450053f2ee7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291762,
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
      "evaluated_at": 1760291762
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
  "sig": "3141f7c255b03bc59e74f55d81f8c2137dcd5d8cc9cfac6cfbb7aa3384be2c2a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021517830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 182, 'threshold': 50, 'total_amount': 54178306, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 181, 'first_seen': 1760285765, 'matching_hash': '323b6ce2946b0561'}}}