```json
{
  "id": "a368bbf1637470eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290692,
  "host_pid": "9e6742732c60:1",
  "hash": "723aa680f1f0d91aeb63185ff36d53a7d7816f64a880c2bcfe1c6f5ed709fedf",
  "cid": "QmV1723aa680f1f0d91aeb63185ff36d53a7d7816f64",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290692,
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
      "evaluated_at": 1760290692
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
  "sig": "2036cf5587a585713fd9a6db9d79ecd79b9e084f017f03dac00a282aeae349b8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021760547
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 157, 'threshold': 50, 'total_amount': 40728783, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 156, 'first_seen': 1760285763, 'matching_hash': 'fad63ed6e9f4a51a'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '408733730', 'validation_error': 'Invalid routing number checksum'}}}