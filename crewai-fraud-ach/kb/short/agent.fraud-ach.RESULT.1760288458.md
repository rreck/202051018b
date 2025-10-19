```json
{
  "id": "0afd7005f2abd07b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288458,
  "host_pid": "9e6742732c60:1",
  "hash": "a0ff7f9dc58c814ddb25b6f214a778ce19eac8e6c0fb83ff350019dd67462da0",
  "cid": "QmV1a0ff7f9dc58c814ddb25b6f214a778ce19eac8e6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288458,
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
      "evaluated_at": 1760288458
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
  "sig": "8c780d11380c040c775ef43e4c9cba593ec2a76cd841cd63383c21666e23d7bd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009597385398
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 94, 'threshold': 50, 'total_amount': 22966738, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 93, 'first_seen': 1760285763, 'matching_hash': '354842811986f77e'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '824845890', 'validation_error': 'Invalid routing number checksum'}}}