```json
{
  "id": "969c5b2891c2de5f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294700,
  "host_pid": "9e6742732c60:1",
  "hash": "6640bce6e67307eaf43f2ca4b109a10b0c6a0f104920eb1ae9e437f754c27547",
  "cid": "QmV16640bce6e67307eaf43f2ca4b109a10b0c6a0f10",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294700,
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
      "evaluated_at": 1760294701
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
  "sig": "e2fd1db30fab85c3195d9b8a6c51daa89f88cf4c1cca82bb62aeac2eec4a71bd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022956374
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 40445649, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': '4e30c52d3b71935d'}}}