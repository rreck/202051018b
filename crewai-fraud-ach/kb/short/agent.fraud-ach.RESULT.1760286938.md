```json
{
  "id": "a2ae083d6a3bbd6e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286938,
  "host_pid": "9e6742732c60:1",
  "hash": "b2b73842178e3cb2c8db9065d7e0bff7d11ac4b0c93349b745fc98c284539c2a",
  "cid": "QmV1b2b73842178e3cb2c8db9065d7e0bff7d11ac4b0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286938,
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
      "evaluated_at": 1760286938
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
  "sig": "4417f67a1a55415e6983616ea010e3f5449dd74d3d351e85c863aa803f8233fc"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 021000022605707
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 11584188, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285765, 'matching_hash': '50e001b692c48bf8'}}}