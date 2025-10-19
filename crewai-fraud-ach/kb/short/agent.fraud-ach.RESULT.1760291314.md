```json
{
  "id": "dde407f37c7a8344",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291314,
  "host_pid": "9e6742732c60:1",
  "hash": "c202c7a59225ea020d724442b3b16b7de958005e968018565a7f1af92b5034af",
  "cid": "QmV1c202c7a59225ea020d724442b3b16b7de958005e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291314,
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
      "evaluated_at": 1760291314
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
  "sig": "92d1a15035bf8894721b999130e0001a80eba703905e8ebec07728c2c2441bcd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278925206
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 42902304, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': 'f9778a1b3fb70950'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}