```json
{
  "id": "366d4eee595be371",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288404,
  "host_pid": "9e6742732c60:1",
  "hash": "ba8bd6d8270fc9f786c8cfd17cfc6989a3e6649c2d28ce1ce567a7b5683c5ab2",
  "cid": "QmV1ba8bd6d8270fc9f786c8cfd17cfc6989a3e6649c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288404,
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
      "evaluated_at": 1760288404
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
  "sig": "247d2935fcc7802855ac35e86ace597c020c3c9c73b762b5a92d7b7ee4c89cde"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594283807
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 18544532, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285764, 'matching_hash': 'e41bbca7fc0ba663'}}}