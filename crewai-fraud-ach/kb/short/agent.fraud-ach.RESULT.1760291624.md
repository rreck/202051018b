```json
{
  "id": "5d231b59e55d634d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291624,
  "host_pid": "9e6742732c60:1",
  "hash": "13317cdbd1b5f4adc5c5b43ffaf406e48889302aa0a312e68de5d4810928eaf6",
  "cid": "QmV113317cdbd1b5f4adc5c5b43ffaf406e48889302a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291624,
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
      "evaluated_at": 1760291624
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
  "sig": "ed496851c8f2169684c60eb1a19789d0f23c43562fdb7cd03c273f81f036c8d9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596807926
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 58767132, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': 'efb59c040be3d116'}}}