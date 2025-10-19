```json
{
  "id": "af7156e88323b7b0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293775,
  "host_pid": "9e6742732c60:1",
  "hash": "4b4e2e1d7e40954d41f4768e036b0ed5de15ed349a78629f3b54a27588169fd6",
  "cid": "QmV14b4e2e1d7e40954d41f4768e036b0ed5de15ed34",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293775,
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
      "evaluated_at": 1760293775
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
  "sig": "4a5205923559044f422dd8bc73d4fd6f9ebb0a2a8c1da9d6fcc2947fb07d8177"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031032710
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 225, 'threshold': 50, 'total_amount': 53370225, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 224, 'first_seen': 1760285763, 'matching_hash': 'e5dc8a38744b9e1c'}}}