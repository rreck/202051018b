```json
{
  "id": "1699e3596f817a20",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291452,
  "host_pid": "9e6742732c60:1",
  "hash": "ab1b232dc10ad8f53e922693bd89f4ce3fa20b38a673d0a0a9aa77cb0f119cd4",
  "cid": "QmV1ab1b232dc10ad8f53e922693bd89f4ce3fa20b38",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291452,
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
      "evaluated_at": 1760291452
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
  "sig": "1b9bf5d6bfba4ec74380ca95de61842d650af750c722aca326baa1fc24616bd7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460464182
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 18485075, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285765, 'matching_hash': '97f231b14306ced8'}}}