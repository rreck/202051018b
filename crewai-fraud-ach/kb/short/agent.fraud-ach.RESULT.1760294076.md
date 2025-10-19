```json
{
  "id": "e4e642810f9b330c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294076,
  "host_pid": "9e6742732c60:1",
  "hash": "ee43e5183f9f0ea526027fb703d73d90142db89e8250239fe628e68fc90c518a",
  "cid": "QmV1ee43e5183f9f0ea526027fb703d73d90142db89e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294076,
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
      "evaluated_at": 1760294076
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
  "sig": "d9ecff01dd4200b157091086c760b2388535759a1429d9cad2d3bc76e530040d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100277305476
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 94260705, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': 'e8a0d4fc67d0b61c'}}}