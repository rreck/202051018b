```json
{
  "id": "3409c60279a63d43",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291606,
  "host_pid": "9e6742732c60:1",
  "hash": "dc2b74dff3d792fab5e34d443d75388e8238bf7083564f5a1638b6276f3cc994",
  "cid": "QmV1dc2b74dff3d792fab5e34d443d75388e8238bf70",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291606,
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
      "evaluated_at": 1760291606
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
  "sig": "b7d046e9697891d169ddb877b48f2f85734393c26a9f8d703822d13690ef5114"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279650502
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 44653161, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': 'f07ec2819f69af8b'}}}