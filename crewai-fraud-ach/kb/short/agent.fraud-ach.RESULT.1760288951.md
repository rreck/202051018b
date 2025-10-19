```json
{
  "id": "967c753ea19fe3eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288951,
  "host_pid": "9e6742732c60:1",
  "hash": "9a9c6a9d6f13920c8f6444062a75f7900a20e836ea04bb2e2a81a5cb272dbf15",
  "cid": "QmV19a9c6a9d6f13920c8f6444062a75f7900a20e836",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288951,
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
      "evaluated_at": 1760288951
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
  "sig": "8019a05468aec044de598001ff4305a62dd8f8ec8b7592b6cb22841155d3a11f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241906665
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 109, 'threshold': 50, 'total_amount': 28252582, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 108, 'first_seen': 1760285764, 'matching_hash': '6ca698820fae5f27'}}}