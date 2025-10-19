```json
{
  "id": "90e7509c298d951d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287188,
  "host_pid": "9e6742732c60:1",
  "hash": "7c18ef4aeb68c0782a056f4ba6fa13e2ac632cedbd90e519c2754a2e39c12381",
  "cid": "QmV17c18ef4aeb68c0782a056f4ba6fa13e2ac632ced",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287188,
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
      "evaluated_at": 1760287188
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "a82cf75bb31a5d1959049c85bbabdf16c723bb508986f7a49af1f9473130289c"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000031910208
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 19441302, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285763, 'matching_hash': '8397d9ba38a9dfb7'}}}