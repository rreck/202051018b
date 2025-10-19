```json
{
  "id": "7206c60beae70780",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294762,
  "host_pid": "9e6742732c60:1",
  "hash": "cd40c3e735fa0cd36884f02ba8ed3be4c02711c507195e57d66b6f28575f569f",
  "cid": "QmV1cd40c3e735fa0cd36884f02ba8ed3be4c02711c5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294762,
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
      "evaluated_at": 1760294762
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
  "sig": "26b91e10e010a13a648255ddd4cc5c204088e52e58884dcfa3e89e862cea9653"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274968720
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 244, 'threshold': 50, 'total_amount': 91044696, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 243, 'first_seen': 1760285763, 'matching_hash': '69fe72c937d65071'}}}