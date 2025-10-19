```json
{
  "id": "44b952fd66c74ae4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290191,
  "host_pid": "9e6742732c60:1",
  "hash": "e39e8afd8a57db01f86349583bfe7cc486fee61508714938458a0084d56b95a2",
  "cid": "QmV1e39e8afd8a57db01f86349583bfe7cc486fee615",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290191,
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
      "evaluated_at": 1760290191
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
  "sig": "c62a56b808e2c2052e6caf921b1bffb39318a3faecc37a3b800f6dc4e11817ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022915367
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 144, 'threshold': 50, 'total_amount': 59870160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 143, 'first_seen': 1760285763, 'matching_hash': '4fdfaefd2437a484'}}}