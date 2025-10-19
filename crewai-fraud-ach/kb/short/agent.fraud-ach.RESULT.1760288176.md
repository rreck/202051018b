```json
{
  "id": "cd36d1e915d97dfb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288176,
  "host_pid": "9e6742732c60:1",
  "hash": "9e80d0bd1f3e6aaac7ae8deffea5732f53a878d5dff6dc8892a6eb5d603e2b8b",
  "cid": "QmV19e80d0bd1f3e6aaac7ae8deffea5732f53a878d5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288176,
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
      "evaluated_at": 1760288176
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
  "sig": "93d6b0ec5eff6e83d07e6212737dec1ec5c8a54b39f9d3224d7e000bf4317baa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034056272
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 85, 'threshold': 50, 'total_amount': 11748870, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 84, 'first_seen': 1760285763, 'matching_hash': 'aae4e2a94575911d'}}}