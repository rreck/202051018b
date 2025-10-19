```json
{
  "id": "91b792192dc1f62d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290195,
  "host_pid": "9e6742732c60:1",
  "hash": "eb31d4cbbc47adeb1bfa3e34c6d32a56d595870eb93f4df3e497d634dd4d8f88",
  "cid": "QmV1eb31d4cbbc47adeb1bfa3e34c6d32a56d595870e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290195,
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
      "evaluated_at": 1760290195
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
  "sig": "e384741de46a5081291bc6965e63b9043bf78337ac8b2872f69c4a1e499fcfcd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276534342
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 44951184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285763, 'matching_hash': '3bb091557ce86ea6'}}}d_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}