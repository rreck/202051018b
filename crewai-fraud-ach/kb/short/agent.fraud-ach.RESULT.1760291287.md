```json
{
  "id": "014cde285f362c20",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291287,
  "host_pid": "9e6742732c60:1",
  "hash": "90b55265242ff901caa3f6314bcc45898a0390230dd88fd20ebc8a4069abcc8c",
  "cid": "QmV190b55265242ff901caa3f6314bcc45898a039023",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291287,
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
      "evaluated_at": 1760291287
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
  "sig": "1e803fdcdc819bb855598e3a2f4528d91b1d48450550268f9bab881b2e957ee2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025001245
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 171, 'threshold': 50, 'total_amount': 36517563, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 170, 'first_seen': 1760285764, 'matching_hash': 'bf601f225a65579b'}}}