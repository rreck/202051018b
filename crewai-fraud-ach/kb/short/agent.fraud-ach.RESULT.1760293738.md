```json
{
  "id": "5904561a2a7aa446",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293738,
  "host_pid": "9e6742732c60:1",
  "hash": "9a3ef71dc779b9db1e5ef2c93ef69c793bfd45122ad5cd4d181e629212d154b3",
  "cid": "QmV19a3ef71dc779b9db1e5ef2c93ef69c793bfd4512",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293738,
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
      "evaluated_at": 1760293738
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
  "sig": "5d417bf27f0c52dfa937b434c55ab42041890c79c3bd9eeb4833b7c920b89a1f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151005829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 60608576, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285765, 'matching_hash': 'ea26f24e3d1967f5'}}}