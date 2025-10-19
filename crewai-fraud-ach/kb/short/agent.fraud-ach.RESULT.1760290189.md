```json
{
  "id": "7b4748bb64fb3bfe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290189,
  "host_pid": "9e6742732c60:1",
  "hash": "48a0e886873e538be9538b807d90b23e095023bef46269212f59e8e4491f444d",
  "cid": "QmV148a0e886873e538be9538b807d90b23e095023be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290189,
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
      "evaluated_at": 1760290189
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
  "sig": "d35056addc91be11bce180c1293a0c1e7cd6218464461fed7c8b8bc49dc9c615"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027703590
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 51818832, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285763, 'matching_hash': '3a097b663e3dde58'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '261425248', 'validation_error': 'Invalid routing number checksum'}}}