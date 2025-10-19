```json
{
  "id": "f59ce5b0b3035aba",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293756,
  "host_pid": "9e6742732c60:1",
  "hash": "fb30daa57b6ed8df2f6e0927728d29535dcd76d309208d59dae658be8719e00b",
  "cid": "QmV1fb30daa57b6ed8df2f6e0927728d29535dcd76d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293756,
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
      "evaluated_at": 1760293756
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
  "sig": "a7610ce05f53f06dd695e113fc7a28fb5f4f56a2d93eb32cf7081c99396b0d3f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022330150
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 99148500, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': 'b30e2736c805251a'}}}