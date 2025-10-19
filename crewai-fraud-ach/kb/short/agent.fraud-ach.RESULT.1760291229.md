```json
{
  "id": "cb006848f9a144d3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291229,
  "host_pid": "9e6742732c60:1",
  "hash": "2574ab13ea9d07f7d0b513ad07a6a1dfdfdf038f92c884113ed52365e1934642",
  "cid": "QmV12574ab13ea9d07f7d0b513ad07a6a1dfdfdf038f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291229,
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
      "evaluated_at": 1760291229
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "2e363bd9745c5f82e3840c12a575dc43407fa036f183360c3f3be1c2a78e5f64"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 503193792297075
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 170, 'threshold': 50, 'total_amount': 71091280, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 169, 'first_seen': 1760285764, 'matching_hash': 'f478a6eb1bcd883b'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '503193790', 'validation_error': 'Invalid routing number checksum'}}}