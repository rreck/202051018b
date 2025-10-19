```json
{
  "id": "823eedd8c8a4f879",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293570,
  "host_pid": "9e6742732c60:1",
  "hash": "5c2d8ffa6900cefe2da3240aecd9713f540c5a88cdfb0c90f1499b4fe76fa9ee",
  "cid": "QmV15c2d8ffa6900cefe2da3240aecd9713f540c5a88",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293570,
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
      "evaluated_at": 1760293570
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
  "sig": "1c7287b46e012d3f519d7478bc2d40c5f9aa70f95815e7bd84a92a7beed4e87e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465310802
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 82657757, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': '86dc5261411570c1'}}}